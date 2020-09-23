t= int(input())
my_dict = {
        '^':3,
        '/':2,
        '*':2,
        '+':1,
        '-':1,
        '(':-1,
        ')':-1,
    }
for _ in range(t):
    n = int(input())
    string = str(input())
    ans = ""
    stack = []
    top = -1
    stack.append("(")
    string = string + ")"
    string = "".join(string.split())
    n += 1
    top += 1
    for i in range(n):
        if string[i] not in my_dict:
            ans += string[i]
        elif string[i] == "(":
            stack.append(string[i])
            top += 1
        elif string[i] == ")":
            while  stack[top] != '(':
                ans += stack.pop()
                top -= 1
            stack.pop()
            top -= 1
        else:
            while my_dict[stack[top]] >= my_dict[string[i]]:
                ans += stack.pop()
                top -= 1
            stack.append(string[i])
            top += 1
    print(ans)
