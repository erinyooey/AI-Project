# https://towardsdatascience.com/introduction-to-q-learning-88d1c4f2b49c
import random

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
        "Return current Q-value for state and action. If not Q-value exists, return 0"
        if (state, action) in self.q:
            return self.q.get((state, action),0)
        else:
            return 0
    
    def update_q_value(self, state, action, old_q, reward, future_rewards):
        """Uses best future rewards value and Q-value to update the Q-value"""
        # following the formula
        old_val_estimate = old_q
        new_val_estimate = reward + future_rewards
        
        updated_q = old_val_estimate + self.alpha*(new_val_estimate - old_val_estimate)
        
        self.q[(state, action)] = updated_q
    
    def best_future_reward(self, state):
        pass
    
    def choose_action(self, state, epsilon=True):
        if state is None:
            raise ValueError("State is None in choose_action")

class Game():
    def __init__(self):
        # ai player starts at this position
        self.ai_position = (4,4) 
        # user's position
        self.user_position = (0,0)
        # using frozenset in python for storing treasure locations
        self.treasures = frozenset({(0,1), (1,3), (2,4)})
        self.player = 0
        self.winner = None
        self.board = [
        ['-', 'T', '-', 'X', '-'],
        ['-', '-', '-', 'T', '-'],
        ['X', '-', '-', '-', 'T'],
        ['-', '-', '-', 'X', '-'],
        ['-', '-', '-', '-', '-']]
        
    # get our current state
    def get_state(self):
        return (
            self.ai_position[0],
            self.ai_position[1],
            self.user_position[0],
            self.user_position[1],
            self.treasures,
            self.player
        )
        
    def other_player(self, player):
        """Determines who the opponent of a given player is"""
        return 0 if player == 1 else 1
    
    def switch_player(self):
        """Changes current player to opposing player"""
        self.player = self.other_player(self.player)
        
    def move(self, action):
        """Takes in user's move for the current state & switches current player to opposing player"""
        
    def available_actions(self, state):
        """Returns a set of all the available actions in a state"""
        

def train(n):
    """Return trained AI player"""
    player = AI()
    for i in range(n):
        print(f"Playing training game {i+1}")
        
        game = Game()
        
        # game loop
        while True:
            state = game.get_state()
            if state is None:
                raise ValueError("State is None before calling choose_action.")
            
            action = player.choose_action(state)
            
            # stop if all treasure is collected
            if len(game.treasures) == 0:
                break
            
            # make move
            game.move(action)
            
            # new state after performing an action
            new_state = game.get_state()
            
            # when game is over, update q values with reward
            if game.winner is not None:
                player.update(state, action, new_state, -1)
    print("Done training")
    
    # return trained AI
    return player

def play(ai, human_player=None):
    """Game starts with trained AI player"""
    # Choose human player's order randomly
    if human_player is None:
        human_player = random.randint(0,1)
    
    # Create game
    game = Game()
    
    # Game loop
    while True:
        # Print contents of board
        print()
        print(f"AI player's position: {game.ai_position} | Your position: {game.user_position}\n")
        print("Board:")
        for row in game.board:
            print(" ".join(row))
        print()
        
        
        # get available actions
        available_actions = game.available_actions(game.get_state())
        
        if game.player == human_player:
            print("\nYour Turn\n")
            while True:
                user_move = input("Choose your move ('UP, DOWN, LEFT, RIGHT'): ")
                
                if user_move not in available_actions:
                    break
                print("Invalid move, try again")
        # Have AI make a move
        else:
            print("AI's Turn")
            
            

if __name__ == "__main__":
    ai = train(10000)
    play(ai)