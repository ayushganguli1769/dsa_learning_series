t= int(input())
for _ in range(t):
    (m,n,k) = map(int,input().strip().split())
    hash_set = set()
    count = 0
    coord_list = []
    for _ in range(k):
        (a,b) = map(int,input().strip().split())
        hash_set.add((a,b))
        coord_list.append((a,b))
    for coordinate in coord_list:
        if coordinate[0] -1 <= 0 or (coordinate[0] -1,coordinate[1]) not in hash_set:
            count += 1
        if coordinate[0] +1 > m or (coordinate[0] +1,coordinate[1]) not in hash_set:
            count += 1
        if coordinate[1] -1 <= 0 or (coordinate[0],coordinate[1] -1) not in hash_set:
            count += 1
        if coordinate[1] +1 > n or (coordinate[0],coordinate[1] +1) not in hash_set:
            count += 1
    print(count)