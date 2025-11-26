#BaiTapTuan4

###W4A1
i = int(input("Enter an integer not higher than 1000: "))

if i > 1000:
    print("The number is higher than 1000.")
    i = int(input("Please enter an integer not higher than 1000: "))
else:
    print("The number is acceptable.")

total = 0

if i >= 1:
    for n in range (1, i+1):
        total += n
else:
    for n in range (1, i-1, -1):
        total += n

print("The sum from 1 to", i, "is:", total)





###W4A2
from math import sqrt


n = int(input("Enter an integer above 0:"))


if n <= 0:
    print("The number is not above 0.")
    n = int(input("Please enter an integer above 0:"))

if n <= 1:
    print(n, "is not a prime number.")

for i in range(1, int(sqrt(n))+1):
    if n%i == 0 and i != 1:
        print(n, "is not a prime number")
        break
    else:
        if i == int(sqrt(n)):
            print(n, "is a prime number.")


###W4A3

n = int(input("Insert an integer above 0 and less than 100: "))

while n <= 0 or n >= 100:
    n = int(input("Insert an integer above 0 and less than 100: "))

total = 1

for i in range (1, n+1):
    total = total*i

print("Factorial of " , n , "is: ", total)



###W4A4

n = int(input("Counting digits of the integer: "))

if n == 0:
    print("Number of digits: 1")


count = 0
while int(n) != 0:
    n = n/10
    count += 1

print("Number of digits: ", count)





###W4A5





n = input("Length of array of numbers - above 0: ")


#check if  n is number above 0
while True:
    if n.isdigit() and int(n) > 0:
        break
    else:
        n = input("Invalid, length must be integer above 0, type again:")

n = int(n)



#insert array
array = input(f"Insert numbers spaced by one space, length is {n}: ").split() # LeQuang
length_of_array = len(array)

#check if array has the right length

while length_of_array != n:
    print("Wrong length, try again!")
    array = input(f"Insert numbers spaced by one space, length is {n}: ").split()
    length_of_array = len(array) #need this to get the length of the new array in the variable,
                                 #otherwise the length stay the same as the line with LeQuang
   

#check for non-number in array

non_number_count = 0

while True:
    for run_check in array:
        if run_check.isdigit():
            pass
        else:
            non_number_count += 1
    if non_number_count >= 1:
            print(f"Array contains {non_number_count} non-number(s), please try again!")
            array = input(f"Insert numbers spaced by one space, length is {n}: ").split()
            non_number_count = 0           #set n_n_c back to 0 to check for nnb again
    else:
        break
    


#check 42

if '42' in array:
    print("I have found the meaning of life!")
else:
    print("Just a joke.")

    












