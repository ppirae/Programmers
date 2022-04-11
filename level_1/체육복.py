def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)

    for i in r_reserve:
        front = i - 1
        back = i + 1
        if front in r_lost:
            r_lost.remove(front)
        elif back in r_lost:
            r_lost.remove(back)

    return n - len(r_lost)