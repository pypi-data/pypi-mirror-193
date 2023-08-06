import re
import time
from abc import abstractmethod
from fractions import Fraction
from multiprocessing import Manager, Pool
from subprocess import call
from tempfile import NamedTemporaryFile

from pysmt.shortcuts import LE, LT

from wmipa.integration.integrator import Integrator
from wmipa.integration.polytope import Polynomial


class CacheIntegrator(Integrator):
    """This class handles the integration of polynomial functions over (convex) polytopes.
    It is a wrapper for an integrator that reads (writes) input (output) from (to) file.
    It implements different levels of caching (-1, 0, 1, 2, 3).

    It inherits from the abstract class Integrator.

    Attributes:
        n_threads (int): The number of threads to use.
        stub_integrate (bool): If True, the values will not be computed (0 is returned)
    """

    DEF_N_THREADS = 7

    def __init__(self, n_threads=DEF_N_THREADS, stub_integrate=False):
        """Default constructor.

        Args:
            **options:
                - algorithm: Defines the algorithm to use when integrating.
                - n_threads: Defines the number of threads to use.
                - stub_integrate: If True the integrals will not be computed

        """

        self.n_threads = n_threads
        self.stub_integrate = stub_integrate
        self.hashTable = HashTable()
        self.integration_time = 0.0

    def get_integration_time(self):
        return self.integration_time

    def _integrate_problem_or_cached(self, integrand, polytope, key, cache):
        value = self.hashTable.get(key)
        if value is not None:
            return value, True
        value = self._integrate_problem(integrand, polytope)
        if cache:
            self.hashTable.set(key, value)
        return value, False

    @abstractmethod
    def _integrate_problem(self, integrand, polytope) -> float:
        pass

    def cache_1(self, polytope, integrand, cond_assignments):
        variables = list(integrand.variables.union(polytope.variables))
        return self.hashTable.key(polytope, cond_assignments, variables), polytope

    def cache_2(self, polytope, integrand, _):
        return self.hashTable.key_2(polytope, integrand), polytope

    def cache_3(self, polytope, integrand, _):
        polytope = self._remove_redundancy(polytope)
        if polytope is None:
            return None, None
        return self.cache_2(polytope, integrand, _)

    def integrate_batch(self, problems, cache, *args, **kwargs):
        """Integrates a batch of problems of the type {atom_assignments, weight, aliases}

        Args:
            problems (list(atom_assignments, weight, aliases)): The list of problems to
                integrate.
            cache (int): The level of caching to use (range -1, 0, 1, 2, 3).

        """

        EMPTY = -1
        cache_modes = {
            -1: self.cache_1,
            0: self.cache_1,
            1: self.cache_1,
            2: self.cache_2,
            3: self.cache_3,
        }
        if cache not in cache_modes:
            modes = map(str, cache_modes.keys())
            raise Exception(
                f"Unsupported cache mode. Supported modes are ({', '.join(modes)})"
            )
        cache_fn = cache_modes[cache]

        problems_to_integrate = {}
        problem_id = []
        cached = 0
        for index, (atom_assignments, weight, aliases, cond_assignments) in enumerate(
                problems
        ):
            integrand, polytope = self._convert_to_problem(
                atom_assignments, weight, aliases
            )
            key, polytope = cache_fn(polytope, integrand, cond_assignments)
            if polytope is not None and not polytope.is_empty():
                # cache >= 1 recognize duplicates before calling the integrator
                pid = key if cache >= 1 else index
                if pid not in problems_to_integrate:
                    problem = (
                        len(problems_to_integrate),
                        integrand,
                        polytope,
                        key,
                        cache >= 0,
                    )
                    problems_to_integrate[pid] = problem
                else:
                    # duplicate found
                    cached += 1
                problem_id.append(problems_to_integrate[pid][0])
            else:
                problem_id.append(EMPTY)

        problems_to_integrate = problems_to_integrate.values()
        assert len(problem_id) == len(problems)
        # Handle multithreading
        start_time = time.time()
        pool = Pool(self.n_threads)
        results = pool.map(self._integrate_wrapper, problems_to_integrate)
        pool.close()
        pool.join()
        values = [0.0 if pid == EMPTY else results[pid][0] for pid in problem_id]
        cached += sum([(pid == EMPTY) or results[pid][1] for pid in problem_id])
        assert len(values) == len(problems)

        self.integration_time = time.time() - start_time
        return values, cached

    def _integrate_wrapper(self, problem):
        """A wrapper to handle multithreading."""
        _, integrand, polytope, key, cache = problem
        return self._integrate_problem_or_cached(integrand, polytope, key, cache)

    def integrate(self, atom_assignments, weight, aliases, cond_assignments, cache, *args, **kwargs):
        """Integrates a problem of the type {atom_assignments, weight, aliases}

        Args:
            problem (atom_assignments, weight, aliases): The problem to integrate.
            cond_assignments (tuple): truth values for the conditions
            cache (int): The level of caching to use (range -1, 0, 1, 2, 3).


        Returns:
            real: The integration result.

        """
        integrand, polytope = self._convert_to_problem(
            atom_assignments, weight, aliases
        )
        return self._integrate_problem_or_cached(
            integrand, polytope, cond_assignments, cache
        )

    @classmethod
    @abstractmethod
    def _make_problem(cls, weight, bounds, aliases):
        """Creates a problem of the type (integrand, polytope) from the given arguments.
        Args:
            weight (FNode): The weight of the integrand.
            bounds (list): The bounds of the polytope.
            aliases (dict): The aliases of the variables.

        Returns:
            integrand (Integrand): The problem to integrate.
            polytope (Polytope): The polytope to integrate over.
        """
        pass

    @classmethod
    def _convert_to_problem(cls, atom_assignments, weight, aliases):
        """Transforms an assignment into a problem, defined by:
            - a polynomial integrand
            - a convex polytope.

        Args:
            atom_assignments (dict): The assignment of the problem.
            weight (FNode): The weight of the problem.
            aliases (dict): The list of all the alias variables (like PI=3.14)

        Returns:
            integrand (Integrand): A representation of the weight.
            polytope (Polytope): The polytope representing the list of inequalities.

        """
        bounds = []
        for atom, value in atom_assignments.items():
            assert isinstance(value, bool), "Assignment value should be Boolean"

            # Skip atoms without variables
            if len(atom.get_free_variables()) == 0:
                continue

            if value is False:
                # If the negative literal is an inequality, change its
                # direction
                if atom.is_le():
                    left, right = atom.args()
                    atom = LT(right, left)
                elif atom.is_lt():
                    left, right = atom.args()
                    atom = LE(right, left)

            # Add a bound if the atom is an inequality
            if atom.is_le() or atom.is_lt():
                bounds.append(atom)

        return cls._make_problem(weight, bounds, aliases)

    def _remove_redundancy(self, polytope):
        polytope.bounds = list(set(polytope.bounds))
        polytope, internal_point = self._preprocess(polytope)
        if polytope is None:
            return None
        non_redundant_index = []
        to_analyze = list(range(0, len(polytope.bounds)))
        while len(to_analyze) > 0:
            index = to_analyze[0]
            non_redundant, essential_index = self._clarkson(
                polytope, internal_point, non_redundant_index, index
            )
            if non_redundant:
                non_redundant_index.append(essential_index)
            to_analyze.remove(essential_index)
        non_redundant_bounds = [polytope.bounds[i] for i in non_redundant_index]
        polytope.bounds = non_redundant_bounds
        return polytope

    def _preprocess(self, polytope):
        """
        maximize x_0
        subject to:
            Ax + 1x0 <= b
            x_0 <= 1

        x_0 is a new variable
        Ax <= b is the polytope
        """

        variables = list(polytope.variables)

        obj = [0] * len(variables) + [1]
        A = []
        b = []
        for bound in polytope.bounds:
            a = [0] * len(variables) + [1]
            for var_name in bound.coefficients:
                var_index = variables.index(var_name)
                a[var_index] = bound.coefficients[var_name]
            A.append(a)
            b.append(bound.constant)

        # x_0 <= 1
        A.append([0] * len(variables) + [1])
        b.append(1)

        optimal_value, optimal_solution = self._lp(A, b, obj, "maximize")

        # remove x_0
        optimal_solution = optimal_solution[:-1]

        if optimal_value > 0:
            # polytope dimension = len(variables)
            return polytope, optimal_solution
        elif optimal_value < 0:
            # polytope empty
            return None, []
        else:
            # polytope neither full-dimensional nor empty
            # TODO ?
            return polytope, optimal_solution

    def _clarkson(self, polytope, internal_point, non_redundant_index, index_to_check):
        """
        maximize A_k*x
        subject to:
            A_i*x <= b_i        for all i in I - k
            A_k*x <= b_k +1

        non-redundant if optimal solution > b_k
        """
        variables = list(polytope.variables)
        obj = []
        A = []
        b = []
        b_k = None

        for i, bound in enumerate(polytope.bounds):
            if i == index_to_check or i in non_redundant_index:
                a = [0] * len(variables)
                for var_name in bound.coefficients:
                    var_index = variables.index(var_name)
                    a[var_index] = bound.coefficients[var_name]
                A.append(a)
                b_i = bound.constant
                if i == index_to_check:
                    b_k = b_i
                    b_i += 1
                    obj = [1 * v for v in a]
                b.append(b_i)
        assert b_k is not None

        optimal_value, optimal_solution = self._lp(A, b, obj, "maximize")

        non_redundant = optimal_value > b_k

        if non_redundant:
            return True, self._ray_shoot(
                polytope, internal_point, optimal_solution, index_to_check
            )
        else:
            return False, index_to_check

    def _get_truth_values(self, polytope, point):
        values = []
        variables = list(polytope.variables)

        assert len(point) == len(variables)

        for index, bound in enumerate(polytope.bounds):
            coefficients = [0] * len(variables)
            for var_name in bound.coefficients:
                var_index = variables.index(var_name)
                coefficients[var_index] = bound.coefficients[var_name]
            polynomial = [point[i] * coefficients[i] for i in range(len(point))]
            truth_value = sum(polynomial) <= bound.constant
            values.append(truth_value)
        return values

    def _ray_shoot(self, polytope, start_point, end_point, index):
        values = self._get_truth_values(polytope, end_point)
        others = values[:index] + values[index + 1:]

        # if at the end point (optimal) there is only one inequality falsified
        # then return that particular inequality (index)
        if min(others) == max(others):
            return index
        try:
            return self._ray_shoot_iter(polytope, start_point, end_point)
        except RecursionError:
            print("RECURSION")
            return index

    def _ray_shoot_iter(self, polytope, start_point, end_point):
        # start point is inside the polytope so every bound is respected
        # calculate middle point
        assert len(start_point) == len(end_point)
        middle_point = [
            ((end_point[i] + start_point[i]) * Fraction(1, 2))
            for i in range(len(start_point))
        ]

        # check bounds
        intersected = None
        values = self._get_truth_values(polytope, middle_point)

        for i, v in enumerate(values):
            if not v:
                if intersected is None:
                    intersected = i
                else:
                    intersected = -1
                    break

        if intersected is None:
            return self._ray_shoot_iter(polytope, middle_point, end_point)
        elif intersected < 0:
            return self._ray_shoot_iter(polytope, start_point, middle_point)
        else:
            return intersected

    def _lp(self, A, B, obj, type_="maximize"):
        f = NamedTemporaryFile(mode="w+t", dir=("."))

        assert len(A) == len(B)

        variable_names = [("x_{}".format(i)) for i in range(len(A[0]))]

        # needed to retrieve the values
        f.writelines("(set-option :produce-models true)")

        # declare all variables
        for var in variable_names:
            f.writelines("(declare-fun {} () Real)".format(var))

        # add all constraints
        f.writelines("(assert (and")
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            assert len(a) == len(variable_names)
            coeffs = []
            for c in a:
                if c < 0:
                    coeffs += ["(- {})".format(abs(c))]
                else:
                    coeffs += [str(c)]
            assert len(a) == len(coeffs)
            b = str(b) if b >= 0 else "(- {})".format(abs(b))
            monomials = [
                ("(* {} {})".format(coeffs[j], variable_names[j]))
                for j in range(len(a))
            ]
            if len(monomials) > 1:
                constraint = "(<= (+ {}) {})".format(" ".join(monomials), b)
            else:
                constraint = "(<= {} {})".format(monomials[0], b)
            f.writelines(constraint)
        f.writelines("))")

        # add objective
        coeffs = []
        for c in obj:
            if c < 0:
                coeffs += ["(- {})".format(abs(c))]
            else:
                coeffs += [str(c)]
        monomials = [
            ("(* {} {})".format(coeffs[j], variable_names[j])) for j in range(len(obj))
        ]
        if len(monomials) > 1:
            f.writelines("({} (+ {}))".format(type_, " ".join(monomials)))
        else:
            f.writelines("({} {})".format(type_, monomials[0]))

        f.writelines("(check-sat)")
        f.writelines("(get-objectives)")
        f.writelines("(load-objective-model 1)")
        for var in variable_names:
            f.writelines("(get-value ({}))".format(var))
        f.writelines("(exit)")
        f.seek(0)

        # read output
        values = []
        out = NamedTemporaryFile(mode="w+t", dir=("."))
        output = call(["optimathsat", f.name], stdout=out)
        out.seek(0)
        output = out.read()
        for line in output.split("\n"):
            """
            output can have these forms:
                ( (x_N DIGITS) )
                ( (x_N (- DIGITS)) )
                ( (x_N (/ DIGITS DIGITS)) )
                ( (x_N (- (/ DIGITS DIGITS))) )

            regex below is x_N + OR of the four different types
            """
            r = re.search(
                r"\( \(x_(\d+) (?:(\d+)|(?:\(- (\d+)\))|(?:\(\/ (\d+) (\d+)\))|(?:\(- \(\/ (\d+) (\d+)\)\)))\) \)",
                line,
            )
            if r:
                var_index = r.group(1)
                if r.group(2):
                    values.append(Fraction(int(r.group(2))))
                elif r.group(3):
                    values.append(-1 * Fraction(int(r.group(3))))
                elif r.group(4):
                    values.append(Fraction(int(r.group(4)), int(r.group(5))))
                elif r.group(6):
                    values.append(-1 * Fraction(int(r.group(6)), int(r.group(7))))

        assert len(values) == len(variable_names)
        obj_value = sum([(obj[i] * values[i]) for i in range(len(values))])
        return obj_value, values


class HashTable:
    def __init__(self):
        manager = Manager()
        self.table = manager.dict()

    def get(self, key):
        try:
            return self.table.get(key)
        except TypeError as ex:
            print("HashTable error:\n", ex)
            return self.get(key)

    def set(self, key, value):
        self.table[key] = value

    def key(self, polytope, cond_assignment, variables):
        bounds_key = []
        for index, bound in enumerate(polytope.bounds):
            bound_key = []
            for var in variables:
                if var in bound.coefficients:
                    bound_key.append(bound.coefficients[var])
                else:
                    bound_key.append(0)
            bound_key.append(bound.constant)
            bounds_key.append(tuple(bound_key))

        bounds_key = tuple(sorted(bounds_key))

        key = tuple([bounds_key, cond_assignment])
        return key

    def key_2(self, polytope, integrand):
        variables = list(integrand.variables.union(polytope.variables))

        # polytope key
        polytope_key = []
        for index, bound in enumerate(polytope.bounds):
            bound_key = []
            for var in variables:
                if var in bound.coefficients:
                    bound_key.append(bound.coefficients[var])
                else:
                    bound_key.append(0)
            bound_key.append(bound.constant)
            polytope_key.append(tuple(bound_key))

        polytope_key = tuple(sorted(polytope_key))

        # integrand key
        integrand_key = []

        if not isinstance(integrand, Polynomial):
            return integrand
        monomials = integrand.monomials

        for mon in monomials:
            mon_key = [float(mon.coefficient)]
            for var in variables:
                if var in mon.exponents:
                    mon_key.append(float(mon.exponents[var]))
                else:
                    mon_key.append(0)
            integrand_key.append(tuple(mon_key))

        integrand_key = tuple(sorted(integrand_key))

        key = tuple([polytope_key, integrand_key])
        return key
