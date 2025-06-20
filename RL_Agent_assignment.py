import numpy as np
import random

# Environment setup
road_length = 5  # Positions: 0 (start) to 4 (goal)
actions = ["left", "right"]

# Q-table (state x action)
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
episodes = 1000  # Training episodes
learning_rate = 0.8  # How fast the agent learns
gamma = 0.9  # Discount factor for future rewards
epsilon = 0.3  # Exploration rate (30% random actions)

# Training loop
for episode in range(episodes):
    state = 0  # Start at position 0

    while state != 4:  # Goal is position 4
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)  # Explore (random action)
        else:
            action = np.argmax(Q[state])  # Exploit (best known action)

        # Take action and get new state
        if action == 0:  # Move left
            new_state = max(0, state - 1)
        else:  # Move right
            new_state = min(4, state + 1)

        # Reward: +1 if reached goal, else 0
        reward = 1 if new_state == 4 else 0

        # Q-learning update rule
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma * np.max(Q[new_state]) - Q[state, action]
        )

        # Move to new state
        state = new_state

# Display learned Q-table
print("Learned Q-table:")
print(Q)

# Test the trained agent
state = 0
steps = 0
path = []
print("\nAgent's path to cross the road:")
while state != 4:
    action = np.argmax(Q[state])  # Choose best action
    if action == 0:
        state = max(0, state - 1)
        path.append("left")
    else:
        state = min(4, state + 1)
        path.append("right")
    steps += 1
    print(f"Step {steps}: Move {actions[action]} → Position {state}")

print(f"\nFinal path: {' → '.join(path)}")
print(f"Goal reached in {steps} steps!")
