t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    if n == 0:
        print(0)
        continue
    tot = 0
    ceiling_limit = float('inf')
    for i in range(n):
        tot += min(arr[i],ceiling_limit)
        left_condition = i-1 < 0 or arr[i] <= arr[i-1]
        right_condition = i + 1 >= n or arr[i] <= arr[i+1]
        if left_condition and right_condition:
            ceiling_limit = min(arr[i],ceiling_limit)
    print(tot)