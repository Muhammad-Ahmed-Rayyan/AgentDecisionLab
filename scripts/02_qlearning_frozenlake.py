"""
Task 5A - Reinforcement Learning: Q-Learning Implementation
Trains a Q-Learning agent on FrozenLake-v1 and compares it against
the random-action baseline (see 01_frozenlake_random_baseline.py).
"""

import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt


def train_q_learning(
    env,
    n_episodes=10000,
    learning_rate=0.1,
    discount_factor=0.99,
    epsilon_start=1.0,
    epsilon_min=0.01,
    epsilon_decay=0.0005,
):
    """
    Train a Q-Learning agent.

    Q-update rule:
        Q(s, a) <- Q(s, a) + lr * (reward + gamma * max(Q(s', :)) - Q(s, a))

    epsilon-greedy exploration: epsilon decays over episodes so the agent
    explores early on and exploits its learned policy later.
    """
    n_states = env.observation_space.n
    n_actions = env.action_space.n
    q_table = np.zeros((n_states, n_actions))

    epsilon = epsilon_start
    rewards_per_episode = np.zeros(n_episodes)

    for episode in range(n_episodes):
        state, info = env.reset()
        done = False
        total_reward = 0

        while not done:
            # epsilon-greedy action selection
            if np.random.random() < epsilon:
                action = env.action_space.sample()  # explore
            else:
                action = np.argmax(q_table[state, :])  # exploit

            next_state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated

            # Q-Learning update (off-policy: uses max over next state's Q-values)
            best_next_action_value = np.max(q_table[next_state, :])
            td_target = reward + discount_factor * best_next_action_value
            td_error = td_target - q_table[state, action]
            q_table[state, action] += learning_rate * td_error

            state = next_state
            total_reward += reward

        # decay epsilon (more exploitation as training progresses)
        epsilon = max(epsilon_min, epsilon - epsilon_decay)
        rewards_per_episode[episode] = total_reward

    return q_table, rewards_per_episode


def evaluate_policy(env, q_table, n_episodes=1000):
    """Evaluate the trained (greedy) policy with no exploration."""
    successes = 0

    for _ in range(n_episodes):
        state, info = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state, :])  # pure exploitation
            state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            if terminated and reward == 1.0:
                successes += 1

    success_rate = (successes / n_episodes) * 100
    print(f"\nTrained agent evaluation over {n_episodes} episodes:")
    print(f"Success rate: {success_rate:.2f}%")
    return success_rate


def plot_training_progress(rewards_per_episode, window=100, save_path="results/q_learning_rewards.png"):
    """Plot a rolling average of reward per episode to show learning progress."""
    rolling_avg = np.convolve(rewards_per_episode, np.ones(window) / window, mode="valid")

    plt.figure(figsize=(10, 5))
    plt.plot(rolling_avg)
    plt.xlabel("Episode")
    plt.ylabel(f"Success rate (rolling avg, window={window})")
    plt.title("Q-Learning Training Progress on FrozenLake-v1")
    plt.grid(True)
    plt.savefig(save_path)
    print(f"\nTraining plot saved to {save_path}")
    plt.show()


def main():
    env = gym.make("FrozenLake-v1", is_slippery=True, render_mode=None)

    print("Training Q-Learning agent...")
    q_table, rewards_per_episode = train_q_learning(env, n_episodes=10000)

    print("\nFinal Q-table:")
    print(q_table)

    evaluate_policy(env, q_table, n_episodes=1000)
    plot_training_progress(rewards_per_episode)

    # Save the Q-table for later use (e.g. testing script, report screenshots)
    np.save("results/q_table.npy", q_table)
    print("\nQ-table saved to results/q_table.npy")

    env.close()


if __name__ == "__main__":
    main()
