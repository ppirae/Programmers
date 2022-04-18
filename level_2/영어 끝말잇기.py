global ch
def solution(n, words):
    ch = []
    res = []

    def is_pass(word):
        if ch == []:
            ch.append(word)
            return True
        else:
            if word not in ch:
                if ch[-1][-1] == word[0]:
                    ch.append(word)
                    return True
                return False
            return False

    cnt = 1
    rotate = 1
    for word in words:
        if is_pass(word) == True:
            cnt += 1
            if cnt > n:
                cnt = 1
                rotate += 1
        else:
            res.append(cnt)
            res.append(rotate)
            break

    if res == []:
        res = [0, 0]

    return res