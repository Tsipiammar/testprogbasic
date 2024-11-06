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
