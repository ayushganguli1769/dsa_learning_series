(m,n) = map(int,input().strip().split())
arr1 = list(map(int,input().strip().split()))[:m]
arr2 = list(map(int,input().strip().split()))[:n]
new_arr1 = [[arr1[i],i] for i in range(m)]
new_arr2 = [[arr2[i],i] for i in range(n)]
new_arr1 = sorted(new_arr1,key= lambda x : x[0])
new_arr2 = sorted(new_arr2,key= lambda x : x[0])
(x,y) = (0,0)
while x < m and y < n:
    print(new_arr1[x][1],new_arr2[y][1])
    if x != m -1:
        x += 1
    else:
        y += 1
#kaunsa bhang fuk ke previous solution likha tha