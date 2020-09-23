from functools import cmp_to_key
(n,x,y) = map(int,input().strip().split())
contest_timing = []
for i in range(n):
    contest = list(map(int,input().strip().split()))[:2]
    contest_timing.append(contest + [i])
transport_to = list(map(int,input().strip().split()))
transport_back = list(map(int,input().strip().split()))
contest_timing = sorted(contest_timing,key= lambda x : x[0])
start_transport_arr = [None]*n
transport_to = sorted(transport_to)
#print(contest_timing,"contest timing")
#print(transport_to,"wormhole tranposting to destination")
i = 0
index_start_time = 0
while i < n:
    if contest_timing[i][0] < transport_to[index_start_time]:
        start_transport_arr[i] = None
        i += 1
        continue
    while index_start_time + 1 < x and contest_timing[i][0] >= transport_to[index_start_time+1]:
        index_start_time += 1
    start_transport_arr[contest_timing[i][2]] = transport_to[index_start_time]
    i += 1
#print(start_transport_arr,'start_transport_arr')
transport_back = sorted(transport_back)
contest_return_timing = [None]*n
contest_timing = sorted(contest_timing,key= lambda x:x[1])
index_end_time = y-1
i = n-1
#print(contest_timing,"contest timings")
#print(transport_back,"wormhole transporting back to home")
while i >= 0:
    if contest_timing[i][1] > transport_back[index_end_time]:
        contest_return_timing[i] = None
        i -= 1
        continue
    while index_end_time - 1 >= 0 and transport_back[index_end_time-1] >= contest_timing[i][1]:
        index_end_time -= 1
    contest_return_timing[contest_timing[i][2]] = transport_back[index_end_time]
    i -= 1
#print(contest_return_timing,"contest return timing")
# compare start_transport_arr contest_return_timing
min_time = float('inf')
for i in range(n):
    if start_transport_arr[i] is not None and contest_return_timing[i] is not None:
        min_time= min(min_time,contest_return_timing[i]- start_transport_arr[i] + 1)
print(min_time)