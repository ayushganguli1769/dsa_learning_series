mod = 10**9 + 7
(n,k) = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
unique_set = set()
for i in arr:
    unique_set.add(i)
unique_count = len(unique_set)
#nCr + nCr-1 = (n+1)Cr

