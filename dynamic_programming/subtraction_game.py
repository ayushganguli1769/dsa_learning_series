def gcd(m,n):
    if m is None:
        return n
    elif n is None:
        return m
    if m < n:
        (m,n) = (n,m)
    if m % n == 0:
        return n
    else:
        return gcd(m%n,n)
def solve(curr_gcd,index,arr,n):
    global memo
    if (index,curr_gcd) in memo:
        return memo[(index,curr_gcd)]
    if index == n:
        if curr_gcd is None:
            return 0
        elif curr_gcd == 1:
            return 1
        else:
            return 0
    count =  0
    count += solve(curr_gcd,index+1,arr,n)#do not include the arr[index]
    count += solve(gcd(curr_gcd,arr[index]),index+1,arr,n)#include arr[index]
    memo[(index,curr_gcd)] = count
    return count
    
t= int(input())
for _ in range(t):
    memo = {}
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    print(solve(None,0,arr,n))