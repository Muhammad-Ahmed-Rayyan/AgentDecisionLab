"""
Task 5B - OpenAI Gym/Gymnasium Exploration
Random-action baseline on FrozenLake-v1.

Purpose: understand observation/action spaces, reset()/step() mechanics,
and establish a baseline success rate before introducing Q-Learning.
"""

import gymnasium as gym
import numpy as np


def explore_environment(env):
    """Print out the environment's observation and action spaces."""
    print("Observation space:", env.observation_space)  # Discrete(16) -> 4x4 grid, 16 possible states
    print("Action space:", env.action_space)             # Discrete(4)  -> Left, Down, Right, Up


def run_single_episode(env, verbose=True):
    """Run one episode with random actions to inspect reset()/step() mechanics."""
    state, info = env.reset(seed=42)
    if verbose:
        print("\nInitial state:", state, "| info:", info)

    done = False
    step_count = 0
    total_reward = 0

    while not done:
        action = env.action_space.sample()  # random action - no learning yet
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward
        step_count += 1
        if verbose:
            print(f"Step {step_count}: action={action}, next_state={next_state}, "
                  f"reward={reward}, terminated={terminated}, truncated={truncated}")

    if verbose:
        print(f"\nEpisode finished after {step_count} steps. Total reward: {total_reward}")

    return total_reward, step_count


def run_random_baseline(env, n_episodes=1000):
    """Run many episodes with random actions and report the success rate."""
    rewards = []

    for _ in range(n_episodes):
        state, info = env.reset()
        done = False
        ep_reward = 0
        while not done:
            action = env.action_space.sample()
            state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            ep_reward += reward
        rewards.append(ep_reward)

    success_rate = np.mean(rewards) * 100
    print(f"\nRandom baseline over {n_episodes} episodes:")
    print(f"Success rate: {success_rate:.2f}%")
    return success_rate


def main():
    env = gym.make("FrozenLake-v1", is_slippery=True, render_mode=None)

    explore_environment(env)
    run_single_episode(env, verbose=True)
    run_random_baseline(env, n_episodes=1000)

    env.close()


if __name__ == "__main__":
    main()
