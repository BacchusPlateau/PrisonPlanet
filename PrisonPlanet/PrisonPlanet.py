from player import Player
import world
import collections    #Python 3 import directive



def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

def choose_action(room, player):
    action = None
    print(" ")

    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)

        if action:
            action()
        else:
            print("Invalid action.")

def get_available_actions(room, player):
    actions = collections.OrderedDict()
    print("Choose an Action: ")
    
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y - 1):
            action_adder(actions, 'w', player.move_west, "Go west")
    
    if player.hp < player.MAX_HITPOINTS:
        action_adder(actions, 'h', player.heal, "Heal")

    action_adder(actions, 'q', player.quit, "Quit")

    return actions

def get_player_command():
    return input('Action: ').lower()

def play():
    print("Escape the Prison Planet!")

    world.parse_world_dsl()
    player = Player()

    while not player.QUIT_ACTION and player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("All grows dark as your eyes close and the breath leaves your body.")
                
play()