"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
from define_classes import classes


def main():
    game = classes.Game(classes.HumanPlayer())
    game.select_opponent()
    game.return_rounds_to_play()
    game.play_game()


if __name__ == '__main__':
    main()
