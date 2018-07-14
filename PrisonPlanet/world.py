import random
import enemies
import npc

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead.")

    def modify_player(self, player):
        pass

class BoringTile(MapTile):
    def intro_text(self):
        return """
        There isn't anything worth noting about this part of the prison.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):

        r = random.random()

        if r < 0.50:
            self.enemy = enemies.Guard()
            self.alive_text = "A brutish prison guard comes out of nowhere!"
            self.dead_text = "The guard looks better face down on the ground now."
        elif r < 0.80:
            self.enemy = enemies.BatColony()
            self.alive_text = "A swarm of bats streams from the broken vent overhead!"
            self.dead_text = "That was enough screeching to drive one batty."
        elif r < 0.95:
            self.enemy = enemies.Thug()
            self.alive_text = "A fellow prisoner decides to take out the competition - YOU!"
            self.dead_text = "The lifeless body of your attacker ceases to move on the ground."
        else:
            self.enemy = enemies.RobotEnforcer()
            self.alive_text = "Holy Snikees!  It's a Robot Enforcer...egad!!!"
            self.dead_text = "Smelly nuts and bolts roll around where the metal monster of mayhem once stood."

        super(EnemyTile, self).__init__(x, y)

    def intro_text(self):
       if self.enemy.is_alive():
            text = self.alive_text 
       else: 
            text = self.dead_text
       return text
        
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, player.hp))

class FindCreditsTile(MapTile):
    def __init__(self, x, y):
        self.credits = random.randint(1, 50)
        self.credits_claimed = False
        super().__init__(x,y)

    def modify_player(self, player):
        if not self.credits_claimed:
            self.credits_claimed = True
            player.credits = player.credits + self.credits
            print("+{} credits added.".format(self.credits))

    def intro_text(self):
        if self.credits_claimed:
            return """
            Isn't this where you found those credits?  Too bad there aren't any more.
            """
        else:
            return """
            Your lucky day!  Someone dropped a few credit chips.  You pick them up.
            """

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a high tech prison cell dimly lit by ambient light
        coming from an unknown source.   The room is quite large,
        darkness bordering just out of arm's reach all around you. You can
        move freely in all four cardinal directions from where you are now.
        """

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x,y)

    def intro_text(self):
        return """
        A seasoned lifer prisoner quats in the shadows under a stairwell
        shuffling credit chips like a casino gambler.  He looks like would
        enjoy a bit of trade.
        """

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy or (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's what's available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's what's available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
               print("Invalid choice.")

    def swap(self, seller, buyer, item):
        if item.value > buyer.credits:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.credits = seller.credits + item.value
        buyer.credits = buyer.credits - item.value
        print("Trade completed")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Credits".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice")

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        The stolen spacecraft roars into outer space and to freedom!
        You've escaped from the Prison Planet.
        """

start_title_location = None

world_dsl = """
|EN|EN|VT|EN|EN|
|  |  |  |  |EN|  
|EN|FC|EN|  |TT|
|  |EN|ST|FC|EN|
|FC|  |EN|  |FC|
"""

world_map = []

tile_type_dict = {"VT" : VictoryTile,
                  "EN" : EnemyTile,
                  "FC" : FindCreditsTile,
                  "ST" : StartTile,
                  "TT" : TraderTile,
                  "  " : BoringTile}

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False

    if dsl.count("|VT|") != 1:
        return False

    lines = dsl.splitlines()            # count the number of lines in a string
    lines = [l for l in lines if l]     # "if l" is shorthand for "if l != ''"
    pipe_counts = [line.count("|") for line in lines]

    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

def parse_world_dsl():
    if not is_dsl_valid(world_dsl): #curious why the author didn't use global scope for accessing world_dsl - he did it in this function then passed it by ref to another.
        raise SyntaxError("DSL is invalid.")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]

        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_title_location
                start_title_location = x, y
            row.append(tile_type(x,y) if tile_type else None)

        world_map.append(row)

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


