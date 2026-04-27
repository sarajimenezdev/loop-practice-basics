#5. Write a program that asks the user to enter a name, to print 'Hello' followed by the name, and to keep asking until the user enters a non-empty name.

name = input('¿Cuál es tu nombre? ')
while name == '':
    print('Por favor, ingresa tu nombre.')
    name = input('¿Cuál es tu nombre? ')
print(f'Hola {name}')

#6. Write a program that asks the user to enter their age, to print 'You are [age] years old', and to keep asking until the user enters a non-negative age.

age = int(input('¿Cuantos años tienes? '))
while age < 0:
    print('Tu edad no puede ser negativa')
    age = int(input('¿Cuantos años tienes? '))
print(f'Tienes {age} años')

# 7. Write a program that asks the user to enter a positive number, to print the multiplication table for that number from 1 to 10, and to keep asking until the user enters a positive number.
num = int(input('Enter a positive number: '))
while num < 0:
    print('That was not a positive number.')
    num = int(input('Enter a positive number: '))
if num > 0:
    for i in range (1, 11):
        print(f'{num} x {i} = {num * i}')
#8. Write a program that asks the user to enter numbers until they enter 0 and then displays the total sum.

number = int(input('Enter any number from 0 to 100: '))
total_sum = 0
while number != 0:
    total_sum += number
    number = int(input('Enter any number from 0 to 100: '))
print(f'The total sum is: {total_sum}')
