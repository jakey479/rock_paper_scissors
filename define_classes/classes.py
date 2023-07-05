import random
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
sys.path.append(ROOT_DIR)

from rock_paper_scissors.helper_functions import helpers


class Player:
    """
    a constructor is initialized to set the class objects state upon instantiation.
    """
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.their_last_move = None
        self.my_last_move = None

    # the learn method assigns the value of self.their_last_move and self.my_last_move so that the player
    # class is able performs operations based on the value of those variables. The learn method must be called
    # at the point where the values for move are established
    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.their_last_move = their_move


class RandomPlayer(Player):
    def move(self):
        move = random.choice(self.moves)
        return move


class HumanPlayer(Player):
    def move(self):
        valid_move = False
        while not valid_move:
            move = input('\nPlay rock, paper, or scissors: ').lower()
            if move not in ['rock', 'paper', 'scissors']:
                continue
            return move


class ReflectPlayer(Player):
    def move(self):
        return random.choice(self.moves) if not self.their_last_move else self.their_last_move


class CyclePlayer(Player):
    def move(self):
        if not self.my_last_move or self.my_last_move == 'paper':
            return 'rock'
        elif self.my_last_move == 'rock':
            return 'scissors'
        else:
            return 'paper'


class Game:
    """
    on instantiation, the Game class requires the value of the first player.
    """
    def __init__(self, p1):
        self.p1 = p1
        self.p2 = None
        self.p1_score = 0
        self.p2_score = 0
        self.rounds_to_play = 0

    def select_opponent(self):
        """
        when this method is called the value of p2 for the game class is determined based on the user input.
        Depending on the user input, a corresponding player class object is created and assigned to the
        value of p2
        :return:
        """
        is_valid_input = False
        while not is_valid_input:
            opponent = input('''Opponents are:
            
reflect player
cycle player
random player
            
Who would you like to play against? ''').lower()
            if opponent == 'reflect player':
                self.p2 = ReflectPlayer()
                break
            if opponent == 'cycle player':
                self.p2 = CyclePlayer()
                break
            if opponent == 'random player':
                self.p2 = RandomPlayer()
                break
            print('Please choose a valid opponent')

    def return_rounds_to_play(self):
        valid_input = False
        while not valid_input:
            rounds_to_play = input('\nhow many rounds would you like to play? ')
            if rounds_to_play.isdigit():
                self.rounds_to_play = int(rounds_to_play)
                break
            continue

    def play_round(self):
        # Within this method is where the values for player and opponent move are established and so in
        # this method is where the player method learn() must be called and passed the values of their_move,
        # my_move
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        return move1, move2

    def score_round(self):
        p1_results, p2_results = self.play_round()
        winner = helpers.winner_is(p1_results, p2_results)
        if winner == 'p1':
            print('\nPlayer one wins!\n')
            self.p1_score += 1
        if winner == 'p2':
            self.p2_score += 1
            print('\nPlayer two wins!\n')
        if winner == 'none':
            print(f'Tie!\n')
        print(f'Score: Player one {self.p1_score}, Player two {self.p2_score}\n')

    def play_game(self):
        print('\nGame start\n')
        for match in range(self.rounds_to_play):
            print(f"Round {match}:")
            self.score_round()
        if self.p1_score > self.p2_score:
            print(f'The winner is: Player 1\n')
        elif self.p1_score < self.p2_score:
            print(f'The winner is: Player 2\n')
        else:
            print('Tie game!\n')
        print("Thanks for playing!")
