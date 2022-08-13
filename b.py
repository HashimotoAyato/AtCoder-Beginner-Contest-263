N = int(input())
p = list(map(int, input().split()))

count = 1
t = p[-1]-2
while t != -1:
    t = p[t]-2
    count += 1
print(count)