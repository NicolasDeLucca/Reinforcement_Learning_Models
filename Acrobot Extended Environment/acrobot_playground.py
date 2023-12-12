# -*- coding: utf-8 -*-
"""Acrobot_Playground.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BZk0ONhkkF3xBlTcKHu3MtWGjpEFO380
"""

import numpy as np
import matplotlib.pyplot as plt

from acrobot_domain import AcrobotEnvExtended # Environment
from acrobot_domain import QLearningAgent # Agent
from acrobot_domain import simulate # Simulation
from acrobot_domain import evaluate_policy # Evaluation
from acrobot_domain import get_state # State

"""#### SetUp"""

# Environment Instances
train_env = AcrobotEnvExtended(render_mode='rgb_array')
test_env = AcrobotEnvExtended(render_mode='human')

# Hyperparameters
hyperparameters = [
    {'alpha': 0.001, 'gamma': 0.99, 'epsilon': 0.001},
    {'alpha': 0.01, 'gamma': 0.95, 'epsilon': 0.01},
    {'alpha': 0.1, 'gamma': 0.9, 'epsilon': 0.1},
    {'alpha': 0.2, 'gamma': 0.8, 'epsilon': 0.2}
]

"""#### Utils"""

def plot_optimal_actions(q_learning_agent: QLearningAgent):
    state_space = [
        q_learning_agent.Q.shape[i] for i in range(len(q_learning_agent.Q.shape) - 1)
    ]
    # we create a state grid
    grid = np.meshgrid(*[np.linspace(-1, 1, bin_count) for bin_count in state_space])
    # we get the optimal actions for each state in the grid
    states = np.vstack([grid[i].ravel() for i in range(len(state_space))])
    optimal_actions = [q_learning_agent.select_action(q_learning_agent.discretize_state(state)) for state in states]
    # we create a graph with arrows that represent the actions in each state
    fig, ax = plt.subplots()
    ax.quiver(states[:, 0], states[:, 1], np.cos(optimal_actions), np.sin(optimal_actions), angles='xy', scale_units='xy', scale=0.1)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('Theta1')
    ax.set_ylabel('Theta2')
    plt.title('Optimal Policy')
    plt.show()

"""#### Analysis"""

num_episodes = 50
best_q_learning_agent = None
best_reward = float('-inf')

for i, params in enumerate(hyperparameters, start=1):
    # Training
    q_learning_agent = QLearningAgent(train_env, **params)
    q_learning_agent.train(num_episodes)
    # Evaluate rewards
    reward = evaluate_policy(num_episodes, test_env, q_learning_agent)
    print(f"\nHyperparameters: {params}\n Policy Evaluation Reward: {reward}\n Optimal Actions:\n")
    # Plot optimal actions
    plot_optimal_actions(q_learning_agent)
    # Update best agent if current agent has higher reward
    if reward > best_reward:
        best_reward = reward
        best_q_learning_agent = q_learning_agent


# Simulate a single episode with the best trained agent
print(f"Best Agent Simulation:\n")
simulate(test_env, best_q_learning_agent)
best_q_learning_agent.save()