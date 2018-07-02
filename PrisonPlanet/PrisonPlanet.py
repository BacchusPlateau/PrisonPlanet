from player import Player
import world

def get_player_command():
    return input('Action: ').lower()

def play():
    print("Escape the Prison Planet!")
    
    player = Player()

    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        action_input = get_player_command()

        if action_input == 'n':
            player.move_north()
        elif action_input == 's':
            player.move_south()
        elif action_input == 'e':
            player.move_east()
        elif action_input == 'w':
            player.move_west()
        elif action_input == 'a':
            player.attack()
        elif action_input == 'i':
            print("Inventory: ")
            pretty_print_unordered(player.inventory)
        elif action_input == 'q':     #quit
            break
        else:
            print("Invalid action")

def pretty_print_unordered(to_print):
    for item in to_print:
      #  print("* " + (item.__str__))
        print(item)

play()