t= int(input())
for _ in range(t):
    n = int(input())
    maxi = 0
    for _ in range(n):
        (s,p,v) = map(int,input().strip().split())
        curr = (p//(s+1)) * v
        maxi = max(maxi,curr)
    print(maxi)