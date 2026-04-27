#1. Write a program that prints the numbers from 1 to 50, but for multiples of 3, print 'Fizz' instead of the number, for multiples of 5, print 'Buzz', and for multiples of both 3 and 5, print 'FizzBuzz'.

for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')

#2. Write a program that prints the numbers from 1 to 100, but for multiples of 2, print 'A' instead of the number, for multiples of 3, print 'B', and for multiples of both 2 and 3, print 'AB'.

for v in range (1,101):
    if v % 2 == 0 and v % 3 == 0:
        print('AB')
    elif v % 2 == 0:
        print('A')
    elif v % 3 == 0:
        print('B')
    else:
        print(v)
#3. Write a program that prints the numbers from 1 to 50, but for multiples of 4, print 'X' instead of the number, for multiples of 6, print 'Y', and for multiples of both 4 and 6, print 'XY'.

for j in range (1, 51):
    if j % 4 == 0 and j % 6 == 0:
        print('XY')
    elif j % 4 == 0:
        print('X')
    elif j % 6 == 0:
        print('Y')

#4. Write a program that prints the numbers from 1 to 100, but for multiples of 3, print 'Fizz' instead of the number, for multiples of 5, print 'Buzz', and for numbers that are not multiples of either 3 or 5, print the number itself.

for i in range (1, 101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
