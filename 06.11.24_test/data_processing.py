# 1:
total_sum = None
while True:
    num_sum = int(input('enter a number?'))
    if num_sum == -99:
        print(f'the number you entered is None')
        break
    if total_sum == None:
        total_sum = num_sum
    else:
        total_sum += num_sum
if total_sum != None:
    print(f'the sum of the total numbers is {total_sum}')

# 2:
max_num = None
min_num = None
while True:
    num = int(input('enter a numbers(a zero or negative number go out)?'))
    if num == -99:
        print(f'the number you entered is None')
        break
    if num <= 0:
        break
    if max_num == None and min_num == None:
        max_num = num
        min_num = num
    else:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
if max_num != None:
    print(f'the highest number is {max_num}')
    print(f'the lowest number is {min_num}')

#3:
max_value = None
max_index = 0
for siduri in range(5):
    number = int(input('enter a five number:'))
    if number > max_value:
        max_value = number
        max_index = siduri
print(max_index)

#4:
num1: int = int(input('enter a num1?'))
num2: int = int(input('enter a num2?'))
result = 0
for _ in range(num2):
    result += num1
print(result)

#5:
