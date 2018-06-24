from player import Player

def get_player_command():
    return input('Action: ').lower()

def play():
    print("Escape the Prison Planet!")
    player = Player()
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
            pretty_print_unordered(player.inventory)
        elif action_input == 'q':     #quit
            break
        else:
            print("Invalid action")

def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))


play()