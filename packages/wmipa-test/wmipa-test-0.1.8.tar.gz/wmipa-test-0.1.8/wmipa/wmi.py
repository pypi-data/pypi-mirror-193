"""This module implements the Weighted Model Integration calculation.

The calculation leverages:
    - a Satisfiability Modulo Theories solver supporting All-SMT (e.g. MathSAT)
    - a software computing exact volume of polynomials (e.g. LattE Integrale)

Currently, three algorithms are supported:
    "BC" -- The baseline Block-Clause method.
    "AllSMT" -- Improves BC by leveraging the AllSAT feature of the SMT Solver.
    "PA" -- WMI with Predicate Abstraction, may reduce drastically the number of
        integrals computed.
    "SA-PA" -- Improves PA by making it aware of the structure of the weight function.
    "SA-PA-SK" -- Improves SA-PA by using a better encoding of the problem and a revised
        enumeration strategy

"""

__version__ = "0.999"
__author__ = "Paolo Morettin"

import math
from collections import defaultdict
from math import fsum

import mathsat
from pysmt.shortcuts import (
    And,
    Bool,
    Iff,
    Implies,
    Not,
    Real,
    Solver,
    serialize,
    simplify,
    substitute,
)
from pysmt.typing import BOOL, REAL
from sympy import solve, sympify

from wmipa import logger
from wmipa.integration import LatteIntegrator
from wmipa.utils import get_boolean_variables, get_lra_atoms, get_real_variables
from wmipa.weightconverter import SkeletonSimplifier
from wmipa.weights import Weights
from wmipa.wmiexception import WMIParsingException, WMIRuntimeException
from wmipa.wmivariables import WMIVariables


class WMI:
    """The class that has the purpose to calculate the Weighted Module Integration of
        a given support, weight function and query.

    Attributes:
        variables (WMIVariables): The list of variables created and used by WMI.
        weights (Weights): The representation of the weight function.
        chi (FNode): The pysmt formula that contains the support of the formula
        integrator (Integrator): The integrator to use.

    """

    # WMI methods
    MODE_BC = "BC"
    MODE_ALLSMT = "AllSMT"
    MODE_PA = "PA"
    MODE_SA_PA = "SAPA"
    MODE_SA_PA_SK = "SAPASK"
    MODES = [MODE_BC, MODE_ALLSMT, MODE_PA, MODE_SA_PA, MODE_SA_PA_SK]

    def __init__(self, chi, weight=Real(1), integrator=None, **options):
        """Default constructor.

        Args:
            chi (FNode): The support of the problem.
            weight (FNode, optional): The weight of the problem (default: 1).
            integrator: integrator instance (default: LatteIntegrator()).

        """
        self.variables = WMIVariables()
        self.weights = Weights(weight, self.variables)
        self.chi = chi

        if integrator is None:
            integrator = LatteIntegrator()
        self.integrator = integrator

        self.list_norm = set()
        self.norm_aliases = dict()
        self.skeleton_simplifier = SkeletonSimplifier()

    def computeMI_batch(self, phis, **options):
        """Calculates the MI on a batch of queries.

        Args:
            phis (list(FNode)): The list of the queries on which to calculate the MI.
            **options:
                - domA: set of pysmt vars encoding the Boolean integration domain
                    (optional)
                - domX: set of pysmt vars encoding the real integration domain
                    (optional)
                - mode: The mode to use when calculating MI.

        Returns:
            list(real): The list containing the result of each computation.
            list(int): The list containing the number of integrations for each
                computation that have been computed.

        """
        # save the old weight
        old_weights = self.weights
        old_variables = self.variables

        # calculate wmi with constant weight
        new_variables = WMIVariables()
        new_weights = Weights(Real(1), new_variables)
        self.weights = new_weights
        self.variables = new_variables

        volumes, integrations = self.computeWMI_batch(phis, **options)

        # restore old weight
        self.weights = old_weights
        self.variables = old_variables
        return volumes, integrations

    def computeWMI_batch(self, phis, **options):
        """Calculates the WMI on a batch of queries.

        Args:
            phis (list(FNode)): The list of the queries on which to calculate the WMI.
            **options:
                - domA: set of pysmt vars encoding the Boolean integration domain
                    (optional)
                - domX: set of pysmt vars encoding the real integration domain
                    (optional)
                - mode: The mode to use when calculating WMI.

        Returns:
            list(real): The list containing the result of each computation.
            list(int): The list containing the number of integrations for each
                computation that have been computed.

        """
        volumes = []
        integrations = []

        for phi in phis:
            volume, n_integrations = self.computeWMI(phi, **options)
            volumes.append(volume)
            integrations.append(n_integrations)

        return volumes, integrations

    def computeMI(self, phi, **options):
        """Calculates the MI on a single query.

        Args:
            phi (FNode): The query on which to calculate the MI.
            **options:
                - domA: set of pysmt vars encoding the Boolean integration domain
                    (optional)
                - domX: set of pysmt vars encoding the real integration domain
                    (optional)
                - mode: The mode to use when calculating MI.

        Returns:
            real: The result of the computation.
            int: The number of integrations that have been computed.

        """
        # save old weight
        old_weights = self.weights
        old_variables = self.variables

        # calculate wmi with constant weight
        new_variables = WMIVariables()
        new_weights = Weights(Real(1), new_variables)
        self.weights = new_weights
        self.variables = new_variables

        volume, n_integrations = self.computeWMI(phi, **options)

        # restore old weight
        self.weights = old_weights
        self.variables = old_variables
        return volume, n_integrations

    def computeWMI(self, phi, **options):
        """Calculates the WMI on a single query.

        Args:
            phi (FNode): The query on which to calculate the WMI.
            **options:
                - domA: set of pysmt vars encoding the Boolean integration domain
                    (optional)
                - domX: set of pysmt vars encoding the real integration domain
                    (optional)
                - mode: The mode to use when calculating WMI.

        Returns:
            real: The result of the computation.
            int: The number of integrations that have been computed.

        """
        domA = options.get("domA")
        domX = options.get("domX")
        mode = options.get("mode")
        cache = options.get("cache")
        ete = options.get("ete")
        if mode is None:
            mode = WMI.MODE_PA
        if mode not in WMI.MODES:
            err = "{}, use one: {}".format(mode, ", ".join(WMI.MODES))
            logger.error(err)
            raise WMIRuntimeException(WMIRuntimeException.INVALID_MODE, err)
        if cache is None:
            cache = -1
        self.cache = cache

        formula = And(phi, self.chi)
        # formula = self.chi

        # Add the phi to the support
        if mode == WMI.MODE_SA_PA:
            formula = And(formula, self.weights.weights_as_formula_euf)
        elif "SK" in mode:
            formula = And(formula, self.weights.weights_as_formula_sk)
        else:
            formula = And(formula, self.weights.labelling)

        # print("FORMULA: ", serialize(formula))
        logger.debug("Computing WMI with mode: {}".format(mode))
        self.variables: WMIVariables
        x = {
            x
            for x in get_real_variables(formula)
            if not (self.variables.is_weight_alias(x) or self.variables.is_euf_alias(x))
        }
        A = {
            x for x in get_boolean_variables(formula) if not self.variables.is_label(x)
        }

        # Currently, domX has to be the set of real variables in the
        # formula, whereas domA can be a superset of the boolean
        # variables A. The resulting volume is multiplied by 2^|domA - A|.
        factor = 1
        logger.debug("A: {}, domA: {}".format(A, domA))
        if domA is not None:
            if len(A - domA) > 0:
                logger.error(
                    "Domain of integration mismatch: A - domA = {}".format(A - domA)
                )
                raise WMIRuntimeException(
                    WMIRuntimeException.DOMAIN_OF_INTEGRATION_MISMATCH, A - domA
                )
            else:
                factor = 2 ** len(domA - A)

        logger.debug("factor: {}".format(factor))
        if domX is not None and domX != x:
            logger.error("Domain of integration mismatch")
            raise WMIRuntimeException(
                WMIRuntimeException.DOMAIN_OF_INTEGRATION_MISMATCH, x - domX
            )

        if ete:
            formula = self._eager_theory_encoding(formula)

        compute_with_mode = {
            WMI.MODE_BC: self._compute_WMI_BC,
            WMI.MODE_ALLSMT: self._compute_WMI_AllSMT,
            WMI.MODE_PA: self._compute_WMI_PA,
            WMI.MODE_SA_PA: self._compute_WMI_SA_PA,
            #  WMI.MODE_SA_PA_BOOL: self._compute_WMI_SA_PA,
            #  WMI.MODE_SA_PA_BOOL_TA: self._compute_WMI_SA_PA_TA,
            #  WMI.MODE_SA_PA_BOOL_TA_TA: self._compute_WMI_SA_PA_TA_TA,
            WMI.MODE_SA_PA_SK: self._compute_WMI_SA_PA_SK,
        }

        volume, n_integrations, n_cached = compute_with_mode[mode](
            formula, self.weights
        )

        volume = volume * factor
        logger.debug(
            "Volume: {}, n_integrations: {}, n_cached: {}".format(
                volume, n_integrations, n_cached
            )
        )

        return volume, n_integrations

    def _eager_theory_encoding(self, chi):
        implications = []
        for var in get_real_variables(chi):
            imp_lt = {}
            imp_gt = {}
            for literal in set(get_lra_atoms(chi)):
                if get_real_variables(literal) == {var}:
                    # convert the inequality to 'var op const'
                    s = solve(sympify(serialize(literal)))
                    arg = 0
                    if "inf" in str(s.args[0]) or "oo" in str(s.args[0]):
                        arg = 1
                    dis = s.args[arg]
                    if dis.args[0].is_Number:
                        # n < var, n <= var
                        const = float(dis.args[0])
                        eq = 1 if literal.is_lt() else 0
                        d = imp_gt
                    else:
                        # var < n, var <= n
                        const = float(dis.args[1])
                        eq = 0 if literal.is_lt() else 1
                        d = imp_lt
                    key = (const, eq)
                    if key not in d:
                        d[key] = []
                    d[key].append(literal)
            imp_lt = sorted(list(imp_lt.items()))
            imp_gt = sorted(list(imp_gt.items()), reverse=True)

            def compare(key, other_key, index):
                if index == 0:
                    return key <= other_key
                elif index == 1:
                    return key >= other_key

            lists = [imp_lt, imp_gt]
            for index_l, l in enumerate(lists):
                other_l = lists[(index_l + 1) % 2]
                for i, (key, literals) in enumerate(l):

                    # all literals in 'literals' are the same => Iff
                    for j, literal in enumerate(literals):
                        if j < len(literals) - 1:
                            implications.append(Iff(literal, literals[j + 1]))

                    # literal at random in the list (because they are all the same)
                    literal = literals[0]
                    if i < len(l) - 1:
                        _, literals_next = l[i + 1]
                        implications.append(Implies(literal, literals_next[0]))

                    # implications between one list and another
                    if len(other_l) > 0:
                        other_key, _ = other_l[0]
                        if compare(key, other_key, index_l):
                            index = 0
                            while (
                                    compare(key, other_l[index][0], index_l)
                                    and index < len(other_l) - 1
                            ):
                                index += 1
                            # other list [index-1 was the last correct implication]
                            #   [1 = get list of literals]
                            #   [0 = get random literal]
                            other_literal = other_l[index - 1][1][0]
                            implications.append(Implies(literal, Not(other_literal)))
        implications = And(implications)
        return And(chi, implications)

    @staticmethod
    def check_consistency(formula):
        """Checks if the formula has at least a total truth assignment
            which is both theory-consistent and it propositionally satisfies it.

        Args:
            formula (FNode): The pysmt formula to examine.

        Returns:
            bool: True if the formula satisfies the requirements, False otherwise.

        """
        for _ in WMI._model_iterator_base(formula):
            return True

        return False

    @staticmethod
    def _model_iterator_base(formula):
        """Finds all the total truth assignments that satisfy the given formula.

        Args:
            formula (FNode): The pysmt formula to examine.

        Yields:
            model: The model representing the next total truth assignment that
                satisfies the formula.

        """
        solver = Solver(name="msat")
        solver.add_assertion(formula)
        while solver.solve():
            model = solver.get_model()
            yield model
            atom_assignments = {a: model.get_value(a) for a in formula.get_atoms()}

            # Constrain the solver to find a different assignment
            solver.add_assertion(
                Not(And([Iff(var, val) for var, val in atom_assignments.items()]))
            )

    @staticmethod
    def _callback(model, converter, result):
        """Callback method useful when performing AllSAT on a formula.

        This method takes the model, converts it into a more suitable form and finally
            adds it into the given results list.

        Args:
            model (list): The model created by the solver.
            converter: The class that converts the model.
            result (list): The list where to append the converted model.

        Returns:
            int: 1 (This method requires to return an integer)

        """
        py_model = [converter.back(v) for v in model]
        result.append(py_model)
        return 1

    def _compute_TTAs(self, formula):
        """Computes the total truth assignments of the given formula.

        This method first labels the formula and then uses the functionality of mathsat
            called AllSAT to retrieve all the total truth assignments.

        Args:
            formula (FNode): The pysmt formula to examine.

        Returns:
            list: The list of all the total truth assignments.
            dict: The dictionary containing all the correspondence between the labels
                and their true value.

        """
        labels = {}
        # expressions = []
        # allsat_variables = set()

        # Label LRA atoms with fresh boolean variables
        labelled_formula, pa_vars, labels = self.label_formula(
            formula, formula.get_atoms()
        )

        # Perform AllSMT on the labelled formula
        solver = Solver(name="msat")
        converter = solver.converter
        solver.add_assertion(labelled_formula)
        models = []
        mathsat.msat_all_sat(
            solver.msat_env(),
            [converter.convert(v) for v in pa_vars],
            lambda model: WMI._callback(model, converter, models),
        )
        return models, labels

    def _compute_WMI_AllSMT(self, formula, weights):
        """Computes WMI using the AllSMT algorithm.

        This method retrieves all the total truth assignments of the given formula,
            it then calculates the weight for the assignments and finally asks the
            integrator to compute the integral of the problem.

        Args:
            formula (FNode): The pysmt formula on which to compute the WMI.
            weights (FNode): The pysmt formula representing the weight function.

        Returns:
            real: The final volume of the integral computed by summing up all the
                integrals' results.
            int: The number of problems that have been computed.

        """
        models, labels = self._compute_TTAs(formula)
        problems = []
        for _, model in enumerate(models):
            # retrieve truth assignments for the original atoms of the formula
            atom_assignments = {}
            for atom, value in WMI._get_assignments(model).items():
                if atom in labels:
                    atom = labels[atom]
                atom_assignments[atom] = value
            problem = self._create_problem(atom_assignments, weights)
            problems.append(problem)

        results, cached = self.integrator.integrate_batch(problems, self.cache)
        volume = fsum(results)
        return volume, len(problems) - cached, cached

    def _create_problem(self, atom_assignments, weights, on_labels=True):
        """Create a tuple containing the problem to integrate.

        It first finds all the aliases in the atom_assignments, then it takes the
            actual weight (based on the assignment).
        Finally, it creates the problem tuple with all the info in it.

        Args:
            atom_assignments (dict): The list of assignments and relative value
                (True, False)
            weights (Weight): The weight of the problem.
            on_labels (bool): If True assignment is expected to be over labels of
                weight condition
                otherwise it is expected to be over unlabelled conditions

        Returns:
            tuple: The problem on which to calculate the integral formed by
                (atom assignment, actual weight, list of aliases).

        """
        aliases = {}
        for atom, value in atom_assignments.items():
            if value is True and atom.is_equals():
                alias, expr = self._parse_alias(atom)
                if self.variables.is_weight_alias(alias):
                    continue

                # check that there are no multiple assignments of the same alias
                if alias not in aliases:
                    aliases[alias] = expr
                else:
                    msg = "Multiple assignments to the same alias"
                    raise WMIParsingException(
                        WMIParsingException.MULTIPLE_ASSIGNMENT_SAME_ALIAS
                    )

        current_weight, cond_assignments = weights.weight_from_assignment(
            atom_assignments, on_labels=on_labels
        )
        return atom_assignments, current_weight, aliases, cond_assignments

    def _parse_alias(self, equality):
        """Takes an equality and parses it.

        Args:
            equality (FNode): The equality to parse.

        Returns:
            alias (FNode): The name of the alias.
            expr (FNode): The value of the alias.

        Raises:
            WMIParsingException: If the equality is not of the type
                (Symbol = real_formula) or vice-versa.

        """
        assert equality.is_equals(), "Not an equality"
        left, right = equality.args()
        if left.is_symbol() and (left.get_type() == REAL):
            alias, expr = left, right
        elif right.is_symbol() and (right.get_type() == REAL):
            alias, expr = right, left
        else:
            raise WMIParsingException(
                WMIParsingException.MALFORMED_ALIAS_EXPRESSION, equality
            )
        return alias, expr

    def _compute_WMI_BC(self, formula, weights):
        """Computes WMI using the Block Clause algorithm.

        This method retrieves all the total truth assignments of the given formula
            one by one thanks to the Block Clause algorithm.
            This particular algorithm finds a model that satisfy the formula, it then
            adds the negation of this model to the formula itself in order to constrain
            the solver to fine another model that satisfies it.

        Args:
            formula (FNode): The pysmt formula on which to compute the WMI.
            weights (FNode): The pysmt formula representing the weight function.

        Returns:
            real: The final volume of the integral computed by summing up all the
                integrals' results.
            int: The number of problems that have been computed.

        """
        problems = []
        for index, model in enumerate(WMI._model_iterator_base(formula)):
            atom_assignments = {
                a: model.get_value(a).constant_value() for a in formula.get_atoms()
            }
            problem = self._create_problem(atom_assignments, weights)
            problems.append(problem)

        results, cached = self.integrator.integrate_batch(problems, self.cache)
        volume = fsum(results)
        return volume, len(problems) - cached, cached

    def _compute_WMI_PA_no_boolean(
            self, lab_formula, pa_vars, labels, other_assignments=None
    ):
        """Finds all the assignments that satisfy the given formula using AllSAT.

        Args:
            lab_formula (FNode): The labelled pysmt formula to examine.
            pa_vars ():
            labels (dict): The dictionary containing the correlation between each label
                and their true value.

        Yields:
            dict: One of the assignments that satisfies the formula.

        """
        if other_assignments is None:
            other_assignments = {}
        solver = Solver(
            name="msat", solver_options={"dpll.allsat_minimize_model": "true"}
        )
        converter = solver.converter
        solver.add_assertion(lab_formula)
        lra_assignments = []
        mathsat.msat_all_sat(
            solver.msat_env(),
            [converter.convert(v) for v in pa_vars],
            lambda model: WMI._callback(model, converter, lra_assignments),
        )
        for mu_lra in lra_assignments:
            assignments = {}
            for atom, value in WMI._get_assignments(mu_lra).items():
                if atom in labels:
                    atom = labels[atom]
                assignments[atom] = value
            assignments.update(other_assignments)
            yield assignments

    def _compute_WMI_PA(self, formula, weights):
        """Computes WMI using the Predicate Abstraction (PA) algorithm.

        Args:
            formula (FNode): The formula on which to compute WMI.
            weights (Weight): The corresponding weight.

        Returns:
            real: The final volume of the integral computed by summing up all the
                integrals' results.
            int: The number of problems that have been computed.

        """
        problems = []
        boolean_variables = get_boolean_variables(formula)
        if len(boolean_variables) == 0:
            # Enumerate partial TA over theory atoms
            lab_formula, pa_vars, labels = self.label_formula(
                formula, formula.get_atoms()
            )
            # Predicate abstraction on LRA atoms with minimal models
            for assignments in self._compute_WMI_PA_no_boolean(
                    lab_formula, pa_vars, labels
            ):
                problem = self._create_problem(assignments, weights)
                problems.append(problem)
        else:
            solver = Solver(name="msat")
            converter = solver.converter
            solver.add_assertion(formula)
            boolean_models = []
            # perform AllSAT on the Boolean variables
            mathsat.msat_all_sat(
                solver.msat_env(),
                [converter.convert(v) for v in boolean_variables],
                lambda model: WMI._callback(model, converter, boolean_models),
            )

            logger.debug("n_boolean_models: {}".format(len(boolean_models)))
            # for each boolean assignment mu^A of F
            for model in boolean_models:
                atom_assignments = {}
                boolean_assignments = WMI._get_assignments(model)
                atom_assignments.update(boolean_assignments)
                subs = {k: Bool(v) for k, v in boolean_assignments.items()}
                f_next = formula
                # iteratively simplify F[A<-mu^A], getting (possibly part.) mu^LRA
                while True:
                    f_before = f_next
                    f_next = simplify(substitute(f_before, subs))
                    lra_assignments, over = WMI._parse_lra_formula(f_next)
                    subs = {k: Bool(v) for k, v in lra_assignments.items()}
                    atom_assignments.update(lra_assignments)
                    if over or lra_assignments == {}:
                        break

                if not over:
                    # predicate abstraction on LRA atoms with minimal models
                    lab_formula, pa_vars, labels = self.label_formula(
                        f_next, f_next.get_atoms()
                    )
                    expressions = []
                    for k, v in atom_assignments.items():
                        if k.is_theory_relation():
                            if v:
                                expressions.append(k)
                            else:
                                expressions.append(Not(k))

                    lab_formula = And([lab_formula] + expressions)
                    for assignments in self._compute_WMI_PA_no_boolean(
                            lab_formula, pa_vars, labels, atom_assignments
                    ):
                        problem = self._create_problem(assignments, weights)
                        problems.append(problem)
                else:
                    # integrate over mu^A & mu^LRA
                    problem = self._create_problem(atom_assignments, weights)
                    problems.append(problem)
        results, cached = self.integrator.integrate_batch(problems, self.cache)
        volume = fsum(results)
        return volume, len(problems) - cached, cached

    def _get_allsat(self, formula, use_ta=False, atoms=None, options=None):
        """
        Gets the list of assignments that satisfy the formula.

        Args:
            formula (FNode): The formula to satisfy
            use_ta (bool, optional): If true the assignments can be partial.
                Defaults to False.
            atoms (list, optional): List of atoms on which to find the assignments.
                Defaults to the boolean atoms of the formula.

        Yields:
            list: assignments on the atoms
        """
        if options is None:
            options = {}
        if use_ta:
            solver_options = {
                "dpll.allsat_minimize_model": "true",
                "dpll.allsat_allow_duplicates": "false",
                "preprocessor.toplevel_propagation": "false",
                "preprocessor.simplification": "0",
            }
        else:
            solver_options = {}

        solver_options.update(options)
        if atoms is None:
            atoms = get_boolean_variables(formula)

        for atom in atoms:
            if not atom.is_symbol(BOOL) and atom not in self.list_norm:
                _ = self.normalize_assignment(atom, True)
        solver = Solver(name="msat", solver_options=solver_options)
        converter = solver.converter

        solver.add_assertion(formula)

        models = []
        mathsat.msat_all_sat(
            solver.msat_env(),
            [converter.convert(v) for v in atoms],
            lambda model: WMI._callback(model, converter, models),
        )

        for model in models:
            assignments = {}
            for atom, value in WMI._get_assignments(model).items():
                if atom.is_symbol(BOOL):
                    assignments[atom] = value
                else:
                    subterms = self.normalize_assignment(atom, False)

                    assert (
                            frozenset(subterms) in self.norm_aliases
                    ), "Atom {}\n(subterms: {})\nnot found in\n{}".format(
                        atom.serialize(),
                        subterms,
                        "\n".join(str(x) for x in self.norm_aliases.keys()),
                    )
                    for element_of_normalization in self.norm_aliases[
                        frozenset(subterms)
                    ]:
                        assignments[element_of_normalization] = (
                            not value if element_of_normalization.is_lt() else value
                        )
            yield assignments

    def normalize_coefficient(self, val, normalizing_coefficient):
        midvalue = round(float(val) / abs(normalizing_coefficient), 10)
        if abs(midvalue - round(float(midvalue))) < 0.00000001:
            return round(float(midvalue))
        return midvalue

    def normalize_assignment(self, assignment, add_to_norms_aliases):
        self.list_norm.add(assignment)
        if not assignment.is_lt():
            list_terms = [(assignment.args()[0], 1), (assignment.args()[1], -1)]
        else:
            list_terms = [(assignment.args()[0], -1), (assignment.args()[1], 1)]
        symbols = defaultdict(float)
        normalizing_coefficient = 0.0
        min_abs_coefficient = math.inf

        for term, coeff in list_terms:
            if term.is_real_constant():
                normalizing_coefficient += term.constant_value() * coeff
            elif term.is_plus():
                list_terms.extend([(atom, coeff) for atom in term.args()])
            elif term.is_minus():
                child1 = term.args()[0]
                child2 = term.args()[1]
                list_terms.append((child1, coeff))
                list_terms.append((child2, -1.0 * coeff))
            elif term.is_times():
                child1 = term.args()[0]
                child2 = term.args()[1]

                if child1.is_real_constant() and child2.is_real_constant():
                    # constant += child1.constant_value() * child2.constant_value()
                    list_terms.append(
                        (child1.constant_value() * child2.constant_value(), coeff)
                    )
                elif child1.is_real_constant():
                    list_terms.append((child2, coeff * child1.constant_value()))
                elif child2.is_real_constant():
                    list_terms.append((child1, coeff * child2.constant_value()))
            else:
                symbols[term] += coeff
                min_abs_coefficient = min(min_abs_coefficient, abs(coeff))

        normalized_assignment = list()
        normalized_assignment2 = list()

        if assignment.is_equals():
            normalized_assignment.append("=")
            normalized_assignment2.append("=")
        else:
            normalized_assignment.append("<=/>=")

        if normalizing_coefficient == 0.0:
            normalized_assignment.append(0.0)
            normalizing_coefficient = min_abs_coefficient
            if assignment.is_equals():
                normalized_assignment2.append(0.0)
        else:
            normalized_assignment.append(
                normalizing_coefficient / abs(normalizing_coefficient)
            )
            if assignment.is_equals():
                normalized_assignment2.append(
                    (-normalizing_coefficient / abs(normalizing_coefficient))
                )

        for term in symbols:
            normalized_assignment.append(
                (
                    term,
                    self.normalize_coefficient(symbols[term], normalizing_coefficient),
                )
            )
            if assignment.is_equals():
                normalized_assignment2.append(
                    (
                        term,
                        self.normalize_coefficient(
                            -symbols[term], normalizing_coefficient
                        ),
                    )
                )

        if add_to_norms_aliases:
            if frozenset(normalized_assignment) not in self.norm_aliases:
                self.norm_aliases[frozenset(normalized_assignment)] = list()
            self.norm_aliases[frozenset(normalized_assignment)].append(assignment)
            # print("ADDING", frozenset(normalized_assignment), "for", assignment)
            if assignment.is_equals():
                if frozenset(normalized_assignment2) not in self.norm_aliases:
                    self.norm_aliases[frozenset(normalized_assignment2)] = list()
                self.norm_aliases[frozenset(normalized_assignment2)].append(assignment)
                # print("ADDING", frozenset(normalized_assignment2), "for", assignment)

        return None if add_to_norms_aliases else normalized_assignment

    def _compute_WMI_PA_no_boolean_no_label(self, lra_formula, other_assignments=None):
        """Finds all the assignments that satisfy the given formula using AllSAT.

        Args:
            lra_formula (FNode): The non-labelled pysmt formula to examine.

        Yields:
            dict: One of the assignments that satisfies the formula.

        """
        # for SAPA filter out new aliases for the weight function written as a formula
        if other_assignments is None:
            other_assignments = {}
        lra_atoms = {
            atom
            for atom in lra_formula.get_atoms()
            if not (self.variables.is_cnf_label(atom) or (
                    atom.is_equals() and self.variables.is_weight_alias(atom.arg(0))
            ))
        }
        # bools = {x for x in get_boolean_variables(lra_formula)
        #         if not self.variables.is_weight_bool(x)}
        # assert len(bools) == 0, bools

        lra_assignments = self._get_allsat(lra_formula, use_ta=True, atoms=lra_atoms)
        for mu_lra in lra_assignments:
            mu_lra.update(other_assignments)
            yield mu_lra

    def _simplify_formula(self, formula, subs, atom_assignments):
        """Substitute the subs in the formula and iteratively simplify it.
        atom_assignments is updated with unit-propagated atoms.

        Args:
            formula (FNode): The formula to simplify.
            subs (dict): Dictionary with the substitutions to perform.
            atom_assignments (dict): Dictionary with atoms and assigned value.

        Returns:
            bool: True if the formula is completely simplified.
            FNode: The simplified formula.
        """
        subs = {k: Bool(v) for k, v in subs.items()}
        f_next = formula
        # iteratively simplify F[A<-mu^A], getting (possibly part.) mu^LRA
        while True:
            f_before = f_next
            f_next = self.skeleton_simplifier.simplify(substitute(f_before, subs))
            lra_assignments, over = WMI._parse_lra_formula(f_next)
            subs = {k: Bool(v) for k, v in lra_assignments.items()}
            atom_assignments.update(lra_assignments)
            if over or lra_assignments == {}:
                break

        if not over:
            # formula not completely simplified, add conjunction of assigned LRA atoms
            expressions = []
            for k, v in atom_assignments.items():
                if k.is_theory_relation():
                    if v:
                        expressions.append(k)
                    else:
                        expressions.append(Not(k))
            f_next = And([f_next] + expressions)
        return over, f_next

    def _compute_WMI_SA_PA(self, formula, weights, use_ta=True):
        """Computes WMI using the Predicate Abstraction (PA) algorithm using Structure
            Awareness.

        Args:
            formula (FNode): The formula on which to compute WMI.
            weights (Weight): The corresponding weight.

        Returns:
            real: The final volume of the integral computed by summing up all the
                integrals' results.
            int: The number of problems that have been computed.

        """
        problems = []

        boolean_variables = get_boolean_variables(formula)

        # number of booleans not assigned in each problem
        n_bool_not_assigned = []
        if len(boolean_variables) == 0:
            # Enumerate partial TA over theory atoms
            for assignments in self._compute_WMI_PA_no_boolean_no_label(formula):
                problem = self._create_problem(assignments, weights, on_labels=False)
                problems.append(problem)
                n_bool_not_assigned.append(0)
        else:
            boolean_models = self._get_allsat(
                formula, use_ta=use_ta, atoms=boolean_variables
            )

            # logger.debug("n_boolean_models: {}".format(len(boolean_models)))
            # for each (partial) boolean assignment mu^A of F
            for boolean_assignments in boolean_models:
                atom_assignments = dict(boolean_assignments)
                # simplify the formula
                over, lra_formula = self._simplify_formula(
                    formula, boolean_assignments, atom_assignments
                )

                residual_booleans = get_boolean_variables(lra_formula)

                # if some boolean have not been simplified, find TTA on them
                if len(residual_booleans) > 0:
                    # compute TTA
                    residual_boolean_models = self._get_allsat(
                        lra_formula, atoms=residual_booleans
                    )
                else:
                    # all boolean variables have been assigned
                    residual_boolean_models = [[]]

                for residual_boolean_assignments in residual_boolean_models:
                    curr_atom_assignments = dict(atom_assignments)
                    if len(residual_boolean_assignments) > 0:
                        # simplify the formula
                        curr_atom_assignments.update(residual_boolean_assignments)
                        over, curr_lra_formula = self._simplify_formula(
                            lra_formula,
                            residual_boolean_assignments,
                            curr_atom_assignments,
                        )
                    else:
                        curr_lra_formula = lra_formula

                    b_not_assigned = len(boolean_variables) - len(boolean_assignments) - len(
                        residual_boolean_assignments)

                    if not over:
                        # predicate abstraction on LRA atoms with minimal models
                        for assignments in self._compute_WMI_PA_no_boolean_no_label(
                                curr_lra_formula, curr_atom_assignments
                        ):
                            problem = self._create_problem(
                                assignments, weights, on_labels=False
                            )
                            problems.append(problem)
                            n_bool_not_assigned.append(b_not_assigned)
                    else:
                        # integrate over mu^A & mu^LRA
                        problem = self._create_problem(
                            curr_atom_assignments, weights, on_labels=False
                        )

                        problems.append(problem)
                        n_bool_not_assigned.append(b_not_assigned)
        results, cached = self.integrator.integrate_batch(problems, self.cache)
        assert len(n_bool_not_assigned) == len(results)
        # multiply each volume by 2^(|A| - |mu^A|)
        volume = fsum(r * 2 ** i for i, r in zip(n_bool_not_assigned, results))
        return volume, len(problems) - cached, cached

    def _compute_WMI_SA_PA_SK(self, formula, weights):
        problems = []

        cnf_labels = {b for b in get_boolean_variables(formula) if
                      self.variables.is_cnf_label(b) or self.variables.is_cond_label(b)}
        boolean_variables = get_boolean_variables(formula) - cnf_labels
        lra_atoms = get_lra_atoms(formula)

        # number of booleans not assigned in each problem
        n_bool_not_assigned = []

        if len(boolean_variables) == 0:
            # Enumerate partial TA over theory atoms
            for assignments in self._get_allsat(formula, use_ta=True, atoms=lra_atoms):
                problem = self._create_problem(assignments, weights, on_labels=False)
                problems.append(problem)
                n_bool_not_assigned.append(0)

        else:
            boolean_models = self._get_allsat(
                formula, use_ta=True, atoms=boolean_variables,
            )

            for boolean_assignments in boolean_models:
                atom_assignments = dict(boolean_assignments)

                # simplify the formula
                over, res_formula = self._simplify_formula(
                    formula, boolean_assignments, atom_assignments
                )

                if not over:
                    # boolean variables first (discard cnf labels)
                    residual_atoms = list(get_boolean_variables(res_formula).intersection(boolean_variables)) + \
                                     list(get_lra_atoms(res_formula))

                    # may be both on LRA and boolean atoms
                    residual_models = self._get_allsat(
                        res_formula, use_ta=True, atoms=residual_atoms
                    )
                    for residual_assignments in residual_models:
                        curr_atom_assignments = dict(atom_assignments)
                        curr_atom_assignments.update(residual_assignments)

                        b_not_assigned = boolean_variables - curr_atom_assignments.keys()

                        problem = self._create_problem(
                            curr_atom_assignments, weights, on_labels=False
                        )
                        problems.append(problem)
                        n_bool_not_assigned.append(len(b_not_assigned))
                else:
                    b_not_assigned = boolean_variables - boolean_assignments.keys()

                    problem = self._create_problem(
                        atom_assignments, weights, on_labels=False
                    )
                    problems.append(problem)
                    n_bool_not_assigned.append(len(b_not_assigned))

        results, cached = self.integrator.integrate_batch(problems, self.cache)

        assert len(n_bool_not_assigned) == len(results)
        # multiply each volume by 2^(|A| - |mu^A|)
        volume = fsum(r * 2 ** i for i, r in zip(n_bool_not_assigned, results))
        return volume, len(problems) - cached, cached

    def label_formula(self, formula, atoms_to_label):
        """Labels every atom in the input with a new fresh WMI variable.

        Args:
            formula (FNode): The formula containing the atoms.
            atoms_to_label (list): The list of atoms to assign a new label.

        Returns:
            labelled_formula (FNode): The formula with the labels in it and their
                respective atoms.
            pa_vars (set): The list of all the atoms_to_label (as labels).
            labels (dict): The list of the labels and correspondent atom assigned to it.

        """
        expressions = []
        labels = {}
        pa_vars = set()
        j = 0
        for a in atoms_to_label:
            if a.is_theory_relation():
                label_a = self.variables.new_wmi_label(j)
                j += 1
                expressions.append(Iff(label_a, a))
                labels[label_a] = a
                pa_vars.add(label_a)
            else:
                pa_vars.add(a)

        labelled_formula = And([formula] + expressions)

        return labelled_formula, pa_vars, labels

    @staticmethod
    def _get_assignments(literals):
        """Retrieve the assignments (formula: truth value) from a list of literals
            (positive or negative).

        Args:
            literals (list): The list of the literals.

        Returns:
            assignments (dict): The list of atoms and corresponding truth value.

        """
        assignments = {}
        for literal in literals:
            if literal.is_not():
                value = False
                atom = literal.arg(0)
            else:
                value = True
                atom = literal
            assert atom.is_theory_relation or (
                    atom.is_symbol() and atom.get_type() == BOOL
            )
            assignments[atom] = value

        return assignments

    @staticmethod
    def _parse_lra_formula(formula):
        """Wrapper for _plra_rec.

        Args:
            formula (FNode): The formula to parse.

        Returns:
            dict: the list of FNode in the formula with the corresponding truth value.
            bool: boolean that indicates if there are no more truth assignment to
                extract.

        """
        return WMI._plra_rec(formula, True)

    @staticmethod
    def _plra_rec(formula, pos_polarity):
        """This method extract all sub formulas in the formula and returns them as a dictionary.

        Args:
            formula (FNode): The formula to parse.
            pos_polarity (bool): The polarity of the formula.

        Returns:
            dict: the list of FNode in the formula with the corresponding truth value.
            bool: boolean that indicates if there are no more truth assignment to
                extract.

        """
        if formula.is_bool_constant():
            return {}, True
        elif formula.is_theory_relation() or formula.is_symbol(BOOL):
            return {formula: pos_polarity}, True
        elif formula.is_not():
            return WMI._plra_rec(formula.arg(0), not pos_polarity)
        elif formula.is_and() and pos_polarity:
            assignments = {}
            over = True
            for a in formula.args():
                assignment, rec_over = WMI._plra_rec(a, True)
                assignments.update(assignment)
                over = rec_over and over
            return assignments, over
        elif formula.is_or() and not pos_polarity:
            assignments = {}
            over = True
            for a in formula.args():
                assignment, rec_over = WMI._plra_rec(a, False)
                assignments.update(assignment)
                over = rec_over and over
            return assignments, over
        elif formula.is_implies() and not pos_polarity:
            assignments, over_left = WMI._plra_rec(formula.arg(0), True)
            assignment_right, over_right = WMI._plra_rec(formula.arg(1), False)
            assignments.update(assignment_right)
            return assignments, over_left and over_right
        else:
            return {}, False
