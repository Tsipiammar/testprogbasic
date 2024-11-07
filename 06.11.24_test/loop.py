# 1:
top: int = int(input('enter a top number:'))
for i in range(1, top + 1):
    print(i, end=',')
print()

# 2:
num1: int = int(input('enter the first number?'))
num2: int = int(input('enter the last number?'))
if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=',')
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end=',')
print()

# 3:
n: int = int(input('enter a natural number:'))
for i in range(0, n + 1, 2):
    print(i, end=' ')
print()

# 4:
max_num: int = int(input('enter a max number?'))
den: int = int(input('enter a den number?'))
for i in range(1, max_num + 1):
    if i % den == 0:
        print(i, end=' ')
print()
