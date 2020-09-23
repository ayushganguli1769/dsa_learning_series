t= int(input())
for _ in range(t):
    string = str(input())
    top = -1
    incorrect_stack = []
    n = len(string)
    for i in range(n):
        if string[i] == "<":
            incorrect_stack.append(i)
            top += 1
        elif string[i] == ">":
            if top >= 0 and string[incorrect_stack[top]] == "<":
                incorrect_stack.pop()
                top -= 1
            else:
                incorrect_stack.append(i)
                top += 1
    #print(incorrect_stack)
    if len(incorrect_stack) == 0:
        print(n)
    else:
        print(incorrect_stack[0])