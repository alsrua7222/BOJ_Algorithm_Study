x, y = map(int, input().split())
x *= 2
y *= 3
stack = []
for a in range(2, 101, 2):
    if (100 - a) % 3 == 0:
        stack.append([a, 100 - a])

index = 0
answer = 0
while index < len(stack):
    if x >= stack[index][0] and y >= stack[index][1]:
        x -= stack[index][0]
        y -= stack[index][1]
        index = 0
        answer += 1
    else:
        index += 1
print(answer)