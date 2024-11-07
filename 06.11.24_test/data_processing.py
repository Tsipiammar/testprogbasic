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

# 3:
# max_value = None
# max_index = 0
# for siduri in range(5):
#     number = int(input('enter a five number:'))
#     if number > max_value:
#         max_value = number
#         max_index = siduri
# print(max_index)

# 4:
num1: int = int(input('enter a num 1?'))
num2: int = int(input('enter a num 2?'))
result = 0
for _ in range(num2):
    result += num1
print(result)

# 5:
numa: int = int(input('enter a num a?'))
numb: int = int(input('enter a num b?'))
res = 1
for _ in range(numb):
    res *= numa
print(res)

# 6:
number = (input('enter a number?'))
digit = (input('enter a digit?'))

if digit in number:
    print(True)
else:
    print(False)

# 7:
a: int = int(input('enter a?'))
b: int = int(input('enter b?'))
num_min = min(a, b)
for ob in range(num_min, 0, -1):
    if a % ob == 0 and b % ob == 0:
        print(ob)
        break

# 8:
a_num = int(input('type a number:'))
if a_num < 2:
    print('the number is not prime')
else:
    is_prime = True
    limit = a_num // 2
    for i in range(2, limit + 1):
       if a_num % i == 0:
           is_prime = False
           break
    if is_prime:
        print(f'{is_prime} the number is a prime')
    else:
        print(f'{is_prime} the number is not prime')
