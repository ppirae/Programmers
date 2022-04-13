def solution(numbers, hand):
    loc = {1: (0, 0),
           2: (0, 1),
           3: (0, 2),
           4: (1, 0),
           5: (1, 1),
           6: (1, 2),
           7: (2, 0),
           8: (2, 1),
           9: (2, 2),
           "*": (3, 0),
           0: (3, 1),
           "#": (3, 2)}

    hand_loc = [(3, 0), (3, 2)]
    result = ''
    for num in numbers:
        if num in [1, 4, 7]:
            result += "L"
            hand_loc[0] = loc[num]
        elif num in [3, 6, 9]:
            result += "R"
            hand_loc[1] = loc[num]
        else:
            r_dis = abs(hand_loc[1][0] - loc[num][0]) + abs(hand_loc[1][1] - loc[num][1])
            l_dis = abs(hand_loc[0][0] - loc[num][0]) + abs(hand_loc[0][1] - loc[num][1])
            if l_dis > r_dis:
                result += "R"
                hand_loc[1] = loc[num]
            elif r_dis > l_dis:
                result += "L"
                hand_loc[0] = loc[num]
            else:
                if hand == "right":
                    result += "R"
                    hand_loc[1] = loc[num]
                else:
                    result += "L"
                    hand_loc[0] = loc[num]
    return result