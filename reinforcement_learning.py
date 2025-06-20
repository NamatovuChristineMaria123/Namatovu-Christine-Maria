# Reinforcement Learning (RL)
# What is RL?
# Reinforcement Learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward. The agent interacts with the environment, receives feedback in the form of rewards or penalties, and adjusts its actions accordingly.
# Key Concepts:
# 1. Agent: The learner or decision-maker.
# 2. Environment: The context in which the agent operates.
# 3. State: A representation of the current situation of the agent in the environment.
# 4. Action: A decision made by the agent that affects the state of the environment.
# 5. Reward: Feedback from the environment based on the action taken by the agent.
# 6. Policy: A strategy that the agent employs to determine its actions based on the current state.
# 7. Value Function: A function that estimates the expected cumulative reward for a given state or state-action pair.

# Key characteristics of RL:
# No labelled data: Unlike supervised learning, RL does not require labelled data. The agent learns from the consequences of its actions.
# Focus on learning from interaction: The agent learns by interacting with the environment, exploring different actions, and observing the outcomes.
# Involves exploration and exploitation: The agent must balance exploring new actions to discover their effects and exploiting known actions that yield high rewards.
# Working throught through delay rewards: The agent may receive rewards after a series of actions, requiring it to learn to associate actions with long-term outcomes.

# Reinforcment Learning Algorithms:
# 1. Q-Learning: A model-free algorithm that learns the value of actions in a given state, allowing the agent to choose actions that maximize cumulative reward.
# 2. Deep Q-Networks (DQN): An extension of Q-learning that uses deep neural networks to approximate the Q-value function, enabling the agent to handle high-dimensional state spaces.
# 3. Policy Gradient Methods: These methods directly optimize the policy by adjusting the parameters of the policy network based on the received rewards.
# 4. Actor-Critic Methods: These methods combine value-based and policy-based approaches, using an actor to select actions and a critic to evaluate the actions taken.
# 5. Proximal Policy Optimization (PPO): A popular policy gradient method that uses a surrogate objective function to update the policy, ensuring stable and efficient learning.
# 6. Trust Region Policy Optimization (TRPO): A policy optimization method that constrains the policy update to ensure stability and prevent large changes in the policy.
# 7. Monte Carlo Methods: These methods estimate the value of states or actions based on the average rewards received from multiple episodes.

# Q-Learning:
# Environment  (Position, Goal, Reward)

# Action (Move Left, Move Right, Stay)
# State (Current Position)
# Reward (Positive for reaching the goal, Negative for hitting a wall)

#  Create a simple Q-learning agent that learns to navigate a grid environment to reach a goal while avoiding walls.
# # Import necessary libraries
import numpy as np
import random


# Define environment parameters
position = 5  # Initial position of the agent 0 to 4
actions = 2  # 0: Move Left, 1: Move Right

# Initialize Q-table
# Create a Q-table with states (positions) and actions (left/right)
Q = np.zeros((position, actions))

# Define parameters
episodes = 1000  # Number of episodes for training
learning_rate = 0.8  # Learning rate
gamma = 0.9  # Discount factor for future rewards
epislon = 0.3  # Probability of taking a random action (exploration)

# Training loop
for episode in range(episodes):
    # Randomly select an initial state (position)
    state = random.randint(0, position - 1)

# Action selection (Epsilon-greedy policy)
    if random.uniform(0, 1) < epislon:  # Explore with probability epislon
        action = random.randint(0, actions - 1)  # Randomly select an action
    else:  # Move right
        action = np.argmax(Q[state])  # Exploit the best known action

# Take action
    # Simulate environment response (for simplicity, assume moving left or right)
    if action == 0:  # Move Left
        # Ensure the position does not go below 0
        next_state = max(0, state - 1)
    else:  # Move Right
        # Ensure the position does not exceed the maximum
        next_state = min(position - 1, state + 1)

    # Reward structure (for simplicity, assume reaching position 4 is the goal)
    if next_state == position - 1:  # If reached the goal
        reward = 10  # Positive reward for reaching the goal
    else:
        reward = -1  # Negative reward for each step taken

    # Q-learning update
    # Update Q-value using the Q-learning formula
    Q[state, action] += learning_rate * \
        (reward + gamma * np.max(Q[next_state]) - Q[state, action])

    # Transition to the next state
    state = next_state  # Update the current state to the next state

    # Show Learned Q-table
    print("Q-table:")
    print(Q)

    # Test the train agent
    state = 0  # Start from the initial position
    steps = 0  # Initialize step counter
    print("\n Agent path goal:")

    # Agent#s path to the goal
    while state < position - 1:  # While not reached the goal
        action = np.argmax(Q[state])  # Select the best action based on Q-table
        if action == 0:  # Move Left
            # Ensure the position does not go below 0
            next_state = max(0, state - 1)
        else:  # Move Right
            # Ensure the position does not exceed the maximum
            next_state = min(position - 1, state + 1)

        print(
            f"Step {steps}: Position {state} -> Action {action} -> Next Position {next_state}")
        state = next_state  # Update the current state to the next state
        steps += 1  # Increment step counter
    print(f"Reached goal in {steps} steps.")

    # Final Q-table
    print("\nFinal Q-table:")
    print(Q)

    # Assignment One train RL agent to navigate to cross the road with action right, left, right
