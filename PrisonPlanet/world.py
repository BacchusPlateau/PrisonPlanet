class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead.")

class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a high tech prison cell dimly lit by ambient light
        coming from an unknown source.   The room is quite large,
        darkness bordering just out of arm's reach all around you. You can
        move freely in all four cardinal directions from where you are now.
        """

class BoringTile(MapTile):
    def intro_text(self):
        return """
        There isn't anything worth noting about this part of the prison.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        The stolen spacecraft roars into outer space and freedom!
        You've escaped from the Prison Planet.
        """

world_map = [
    [None, VictoryTile(1,0), None],
    [None, BoringTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2), BoringTile(2,2)],
    [None, BoringTile(1,3), None]
]

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


