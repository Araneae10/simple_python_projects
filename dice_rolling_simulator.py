import random

consent = input('enter yes if you want to roll the dice:').upper()
print(consent)
dice_number = True if consent == 'yes' else False
if(dice_number):
    r1 = random.randint(1,6)
    print(f'the number after rolling the dice is {r1}')
else:
    print('the dice did not roll')