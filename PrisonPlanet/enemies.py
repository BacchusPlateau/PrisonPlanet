class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create abstract Enemy instances")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class Guard(Enemy):
    def __init__(self):
        self.name = "Guard"
        self.hp = 10
        self.damage = 2

class Thug(Enemy):
    def __init__(self):
        self.name = "Thug"
        self.hp = 30
        self.damage = 10

class BatColony(Enemy):
    def __init__(self):
        self.name = "Bat Colony"
        self.hp = 100
        self.damage = 4


class RobotEnforcer(Enemy):
    def __init__(self):
        self.name = "Robot Enforcer"
        self.hp = 80
        self.damage = 15



