#creating sieve sum
import math
N = 1000000
dp = [0] * (N + 1)
def sieve():
    array = [0] * (N + 1)
    array[0] = 1
    array[1] = 1
    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if array[i] == 0:
            for j in range(i * i, N + 1, i):
                array[j] = 1
    runningPrimeSum = 0
    for i in range(1, N + 1):
        if array[i] == 0:
            runningPrimeSum += i
        dp[i] = runningPrimeSum
sieve() #instead of calling the sieve inside the loop, create a copy of sieve in the memory itself
nc = int(input())
for _ in range(nc):
    l,r = map(int, input().rstrip().split())
    print(dp[r]-dp[l-1])
