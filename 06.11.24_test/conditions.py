# 1:
one: float = float(input('enter the first number?'))
two: float = float(input('enter the first number?'))

for _ in range(3):
    print(min(one, two))

# 2:
num_1: int = int(input('enter a number 1?'))
num_2: int = int(input('enter a number 2?'))
print((num_1 + num_2) / 2)

# 3:
max_num: int = int(input('enter a number?'))
for i in range(2):
    num = int(input('enter a number?'))
    if num > max_num:
        max_num = num
print(max_num)

# 4:
movie: int = int(input('how long is the movie in minutes?'))
hours = movie // 60
minutes = movie % 60
print(f'the length of the movie is {hours} hours and {minutes} minutes')

# 5:
four_digits: int = int(input('enter a four - digit number?'))
print(f'the last number is {four_digits % 10}')

# 6:
number = four_digits // 10
second = number % 10
print(f' the second number from the end is {second}')

# 7:
x: int = int(input('enter a two - digit number?'))
print(f'the sum of the digits is {(x // 10) + (x % 10)}')

# 8:
y: int = int(input('enter a two - digit number?'))
print(f'the opposite number is {(y % 10) * 10 + (y // 10)}')

# 9:
z: int = int(input('enter a z:'))
if z % 2 == 0:
    print('even')
else:
    print('odd')

# 10:
salary: float = float(input('enter your salary?'))
tax = 0
if salary <= 6000:
    tax = 0
elif salary <= 12000:
    tax = (salary - 6000) * 0.1
elif salary <= 18000:
    tax = (12000 - 6000) * 0.1 + (salary - 12000) * 0.2
elif salary <= 25000:
    tax = (12000 - 6000) * 0.1 + (18000 - 12000) * 0.2 + (salary - 18000) * 0.3
elif salary <= 35000:
    tax = (12000 - 6000) * 0.1 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (salary - 25000) * 0.4
elif salary <= 50000:
    tax = (12000 - 6000) * 0.1 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (35000 - 25000) * 0.4 + (
                salary - 50000) * 0.51
print(f' the tax on your salary is {tax:.2f}')

# 11:
age: int = int(input('enter your age?'))
height: float = float(input('enter your height?'))
if 8 <= age <= 18 and height > 115:
    print(f'you are allowed to get on a roller coaster')
elif age > 18 and height > 100:
    print(f'you are allowed to get on a roller coaster')
else:
    print(f'you are not allowed to get on a roller coaster')
