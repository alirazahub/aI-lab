# print number on screen
print(24)

print('''Hello world
    of python
''')


#Small Tasks for practice
print(50-4)
print(23.5 + 2.1)
print((int)(23.4 / 3.1))
print(28//4)
print(26//4)
print(4**3)
print(4**10)

print(2+3*6)
print((2+3)*6)
print(48565878*578453)
print(2     +     2)
print((5-1)*((7+1)/((3-1))))

print('My lucky number is %d, what is yours' % 7)
print('My lucky number is ' + str(7) + ', what is yours')

name = input('What is your name? ')
print('Hello %s' % name)

num  = input('Enter a number: ')
print('Your number is %s' % num)

#Class Activity
num = input('Enter a number: ')
if(int(num) %2 == 0):
    print('Even')
else:
    print('Odd')

num = 0

for i in range(1, 11):
    num += i

print(num)

#
while(True):
    num2 = int(input('Enter a number: '))
    if(num2 == 0):
        break
    else:
        num += num2



#Home Task 1
number = int(input("Enter a number: "))
isNotPrime = False

if number > 1:
    for i in range(2, number):
        print(i)
        if (number % i) == 0:
            isNotPrime = True
            break
if isNotPrime:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
    

# 11-sep-2023
#Activity 1 Grading System
number = int(input("Enter your Marks: "))
if number < 50:
    print("F")
elif number >= 50 and number < 60:
    print("D")
elif number >= 60 and number < 70:
    print("C")
elif number >= 70 and number < 80:
    print("B")
elif number >= 80 and number < 90:
    print("A")
elif number >= 90 and number <= 100:
    print("A+")
else:
    print("Invalid Input")

#Activity 2 Factorial
number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of", number, "is", factorial)