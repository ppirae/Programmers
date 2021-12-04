def solution(nums):
    answer = 0
    
    len1 = len(nums)/2
    len2 = len(set(nums))
               
    if len2 >= len1:
        answer = len1
    else:
        answer = len2
    
    return answer