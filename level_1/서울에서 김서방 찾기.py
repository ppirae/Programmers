def solution(seoul):
    answer = ''
    for name in seoul:
        if name=="Kim":
            answer = "김서방은 "+str(seoul.index(name))+"에 있다"
    return answer
