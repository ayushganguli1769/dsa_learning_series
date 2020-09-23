n = int(input())
coordinate_list = [[0,0]]
for _ in range(n):
    curr_coordinate = list(map(int,input().strip().split()))
    coordinate_list.append(curr_coordinate)
coordinate_list.append([100000,500])
coordinate_list.append([100000,0])
stack = []
top = -1
n = len(coordinate_list)
max_area = -float('inf')
for i in range(n):
    if top == -1 or coordinate_list[i][1] >= coordinate_list[stack[top]][1]:
        stack.append(i)
        top += 1
    else:
        while top >= 0 and coordinate_list[i][1] < coordinate_list[stack[top]][1]:
            pop_index = stack.pop()
            top -= 1
            print(coordinate_list[i][0],coordinate_list[stack[top]][0],coordinate_list[pop_index][1],'debug')
            if top >= 0:
                curr_area = (coordinate_list[i][0]- coordinate_list[stack[top]][0]) * coordinate_list[pop_index][1]
            else:
                curr_area = coordinate_list[i][0] * coordinate_list[pop_index][1]

            max_area = max(max_area,curr_area)
        stack.append(i)
        top += 1
print(max_area)
