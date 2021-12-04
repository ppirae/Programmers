def solution(nums):
    answer = -1
    cnt = 0
    result = []
    sosu = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                result.append(nums[i]+nums[j]+nums[k])
            
    result = list(result)
    result.sort()
    for i in result:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            sosu.append(i)
            cnt = 0
    
    answer = len(sosu)
    
    return answer