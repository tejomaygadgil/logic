import itertools
import session

class satisfier:
    def __init__(self, operators, syntax):
        self.ops = operators
        self.syn = syntax


    def get_constants(self, exp):
        def recurse(exp):
            if self.syn.is_variable(exp):
                return set([exp])
            else:
                return set.union(*list(map(recurse, self.syn.operands(exp))))

        return recurse(self.syn.parse(exp)[0])


    def gen_worlds(self, constants):
        truth_assignments = map(lambda x: [(x, v) for v in self.syn.vocab], constants)
        worlds = itertools.product(*truth_assignments)

        return list(worlds)


    def satisfies(self, world, exp):
        s = session.session(operators=self.ops, syntax=self.syn)

        for k, v in world:
            s.eval(f"(define {k} {v})")

        return s.eval(exp) == self.ops.true


    def model_check(self, exp, verbose=False):
        constants = self.get_constants(exp)
        worlds = self.gen_worlds(constants)

        satisfiers = {"yes": [], "no": []}
        for world in worlds:
            if self.satisfies(world, exp):
                satisfiers["yes"].append(world)
            else:
                satisfiers["no"].append(world)

        property = None
        if satisfiers["yes"]:
            if satisfiers["no"]:
                property = "contingent"
            else:
                property = "valid"
        else:
            property = "unsatisfiable"

        if verbose:
            print(f"Expression is {property}: {exp}")
            if satisfiers["yes"]:
                print("Satisfying worlds")
                for world in satisfiers["yes"]:
                    print(world)
            if satisfiers["no"]:
                print("Unsatisfying worlds")
                for world in satisfiers["no"]:
                    print(world)

        return property, satisfiers


    def driver_loop(self):
        while True:
            exp = input("> ")
            try:
                self.model_check(exp, verbose=True)
            except AssertionError as e:
                print(e)
