import random
import enemies

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

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a high tech prison cell dimly lit by ambient light
        coming from an unknown source.   The room is quite large,
        darkness bordering just out of arm's reach all around you. You can
        move freely in all four cardinal directions from where you are now.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        The stolen spacecraft roars into outer space and to freedom!
        You've escaped from the Prison Planet.
        """

world_dsl = """
|  |VT|  |
|  |EN|  |
|EN|ST|EN|
|  |EN|  |
"""

world_map = []

tile_type_dict = {"VT" : VictoryTile,
                  "EN" : EnemyTile,
                  "ST" : StartTile,
                  "  " : None}

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
            row.append(tile_type(x,y) if tile_type else None)

        world_map.append(row)

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


