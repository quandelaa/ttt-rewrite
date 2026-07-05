from board_utils import Utils
from random import random, choice

class Bot:
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):
        old_q_value = self.get_q_value(old_state, action)
        best_reward = self.best_future_reward(new_state)

        self.update_q_value(old_state, action, old_q_value, reward, best_reward)

    def get_q_value(self, state, action):
        q_value = self.q.get((tuple(state), action))

        return q_value if q_value is not None else 0

    def update_q_value(self, state, action, old_q, reward, best_reward):
        self.q[(tuple(state), action)] = old_q + self.alpha * ((reward + best_reward) - old_q)

    def best_future_reward(self, state):
        available_actions = Utils.available_actions(state)

        if len(available_actions) < 1:
            return 0

        best_reward = float("-inf")

        for action in available_actions:
            q_value = self.q.get((tuple(state), action), 0)
            best_reward = q_value if q_value> best_reward else best_reward

        return best_reward

    def choose_action(self, state, epsilon: bool = False):
        q_state = Utils.flatten(state)
        available_actions = Utils.available_actions(state)

        best_reward = float("-inf")
        best_action = None

        for action in available_actions:
            q_value = self.q.get((tuple(q_state), action), 0)

            if q_value > best_reward:
                best_reward = q_value
                best_action = action
        
        if epsilon is False:
            return best_action

        if self.epsilon > random():
            return tuple(choice(available_actions))
        else:
            return best_action
