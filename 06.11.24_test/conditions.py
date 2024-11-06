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
