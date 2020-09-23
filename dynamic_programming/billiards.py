import sys
sys.setrecursionlimit(10**6)
t= int(input())
def recurse(req_sum):
    global memo,mod
    if req_sum in memo:
        return memo[req_sum]
    if req_sum < 0:
        return 0
    if req_sum == 0:
        return 1
    option1 = recurse(req_sum-2)
    option2 = recurse(req_sum-3)
    ans= option1 + option2
    memo[req_sum] = ans % mod
    return ans % mod
mod = 10**9 + 9
memo = {}
for _ in range(t):  
    req_sum = int(input())
    print(recurse(req_sum)% mod)