def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    if m % n == 0:
        return n
    else:
        return gcd(m%n,n)
t = int(input())
for _ in range(t):
    (l,b) = map(int,input().strip().split())
    print(gcd(l,b))