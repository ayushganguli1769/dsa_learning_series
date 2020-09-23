t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    curr_length = 1
    total = 1
    for i in range(1,n):
        if arr[i] >= arr[i-1]:
            curr_length += 1
            total += curr_length
        else:
            curr_length = 1
            total += curr_length
    print(total)