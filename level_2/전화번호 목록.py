def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(1, len(phone_book)):
        if str(min(phone_book)) in str(phone_book[i]):
            answer = False
            break
    return answer
