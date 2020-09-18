s = input()
a = []
for i in range(len(s)):
    a.append(int(s[i]))

for i in a:
    print(i, '\n')

# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])