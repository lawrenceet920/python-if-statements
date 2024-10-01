# Ethan Lawrence
# oct 1 2024
# If Else Python

# Task 2
alien_color = 'green'
# alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points')

if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')

# Task 3
fname = input('Please input your name:  ')

if len(fname) <= 5:
    print('Your name is too short.')
else:
    print(f'You have a long name, {fname}.')

# Task 4
vowels = ['a', 'e', 'i', 'o', 'u']
letter = input('Please enter a letter of the alphabet:  ').lower()

if letter in vowels:
    print('The letter {0} is a vowel'.format(letter))
else:
    print(f'The letter \'{letter}\' is a consonant')

# task 5
num1 = int(input('Please input a whole number:  '))
num2 = int(input('Please input another whole number:  '))

if num1 % num2 == 0:
    print(f'The first number "{num1}" is divisible by the second number "{num2}".')
else:
    print(f'"{num1}" is not divisable by "{num2}"')