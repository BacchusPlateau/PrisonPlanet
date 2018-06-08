def play():
    print("Escape the Prison Planet!")
    action_input = get_player_command()
    if action_input == 'n':
        print("Go North")
    elif action_input == 's':
        print("Go South")
    elif action_input == 'e':
        print("Go East")
    elif action_input == 'w':
        print("Go West")
    else:
        print("Invalid action")


def get_player_command():
    return input('Action: ').lower()

play()