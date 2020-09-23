from math import floor,ceil
t= int(input())
def solve():
    n = int(input())
    string = str(input())
    num_arr = [int(i) for i in string]
    (a_count,b_count) = (0,0)
    #tot strikes taken till tht turn is i +1
    for i in range(2*n):
        turn_a_left = floor((2*n - i -1)/2)
        turn_b_left = ceil((2*n - i -1)/2)
        if i % 2 == 0 and num_arr[i] == 1:
            a_count += 1
        elif i % 2 != 0 and num_arr[i] == 1:
            b_count += 1 
        if a_count + turn_a_left < b_count:
            return (i +1)
        elif b_count + turn_b_left < a_count:
            return (i+1)
    return 2*n
for _ in range(t):
    print(solve())

