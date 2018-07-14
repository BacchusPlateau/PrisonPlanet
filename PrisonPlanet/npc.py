import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Don't create instance from abstract class NonPlayableCharacter")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.credits = 100
        self.inventory = [items.Manna(), items.Manna(), items.Manna(), items.Medpack(), items.Medpack()]

