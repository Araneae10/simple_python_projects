cur = int(input('enter the amount you want to convert:'))

current_amount = input('which of the following do you wanna convert to us,eur,gbp:').lower()

us = 134

eur = 120

gbp = 153

if current_amount == 'us':
    aum = us * cur 
    print(aum)
if current_amount == 'eur':
    aum = eur * cur 
    print(aum)
if current_amount == 'gbp':
    aum = gbp * cur     
    print(aum)