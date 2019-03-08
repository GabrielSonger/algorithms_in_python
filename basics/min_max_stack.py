class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.stack_max = []
        self.stack_min = []

    def push(self, e):
        self.stack.append(e)

        if not self.stack_min or e < self.stack_min[-1]:
            self.stack_min.append(e)
        else:
            self.stack_min.push(self.stack_min[-1])

        if not self.stack_max or e> self.stack_max[-1]:
            self.stack_max.append(e)
        else:
            self.stack_max.append(self.stack_max[-1])

    def pop(self, e):
        if self.stack_max and self.stack_min and self.stack:
            e = self.stack.pop()

            return e
        else:
            print ("stack is empty")

            return

    def min(self):
        return self.stack_min.pop()

    def max(self):
        return self.stack_max.pop()