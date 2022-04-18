def solution(d):
    score = [0]
    for i in d:
        if i == "S":
            score[-1] **= 1
            score.append(0)
        elif i == "D":
            score[-1] **= 2
            score.append(0)
        elif i == "T":
            score[-1] **= 3
            score.append(0)
        elif i == "#":
            score[-2] *= -1
        elif i == "*":
            score[-2] *= 2
            if len(score) > 2:
                score[-3] *= 2
        else:
            score[-1] = score[-1] * 10 + int(i)

    return sum(score)