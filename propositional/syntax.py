class syntax:
    memory = "mem"
    definition = "define"
    negation = "not"
    conjunction = "and"
    disjunction = "or"
    implication = "if"
    bicondition = "iff"

    def __init__(self,
                 vocab,
                 sentinel="(",
                 terminal=")",
                 separator=" "):
        self.sentinel = sentinel
        self.terminal = terminal
        self.separator = separator
        self.vocab = vocab
        self.punct = [sentinel, terminal, separator]


    def is_token(self, exp):
        return type(exp) == str


    def is_primitive(self, exp):
        if self.is_token(exp):
            return exp in self.vocab
        return False


    def is_variable(self, exp):
        if self.is_token(exp):
            return all(x not in exp for x in self.punct)
        return False


    def is_memory(self, exp):
        if self.is_token(exp):
            return exp.lower() == self.memory
        return False


    def is_definition(self, exp):
        return self.operator(exp) == self.definition


    def parse(self, exp):
        tokens = exp.replace(self.sentinel, f" {self.sentinel} ").replace(self.terminal, f" {self.terminal} ").replace(self.separator, " ").split()

        parsed = []
        stack = [parsed]
        for i, token in enumerate(tokens):
            if i == len(tokens) - 1:
                assert token == self.terminal, "Check your parentheses"
            if token == self.sentinel:
                stack[-1].append([])
                stack.append(stack[-1][-1])
            elif token == self.terminal:
                stack.pop()
            else:
                stack[-1].append(token)

        return parsed


    def operator(self, exp):
        return exp[0]


    def operands(self, exp):
        return exp[1:]
