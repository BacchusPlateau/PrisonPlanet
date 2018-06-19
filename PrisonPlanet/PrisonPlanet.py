class Weapon:    #note that a superclass has to be above the subclass...ugh!
    def __str__(self):
        return self.name

class Crysknife(Weapon):
    def __init__(self):
        self.name = "Crysknife"
        self.description = "A deadly blade carved from a tooth of Shai Hulud."
        self.damage = 5

class Lasgun(Weapon):
    def __init__(self):
        self.name = "Lasgun"
        self.description = "Now this is what I call a weapon, " \
            "just point and watch the fun."
        self.damage = 20

class StunBaton(Weapon):
    def __init__(self):
        self.name = "Stun Baton"
        self.description = "A short staff with a cone projector at one end. " \
            "Causes painful blisters when in range."
        self.damage = 10

def get_player_command():
    return input('Action: ').lower()

def play():
    inventory = [Crysknife(),'Gold(5)','Crusty Bread']
    print("Escape the Prison Planet!")
    while True:
        action_input = get_player_command()
        if action_input == 'n':
            print("Go North")
        elif action_input == 's':
            print("Go South")
        elif action_input == 'e':
            print("Go East")
        elif action_input == 'w':
            print("Go West")
        elif action_input == 'i':
            print("Inventory: ")
            pretty_print_unordered(inventory)
        elif action_input == 'q':     #quit
            break
        else:
            print("Invalid action")

def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))


play()