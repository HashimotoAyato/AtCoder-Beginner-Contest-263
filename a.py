C = list(map(int, input().split()))
C.sort()
ans = False
if C[0] == C[1] and C[4] == C[3]:
    if C[2] == C[0] or C[2] == C[4]:
        ans = True
print('Yes' if ans else 'No')