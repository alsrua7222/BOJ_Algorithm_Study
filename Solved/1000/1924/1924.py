days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
day = y
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(x - 1):
    day += days[i]

print(week[day % 7])