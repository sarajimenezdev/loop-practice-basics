#1. Write a program that prints the numbers from 1 to 10 using a for loop.

for v in range(1,11):
    print(v)

#2. Write a program that prints the numbers from 10 to 1 in reverse order using a for loop.

for g in reversed(range(1,11)):
    print(g)
print('Happy New Year')

#3. Write a program that displays the numbers from 1 to 100 in increments of 2.
for i in range (2, 101, 2):
    print(i)

#4. Write a program that prints the numbers from 1 to 200 and skips the number 59 using a for loop.

for i in range(1, 201):
    if i == 59:
        continue
    print(i)
  
#5. Write a program that prints the numbers from 1 to 100, and at the end prints the count of how many numbers were multiples of 7.
count = 0
for i in range (1, 101):
    if i % 7 != 0:
        print(i)
    if i % 7 == 0:
        count += 1
print(count)
