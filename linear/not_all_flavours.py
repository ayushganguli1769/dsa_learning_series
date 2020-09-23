t= int(input())
for _ in range(t):
    (n,k) = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    my_dict = {}
    (l,r)= (0,0)
    max_length = -float('inf')
    while r < n:
        if len(my_dict) < k:
            while r <= n and len(my_dict) < k:
                curr_length = r- l
                max_length = max(max_length,curr_length)
                if r >= n:
                    break
                if arr[r] in my_dict:
                    my_dict[arr[r]] += 1
                else:
                    my_dict[arr[r]] =  1  
                r += 1                  
        else:
            while len(my_dict) == k:
                my_dict[arr[l]] -= 1
                if my_dict[arr[l]] <= 0:
                    del my_dict[arr[l]] 
                l += 1
    print(max_length)