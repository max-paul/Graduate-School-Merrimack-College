def lp(A,left,right):
    p = A[left]
    s = left
    for i in range(left + 1, right +1):
        if A[i] < p:
            lp(A,s,i)
    lp(A,left,s)
    return s