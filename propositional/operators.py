class operators:
    def __init__(self, true=1, false=0):
        self.true = true
        self.false = false

    def negation(self, x):
        return {
            self.true: self.false,
            self.false: self.true,
        }[x]


    def conjunction(self, x, y):
        return {
            (self.true, self.true): self.true,
            (self.true, self.false): self.false,
            (self.false, self.true): self.false,
            (self.false, self.false): self.false,
        }[tuple([x, y])]


    def disjunction(self, x, y):
        return {
            (self.true, self.true): self.true,
            (self.true, self.false): self.true,
            (self.false, self.true): self.true,
            (self.false, self.false): self.false,
        }[tuple([x, y])]


    def implication(self, x, y):
        return {
            (self.true, self.true): self.true,
            (self.true, self.false): self.false,
            (self.false, self.true): self.true,
            (self.false, self.false): self.true,
        }[tuple([x, y])]


    def bicondition(self, x, y):
        return {
            (self.true, self.true): self.true,
            (self.true, self.false): self.false,
            (self.false, self.true): self.false,
            (self.false, self.false): self.true,
        }[tuple([x, y])]
