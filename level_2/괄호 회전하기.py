def solution(s):
    from collections import deque

    s = deque(s)

    def check(li):
        stk = []
        if len(li) <= 1:
            return False
        for i in li:
            if stk == []:
                if i == "]" or i == "}" or i == ")":
                    return False
                else:
                    stk.append(i)
            else:
                temp = stk[-1]
                if temp == "[" and i == "]":
                    stk.pop()
                elif temp == "(" and i == ")":
                    stk.pop()
                elif temp == "{" and i == "}":
                    stk.pop()
                else:
                    if i == "{" or i == "(" or i == "[":
                        stk.append(i)
                    else:
                        return False
        if stk == []:
            return True

    cnt = 0
    for i in range(len(s)):
        if check(s):
            cnt += 1
        temp = s.popleft()
        s.append(temp)

    return cnt