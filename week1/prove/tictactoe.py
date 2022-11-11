"""
tictactoe.py

Author: Carter Kearns
Assignment: Week 1 Prove
"""

PLAYER_1 = "X"
PLAYER_2 = "O"


def print_board(b):
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print(f"-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print(f"-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")


def input_move(player, possible_moves):
    """
    Gets a move from user input. Guarantees the returned move is one of <possible_moves>.
    """

    choice = None
    while choice not in possible_moves:
        choice = input(f"{player}'s turn to choose a square (1-9): ").strip()

        if choice not in possible_moves:
            print("Please choose a free square from 1-9.")
    return choice


def take_turn(current_player, board):
    POSSIBLE_MOVES = [move for move in board if move not in [PLAYER_1, PLAYER_2]]
    move_index = int(input_move(current_player, POSSIBLE_MOVES)) - 1
    board[move_index] = current_player


def check_winner(player, b):
    """
    Returns True if <player> won the game by meeting any of the 5 win conditions, False otherwise
    """

    return (
        (b[0] == player and b[1] == player and b[2] == player)
        or (b[3] == player and b[4] == player and b[5] == player)
        or (b[6] == player and b[7] == player and b[8] == player)
        or (b[0] == player and b[4] == player and b[8] == player)
        or (b[2] == player and b[4] == player and b[6] == player)
    )


def check_draw(b):
    """
    Returns True if the game is a draw, False otherwise
    """
    for move in b:
        if move not in [PLAYER_1, PLAYER_2]:
            return False
    return True


def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    game_over_msg = None
    current_player = PLAYER_1

    while not game_over_msg:
        print_board(board)
        print()
        take_turn(current_player, board)
        print()

        if check_winner(current_player, board):
            game_over_msg = f"{current_player} wins!"

        if check_draw(board):
            game_over_msg = "It's a draw!"

        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

    print(game_over_msg)
    print_board(board)


if __name__ == "__main__":
    main()
