(n,k,p) = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))[:n]
my_arr = [[arr[i],i+1] for i in range(len(arr))]
my_arr = sorted(my_arr,key= lambda x:x[0])
group_dict = {}
N = len(my_arr)
curr_group = 0
for i in range(N):
    group_dict[my_arr[i][1]] = curr_group
    if i + 1 < N:
        if abs(my_arr[i][0] - my_arr[i+1][0] )> k:
            curr_group += 1
for _ in range(p):
    (a,b) = map(int,input().strip().split())
    if group_dict[a] == group_dict[b]:
        print("Yes")
    else:
        print("No")
