class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw weapon objects")

    def __str__(self):
        return self.name


class Crysknife(Weapon):
    def __init__(self):
        self.name = "Crysknife"
        self.description = "A deadly blade carved from a tooth of Shai Hulud."
        self.damage = 5

class Lasegun(Weapon):
    def __init__(self):
        self.name = "Lasegun"
        self.description = "Now this is what I call a weapon, " \
            "just point and watch the fun."
        self.damage = 20

class Stunner(Weapon):
    def __init__(self):
        self.name = "Stunner"
        self.description = "A short staff with a cone projector at one end. " \
            "Causes painful blisters when in range."
        self.damage = 10
