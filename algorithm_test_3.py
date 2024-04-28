N = int(input())
height = []
line = input().split(' ')
for i in range(N):
    height.append(int(line[i]))

# dp = [[0] for i in range(N)]
# print(np.array(dp))
father = [0] * N
father[0] = height[0]
max_ = height[0]
re = 1
for i in range(1, N):
    k = 0
    while k < re and father[k] < height[i]:
        k += 1
    father[k] = height[i]
    if k >= re:
        re += 1

print(re)