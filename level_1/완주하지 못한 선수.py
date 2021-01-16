def solution(participant, completion):
    complement = list(set(participant) - set(completion))
    if  len(complement) != 0:
        return complement[0]

    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

    answer = ''
    return answer
