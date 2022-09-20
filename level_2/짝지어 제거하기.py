def solution(s):
    def check(stk, ch):
        if stk == []:
            stk.append(ch)
        elif stk[-1] == ch:
            stk.pop()
        elif stk[-1] != ch:
            stk.append(ch)
        return stk

    s = list(s)
    stk = []

    for i in s:
        stk = check(stk, i)

    ans = 0
    if stk == []:
        ans = 1
    else:
        ans = 0
    return ans