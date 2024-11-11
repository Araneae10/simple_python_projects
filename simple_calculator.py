num1 = int(input('enter the number:'))
num2 = int(input('enter the number:'))

operation = str(input('enter the operator:'))

if operation == '+':
    sum = num1 + num2
    print('the sum is:',sum)
elif operation == '-':
    sub = num1 - num2
    print('the subtraction is:',sub)
elif operation == '*':
    mul = num1 * num2
    print('the multiplication is:',mul)
elif operation == '/':
    div = num1 / num2
    print('the divition is:',div)
