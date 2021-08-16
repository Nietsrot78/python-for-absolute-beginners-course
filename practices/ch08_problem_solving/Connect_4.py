# Rules of the game
# Set symbols --> assign to player?
# Find winner
# Announce winner

def main():
    welcome_screen()
    create_board()
    set_players()

def welcome_screen():
    print()
    print('Velkommen til "4-på-rad"')
    print('Laget av Torstein')
    print()

def create_board():
    # Create the board
    board = [
        [None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, ],
        [None, None, None, None, None, None, None, ]
    ]

def set_players():
    # Toggle active player
    # Set symbols
    human_player = input('What is your name? ')
    players = [human_player, 'Computer']
    symbols = ['X', 'O']

    set_active_player(players)


def set_active_player(players):
    active_player_index = 0
    player = players[active_player_index]


if __name__ == '__main__':
    main()