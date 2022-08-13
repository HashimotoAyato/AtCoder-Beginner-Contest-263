import math

N, L, R = map(int, input().split())
a = list(map(int, input().split()))

dp = [[math.inf for j in range(N+1)] for i in range(N+1)]
dp[0][0] = sum(a)
for i in range(1,N+1):
    dp[i][0] = dp[i-1][0] - a[N-i] + R

min_sum = math.inf
for i in range(0, N+1):
    for j in range(1,N+1-i):
        dp[i][j] = dp[i][j-1] - a[j-1] + L
        if dp[i][j] < min_sum:
            min_sum = dp[i][j]

for i in range(N+1):
    print(dp[i])
    