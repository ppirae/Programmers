def solution(myString):
    answer = []
    result = []
    answer = sorted(myString.split('x'))
    for i in answer:
        if i!="":
            result.append(i)
    return result


# 더 좋은 코드
def solution(myString):
    return sorted(filter(lambda x: x!="", myString.split('x')))