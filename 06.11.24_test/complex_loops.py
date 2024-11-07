# 1:
temperatures = []
prev_temp = None

for month in range(1, 13):
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

# 2:
topic = input('enter the voting topic')
votes_for = 0
votes_against = 0
votes_abstain = 0
veto_country = None
first_vote_for = None
last_vote_against = None
votes = []
for country_number in range(1, 44 + 1):
    while True:
        try:
            vote = int(input('enter your vote:[1- for, 2- against, 3- abstain, 4- veto]'))
            if vote == 1:
                votes_for += 1
                if first_vote_for is None:
                    first_vote_for = country_number
            elif vote == 2:
                votes_against +=1
                last_vote_against = country_number
            elif vote == 3:
                votes_abstain += 1
            elif vote == 4:
                veto_country = country_number
                print(f' the state number {veto_country} vetoed, the program stopped')
                break
            else:
                print('the vote is invalid, try again')
                continue
            votes.append(vote)
            break
        except ValueError:
            print('enter only a number')
    if veto_country:
        break
if veto_country is None:
    print(f'the number of votes in for {votes_for}')
    print(f'the number of votes in against {votes_against}')
    print(f'the number of votes in abstain { votes_abstain}')
else:
    pass
if first_vote_for:
    print(f'the first country to vote in favor{first_vote_for}')
else:
    print(f'there was no country that voted in favor')
if last_vote_against:
    print(f'the last country to vote against {last_vote_against}')
else:
    print(f'there was no country that voted against')
