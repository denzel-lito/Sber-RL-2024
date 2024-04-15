import json
import numpy as np
import gymnasium as gym


def initialize_q_table(observation_space_n, action_space_n):
    Q = np.zeros([observation_space_n, action_space_n])
    return Q


def select_action_eps_greedy(Q, state, epsilon):
    # TODO
    action = ...
    return action


def update_Q_SARSA(Q, s, a, r, next_s, next_a, alpha, gamma):
    # TODO
    ...


def update_Q(Q, s, a, r, next_s, next_a, alpha, gamma):
    # TODO
    ...


def learn(method):
    env = gym.make('CliffWalking-v0')
    # определяем память, в которой будет храниться Q(s,a)
    Q = initialize_q_table(env.observation_space.n, env.action_space.n)

    # гиперпараметры алгоритма (не меняйте параметры)
    alpha = 0.1
    gamma = 0.9
    max_epsilon = 0.2
    episodes_number = 10000

    for episode in range(1, episodes_number + 1):
        epsilon = max_epsilon * (episodes_number - episode) / (episodes_number - 1)
        s, _ = env.reset()

        r, episode_reward = 0, 0
        done = False
        a = select_action_eps_greedy(Q, s, epsilon)
        while not done:
            next_s, r, terminated, truncated, info = env.step(a)
            done = terminated or truncated

            next_a = select_action_eps_greedy(Q, next_s, epsilon)
            ##############################
            # Обновите Q функцию в соответствии с алгоритмом SARSA или Q обучение
            if method == 'SARSA':
                update_Q_SARSA(Q, s, a, r, next_s, next_a, alpha, gamma)
            else:
                update_Q(Q, s, a, r, next_s, next_a, alpha, gamma)
            # Note: считаем Q функцию для терминальных состояний всегда равной 0
            ##############################

            s = next_s
            a = next_a
            episode_reward += r
        if episode % 100 == 0:
            print(f"Episode: {episode}, Reward: {episode_reward}, Eps: {epsilon}")
    return Q

def main():
    Q = learn('Q')
    SARSA = learn('SARSA')
    # сохранение
    env = gym.make('CliffWalking-v0')
    states = env.observation_space.n
    actions = env.action_space.n
    Q_dict = {}
    pi_Q = {} 
    SARSA_dict = {}
    pi_SARSA = {}
    for s in range(states):
        Q_dict[s] = {}
        SARSA_dict[s] = {}

        # Задайте жадную стратегию !!!!!!!!
        # TODO
        pi_SARSA[s] = 0
        pi_Q[s] = 0

        for a in range(actions):
            Q_dict[s][a] = Q[s, a]
            SARSA_dict[s][a] = SARSA[s, a]

    with open('submit.json', "w") as f:
        json.dump([Q_dict, pi_Q, SARSA_dict, pi_SARSA], f)



if __name__ == '__main__':
    main()
