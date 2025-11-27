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







#W4A6



from math import sqrt

print("Tinh tong cac so nguyen to giua hai so nguyen duong nhap vao, so dau be hon so sau.")

hai_so = input("Nhap hai so cach nhau boi dau cach: ").split()

so_luong_so = len(hai_so)

'''kiem tra xem user co nhap dung hai so khong, co chen them chu vao khong, nhap sai so luong khong,
co dung so be truoc so lon khong'''

while True:
    check_result = 1   #1 la dung, 0 la sai

#kiem tra dinh dang so
    for run_check_1 in hai_so:
        if run_check_1.isdigit(): 
            pass

            #kiem tra thu tu so be so lon
            if run_check_1 == hai_so[so_luong_so - 1]:
                if 0 < int(hai_so[0]) < int(hai_so[so_luong_so -1]): 
                    #can phai de hai_so[so_luong_so -1] de phong truong hop chi 1 so duoc nhap vao
                    #se loi chuong trinh khong chay tiep duoc vi khong co so thu hai
                    #de la [so_luong_so -1] thi no se don gian la khien cho dieu kien bi sai
                    #do 1 so khong the be hon chinh no
                    #ket qua la neu chi nhap vao 1 so thi se khong duoc chap nhan, phai nhap lai
                    pass
                else:
                    check_result = 0

        else:
            check_result = 0
            break

    if so_luong_so != 2 or check_result == 0:
 
        hai_so = input("Sai so luong/dinh dang so/thu tu so be so lon, hay nhap lai: ").split() 
        #thieu split dong tren la sai, phai dung kieu tap hop ban dau, fix mai moi nhin ra, lau v, mat ca buoi toi
        so_luong_so = len(hai_so)
    else: 
        break

'''tinh tong cac so nguyen to giua hai so be so lon'''

#lap ham kiem tra so nguyen to

from math import sqrt

def kiem_tra_so_nguyen_to(r):
    can_bac_2 = int(sqrt(r))

    if r > 2 :
        for i in range (2, can_bac_2 + 1): #mac loi sai khong cong them 1 vao can_bac_2, the la chuong
                                           #trinh chi dem den can_bac_2 -1
            if r%i == 0:
                return 0
        return r
    elif r == 2:
        return 2

    else: #so be hon 2 thi khong phai so nguyen to
        return 0

#tong cac so nguyen to trong doan [so be, so lon]
total = 0
for count in range(int(hai_so[0]), int(hai_so[1]) + 1): #do trong tap hop nay la string, can chuyen ve int
    #print(kiem_tra_so_nguyen_to(count)) - lenh nay dung de kiem tra loi trong chuong trinh
    total += kiem_tra_so_nguyen_to(count)

print(f"Tong cac so nguyen to giua hai so la: {total}")




    



    




    












