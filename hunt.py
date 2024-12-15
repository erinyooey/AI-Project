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
        best_future = self.best_future_reward(new_state, action)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state, action):
        "Return current Q-value for state and action. If not Q-value exists, return 0"
        # returns 0 if our key (state, action) doesn't exist.
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

    def best_future_reward(self, state, actions):
        """Get best future reward through the highest q value"""
        
        if not actions:
            return 0
        return max(self.get_q_value(state, action) for action in actions)

    def choose_action(self, state, actions, epsilon=True):
        if state is None:
            raise ValueError("State is None in choose_action")

        if not actions:
            return None
        
        if epsilon and random.uniform(0,1) < self.epsilon:
            return random.choice(actions)
        else:
            # choose best action by comparing the q-values
            best_action = max(actions, key=lambda a: self.get_q_value(state, a))
            return best_action

class Game():
    def __init__(self):
        self.positions = [(4, 4), (0,0)] # [AI_positon, User_position]
        # using frozenset in python for storing treasure locations
        self.treasures = frozenset({(0,1), (1,3), (2,4)})
        self.player = 0
        self.winner = None
        self.scores = [0,0] # [AI_Score, User_score]
        self.board = [
        ['-', 'T', '-', 'X', '-'],
        ['-', '-', '-', 'T', '-'],
        ['X', '-', '-', '-', 'T'],
        ['-', '-', '-', 'X', '-'],
        ['-', '-', '-', '-', '-']]

    # get our current state
    def get_state(self):
        return (
            self.positions[0],
            self.positions[1],
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
        
        row, col = self.positions[self.player]
            
        moves = {"UP": (-1, 0), "DOWN": (1,0), "LEFT":(0,-1), "RIGHT": (0,1)}
        dr, dc = moves[action]
        new_row = row + dr
        new_col = col + dc
        
        # access the cell
        cell = self.board[new_row][new_col]
        # if cell is T for treasure, add points
        if cell == 'T':
            self.scores[self.player] += 10
            
            # we can remove the T since we found the treasures
            if (new_row, new_col) in self.treasures:
                self.treasures = self.treasures - {(new_row, new_col)}
            # now update the board to empty
            self.board[new_row][new_col] = '-'
            
        elif cell == 'X':
            # if it's a trap, deduct 5 points
            self.scores[self.player] -= 5
                
        # Update player's position
        self.positions[self.player] = (new_row, new_col)
        
        # Switch player
        self.switch_player()
        
        if len(self.treasures) == 0:
            self.winner = self.player
                
            
    def available_actions(self, state):
        """Returns available actions for the player"""
        ai_pos, user_pos, treasures, player = state
        
        # up, down, left, right
        actions = []

        moves = {
            "UP": (-1,0),
            "DOWN": (1,0),
            "LEFT": (0,-1),
            "RIGHT": (0,1)
        }
        
        if player == 0:
            row, col = ai_pos
        else:
            row, col = user_pos
        # check each possible move
        for action, (dr, dc) in moves.items():
            new_row = row + dr
            new_col = col + dc
            
            # check for boundaries
            if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[0]):
                actions.append(action)
                
        return actions

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
            
            available_actions = game.available_actions(state)
            action = player.choose_action(state, actions=available_actions)
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
                break
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
        print(f"AI player's position: {game.positions[0]} | Your position: {game.positions[1]}\n")
        print("Board:")
        for row in game.board:
            print(" ".join(row))
        print()
        
        # get available actions
        available_actions = game.available_actions(game.get_state())
        print("available actions: ", available_actions)
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
            state = game.get_state()
            actions = ai.choose_action(state, available_actions,epsilon=False)
            print(f"AI chose to move {actions}")
            
        # make move
        game.move(actions)
        
        if game.winner is not None:
            print()
            print("GAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")
            return

if __name__ == "__main__":
    ai = train(10000)
    play(ai)