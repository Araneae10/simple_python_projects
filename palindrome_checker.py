num = input('enter the number:')

a = num[::-1]

if num == a:
    print(f'the given number {num} is palindrome')
else:
    print(f'the given number {num} is not palindrome')