class ClassicalMechanics:
    def __init__(self, speed):
        self.name = "ClassicalMechanics"
        self.velocity = speed

    def __call__(self, speed):
        return self.velocity + speed

    def __repr__(self):
        return f"Object {self.name}, velocity {self.velocity} c"

    def __str__(self):
        return f"Object {self.name}, velocity {self.velocity} c"


class SpecialTheoryRelativity(ClassicalMechanics):
    def __init__(self, speed):
        self.velocity = speed
        self.name = "SpecialTheoryRelativity"

    def __call__(self, speed):
        if self.velocity < 0.1 and speed < 0.1:
            return self.velocity + speed
        return (self.velocity + speed) / (1 + (self.velocity * speed))