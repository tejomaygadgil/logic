import readline

class session:
    def __init__(self, operators, syntax):
        self.operators = operators
        self.syntax = syntax
        self.memory = {}


    def define(self, x, v):
        assert self.syntax.is_token(x), f"Cannot assign complex expression -- {x}"
        assert not self.syntax.is_primitive(x), f"Cannot assign primitive -- {x}"
        self.memory[x] = self._eval(v)

        return "ok"


    def eval(self, exp):
        exp = exp.replace("0", self.operators.false).replace("1", self.operators.true)
        parsed = self.syntax.parse(exp)
        values = map(self._eval, parsed)
        return " ".join(values)


    def _eval(self, exp):
        if self.syntax.is_memory(exp):
            return self.memory
        elif self.syntax.is_primitive(exp):
            return exp
        elif self.syntax.is_variable(exp):
            try:
                return self.memory[exp]
            except KeyError as e:
                raise AssertionError(f"Unbound variable -- {exp}")
        elif self.syntax.is_definition(exp):
            return self.define(*self.syntax.operands(exp))
        else:
            try:
                return {
                    self.syntax.negation: self.operators.negation,
                    self.syntax.conjunction: self.operators.conjunction,
                    self.syntax.disjunction: self.operators.disjunction,
                    self.syntax.implication: self.operators.implication,
                    self.syntax.bicondition: self.operators.bicondition,
                }[self.syntax.operator(exp)](*map(self._eval, self.syntax.operands(exp)))
            except KeyError as e:
                raise AssertionError(f"Unbound operator -- {self.syntax.operator(exp)}")


    def driver_loop(self):
        while True:
            exp = input("> ")
            try:
                value = self.eval(exp)
                print(value)

            except AssertionError as e:
                print(e)
