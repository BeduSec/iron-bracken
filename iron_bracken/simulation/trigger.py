class Trigger:
    def __init__(self, condition):
        self.condition = condition

    def check(self, environment):
        return self.condition(environment)
