def solution(number, k):
    a = list(map(int, number))
    stack = []

    for i in a:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    return ''.join(map(str, stack))