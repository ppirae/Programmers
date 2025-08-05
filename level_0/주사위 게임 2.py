def solution(a, b, c):
    answer = 0
    if a!=b and b!=c and a!=c:
        answer = a+b+c
    elif a==b and b!=c and a!=c:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif a==c and b!=c and b!=a:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif b==c and a!=c and a!=b:
        answer = (a+b+c)*(a**2+b**2+c**2)
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    return answer