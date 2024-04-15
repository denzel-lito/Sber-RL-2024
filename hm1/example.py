import json


def solution(mdp, gamma):
    # Заполняем табличку нулями
    q_table = {
        state: {
            action: 0 for action in actions
        } for state, actions in mdp['transition_probs'].items()
    }
    return q_table


def main():
    # Список словарей содержит данные о каждом МППР, который определяется
    # состояниями, действиями, вероятностями перехода и вознаграждениями.
    with open('mdps.json', "r") as f:
        mdps = json.load(f)
    print(mdps[0])
    # {'transition_probs': {'s0': {'a0': {'s1': 0.84, 's2': 0.16},
    #                              'a1': {'s1': 0.53, 's2': 0.47}},
    #                       's1': {'a0': {'s0': 0.19, 's2': 0.81},
    #                              'a1': {'s0': 0.25, 's2': 0.75}},
    #                       's2': {'a0': {'s0': 0.12, 's1': 0.88},
    #                              'a1': {'s0': 0.65, 's1': 0.35}}},
    # 'reward_function': {'s0': {'a0': {'s1': -0.05811640535549212, 's2': -0.5935041149106424},
    #                            'a1': {'s1': -0.6179274398384225, 's2': -0.4369088027162966}},
    #                     's1': {'a0': {'s0': 0.7274441514167771, 's2': 0.6107444418118435},
    #                            'a1': {'s0': -0.6202851758369194, 's2': 0.9679911637843441}},
    #                     's2': {'a0': {'s0': -0.5921735314515975, 's1': 0.2501293709049084},
    #                            'a1': {'s0': 0.7976150574969298, 's1': 0.9495275614143339}}}}
    Qs = []
    for mdp in mdps:
        Qs.append(solution(mdp, gamma=0.9))
    with open('submit.json', "w") as f:
        json.dump(Qs, f)


if __name__ == '__main__':
    main()