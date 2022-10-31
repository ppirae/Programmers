def solution(price):
    ans = 0
    if 100000 > price:
        ans = price
    elif 100000 <= price < 300000:
        ans = 0.95 * price
    elif 300000 <= price < 500000:
        ans = 0.9 * price
    else:
        ans = 0.8 * price
    return int(ans)