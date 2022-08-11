def solution(n):
    def convert(n, base):
        res = ""
        while n > 0:
            if n % base == 0:
                n, mod = divmod(n, base)
                n -= 1
            else:
                n, mod = divmod(n, base)
            res += str(mod)
        return res[::-1]

    ans = convert(n, 3)
    ans = str(ans)
    ans = ans.replace('0', '4')
    return ans