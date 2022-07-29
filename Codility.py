def solution(A):
    # write your code in Python 3.6
    A.sort()
    B = set()
    for i in range(1,len(A)):
        print(A)
        B.add(A[i])
        print(B)
        if A[i] - A[i-1] !=1:
            
            # print(A)
            return i
        else:
            return False
        
    return A
print(solution([13,16,14,10, 15]))