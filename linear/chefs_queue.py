mod = 1000000007
(n,k) = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))[:n]
stack = []
top = -1
fear = 1
ans = [None]*n
for i in range(n):
    if top == -1 or arr[i] >= arr[stack[top]]:
        stack.append(i)
        top += 1
    else:
        while top >= 0 and arr[i] < arr[stack[top]]:
            pop_index = stack.pop()
            top -= 1
            ans[pop_index] = i
        stack.append(i)
        top += 1
for i in range(n):
    if ans[i] is not None:
        fear *= (ans[i]-i +1)
        fear %= mod
print(fear% mod)