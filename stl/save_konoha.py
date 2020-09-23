import heapq
from math import ceil
t= int(input())
def solve():
    (n,z) = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    my_heap = []
    for i in arr:
        heapq.heappush(my_heap,-i)
    count = 0
    while z > 0 :
        if len(my_heap) == 0:
            print("Evacuate")
            return
        curr_pop = - heapq.heappop(my_heap)
        z -= curr_pop
        x = -(ceil(curr_pop/2))
        if x > 0:
            heapq.heappush(my_heap,x)
        count += 1
    print(count)
    return
for _ in range(t):
    solve()
