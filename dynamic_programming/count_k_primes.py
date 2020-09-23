from math import sqrt
from math import ceil
import sys
def sieve(N):
    prime_count = [0]* (N+2)
    for i in range(2,N+1):#we go till N+1 as there are non primes after sqrt(N) or n//2 + 1 but they there are already marked in sieve as non prime or False. Here we also need to mark primes with number of factors
        if prime_count[i] == 0:
            prime_count[i] += 1
            for j in range(2*i,N+1,i):
                prime_count[j] += 1
    return prime_count
N = 100000
prime_count =sieve(N+200)
(count1,count2,count3,count4,count5) = (0,0,0,0,0)
(prime1,prime2,prime3,prime4,prime5) = ([0]*(N+200),[0]*(N+200),[0]*(N+200),[0]*(N+200),[0]*(N+200))
for i in range(2,N+1):
    if prime_count[i] == 1:
        count1 += 1
    elif prime_count[i] == 2:
        count2 += 1
    elif prime_count[i] == 3:
        count3 += 1
    elif prime_count[i] == 4:
        count4 += 1
    elif prime_count[i] == 5:
        count5 += 1
    prime1[i] = count1
    prime2[i] = count2
    prime3[i] = count3
    prime4[i] = count4
    prime5[i] = count5 

t = int(input())
for _ in range(t):
    (a,b,k) = map(int,input().strip().split())
    if k == 1:
        print(prime1[b]- prime1[a-1])
    elif k == 2:
        print(prime2[b]- prime2[a-1])
    elif k == 3:
        print(prime3[b]- prime3[a-1])
    elif k == 4:
        print(prime4[b]- prime4[a-1])
    elif k == 5:
        print(prime5[b]- prime5[a-1])