#1:
temperatures = []
prev_temp = None

for month in range(1,13):
    while True:
        try:
            temp = float(input('enter a temperature between -5c - 40c:'))
            if temp < -5 or temp > 40:
                print('the temperature is out of range')
                continue
            if temp == 0 and prev_temp == 0:
                print('the two temperatures in a row are zero, try again')
                continue
            temperatures.append(temp)
            prev_temp = temp
            break
        except ValueError:
            print('incorrect, please enter a value that is a number')
if len(temperatures) == 12:
    print('the input is correct')
else:
    print('incorrect')

avg_temp = sum(temperatures) / len(temperatures)
print(f'average temperatures for 2023 {avg_temp:.2f}C')

print(f'the max temperature is {max(temperatures)}')
print(f'the min temperature is {min(temperatures)}')

#2:

