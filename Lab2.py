#Activity 1
list = []
for i in range(5):
    val = input('Enter a number: ')
    list.append(val)

print("List of numbers: ", list)

#Activity 2
list = []
sum = 0
for i in range(5):
    val = input('Enter a number: ')
    sum += int(val)
    list.append(val)

print("List of numbers: ", list)
print("Sum of numbers: ", sum)

#Activity 3
list = []

for i in range(5):
    val = int(input('Enter a number: '))
    list.append(val)

list.sort()
print("Sorted List of numbers: ", list)

#Activity 4
list1 = []
list2 = []

for i in range(5):
    val = int(input('Enter a number: '))
    list1.append(val)

for i in range(5):
    val = int(input('Enter a number: '))
    list2.append(val)

list3 = list1 + list2
list3.sort()
print ("List is : " , list3)

#Activity 5
list = []

for i in range(5):
    val = int(input('Enter a number: '))
    list.append(val)

requiredNumber = int(input('Enter a number to search: '))
isFound = False
for i in range(5):
    if list[i] == requiredNumber:
        isFound = True
        break

if isFound:
    print("Found")
else:
    print("Not Found")

#Activity 6
def say_hello(name):
    print("Hello " + name + "!")
    return

say_hello("Rahim")
say_hello("Ali Raza")
say_hello("Abdul Hadi")
say_hello("Abdul Rehman")

#Activity 7
def isPalindrome(string):
    lowerCase = string.lower()
    for i in range(len(lowerCase)):
        if lowerCase[i] != lowerCase[len(lowerCase)-i-1]:
            return False
    return True

string = input("Enter a string: ")
if isPalindrome(string):
    print("String is palindrome")
else:
    print("String is not palindrome")

#Activity 8
def multiplyMatrix(a,b):
    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

a = [[1,0,0],
    [0 ,1,0],
    [0 ,0,1]]
b = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

result = multiplyMatrix(a,b)
for r in result:
    print(r)