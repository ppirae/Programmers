def solution(operations):
    import heapq
    hq = []

    def change(li):
        for i in range(len(li)):
            li[i] *= -1
        return li

    for i in range(len(operations)):
        oper = operations[i].split(" ")[0]
        num = int(operations[i].split(" ")[1])
        if oper == "I":
            heapq.heappush(hq, num)
        else:
            if len(hq) < 1:
                continue
            if num == 1:  # 최댓값 삭제
                hq = change(hq)
                if len(hq) > 1:
                    heapq.heapify(hq)
                heapq.heappop(hq)
                hq = change(hq)
                if len(hq) > 1:
                    heapq.heapify(hq)
            else:  # 최솟값 삭제
                heapq.heappop(hq)

    if hq == []:
        return [0, 0]
    else:
        return [max(hq), min(hq)]