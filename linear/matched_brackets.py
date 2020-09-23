n= int(input())
arr = list(map(int,input().strip().split()))[:n]
n = len(arr)
stack = []
top = -1
curr_depth = 0
max_depth = -float('inf')
max_depth_pos = None
max_seq_length = -float('inf')
max_seq_pos = None
for i in range(n):
    if arr[i] == 1:
        stack.append(i)
        top += 1
        curr_depth += 1
    else:
        pop_index = stack.pop()
        curr_depth -= 1
        curr_seq_length = i - pop_index + 1
        if curr_seq_length > max_seq_length:
            max_seq_length = curr_seq_length
            max_seq_pos = pop_index + 1
    if curr_depth > max_depth:
        max_depth = curr_depth
        max_depth_pos = i + 1
print(max_depth,max_depth_pos,max_seq_length,max_seq_pos)