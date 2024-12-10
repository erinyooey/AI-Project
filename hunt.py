# https://towardsdatascience.com/introduction-to-q-learning-88d1c4f2b49c

import pygame

class AI():
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon
    
    # following hw5's approach for Q-learning
    def update(self, old_state, action, new_state, reward):
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state, action):
        pass
    
    def update_q_value(self, state, action, old_q, reward, future_rewards):
        pass
    
    def best_future_reward(self, state):
        pass
    
    def choose_action(self, state, epsilon=True):
        if state is None:
            raise ValueError("State is None in choose_action")

class Game():
    def __init__(self):
        self.player = 0
        self.winner = None
        self.board = [
        ['-', 'T', '-', 'X', '-'],
        ['-', '-', '-', 'T', '-'],
        ['X', '-', '-', '-', 'T'],
        ['-', '-', '-', 'X', '-'],
        ['-', '-', '-', '-', '-']]
        self.reward = [
            [0, 10, 0, -5, 0],
            [0, 0, 0, 10, 0],
            [-5, 0, 0, 0, 10],
            [0, 0, 0, -5, 0],
            [0, 0, 0, 0, 0]]
        
    def other_player(self, player):
        """Determines who the opponent of a given player is"""
        return 0 if player == 1 else 1
    
    def switch_player(self):
        """Changes current player to opposing player"""
        self.player = self.other_player(self.player)
        
    def move(self):
        """Performs an arrow key action on the current state & switches current player to opposing player"""

def train(n):
    """Return trained AI player"""
    player = Game()
    for i in range(n):
        print(f"Playing training game {i+1}")
        
        game = AI()
        
        # stop if all treasure is collected
        
        
        
        # make move
        
        # new state after performing an action

def play(ai):
    """Game starts with trained AI player"""
    
    # check for winner
    

def main():
    ai = train(10000)
    play(ai)
    # initialize screen
    pygame.init()

main()