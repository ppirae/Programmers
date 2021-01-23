def solution(s):
    answer = True
    stack = []
    for ps in s:
        if stack == []:
            if ps == ")":
                return False
            else:
                stack.append(ps)
        else:
            if ps == "(":
                stack.append(ps)
            else:
                stack.pop()

    if stack == []:
        return True
    else:
        return False
