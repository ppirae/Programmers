def solution(s):
    s = s.split(' ')
    res = ""
    for i in s:
        if len(i) > 1:
            res += i[0].upper() + i[1:].lower()
        else:
            if i == " ":
                res += " "
            else:
                res += i.upper()
        res += " "
    return res[:-1]