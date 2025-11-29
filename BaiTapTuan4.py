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







###W4A6



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



###W4A7


n = input("Nhap vao so nguyen duong >= 2: ")

#kiem tra user nhap dung 1 so >= 2
while True:
    if n.isdigit():
          if int(n) >= 2:
               break
          else:
               n = input("Nhap lai so nguyen duong >= 2: ")
    else:
        n = input("Nhap lai so nguyen duong >= 2 : ")

#Ham kiem tra so nguyen to
from math import sqrt
def ktra_snt(p):
     if p == 2:
          return True    
     cb2 = sqrt(p)
     i = 2
     while i <= cb2 :
          if p%i == 0:
               return False
          i += 1
     return True

#Tim cac uoc tu be den lon, kiem tra snt
#Biet n >= 2

n = int(n)

uoc_hon_2 = []
for i in range (2, int(n/2)):
     if n%i == 0:
          uoc_hon_2.append(i)
uoc_hon_2.append(n)

#uoc so nguyen to max
u_snt_max = 0
for x in uoc_hon_2:
     if ktra_snt(x):
          u_snt_max = x

print(f"Uoc so nguyen to lon nhat cua so da nhap la: {u_snt_max}")




###W4A8



x = int(input("Nhap so nguyen duong: "))

#lap ham tim so doi xung
def reverse(n):

#count - dem so chu so
    count = 0
    n_count = n #can phai dat n_count rieng, khong dung lai n trong while de n khong bi
                #thay doi khi tinh reversed_num
    while True:   
        if n_count >= 1:
            n_count = n_count/10
            count += 1
        else:
            break

    reversed_num = 0
    for i in range (1, count + 1):
        reversed_num += (n%10)*(10**(count - i))
        n = int(n/10)

    return reversed_num

so_buoc = 0
while True: 
    if x == reverse(x):
        print("So doi xung/ Palindrome: ", x)
        print("So buoc: ", so_buoc)
        break
    else:
        x += reverse(x)
        so_buoc += 1
        



###W4A9



#lap ham kiem tra cac chu so doi mot khac nhau

def doi_mot_khac_nhau(a):
    a = str(a)
    for x in a:
        for i in range(a.index(x) + 1, len(a)):
            if x == a[i]:
                return False
            else:
                pass
    return True

#Tap hop cac so chinh phuong be hon n
from math import sqrt

n = input("Nhap vao so nguyen duong n: ")

#fool-proof
while True:
    if n.isdigit():
        if int(n) >= 0:   #can co int(n) vi n dang la str
            break
        else:
            n = input("Nhap lai so nguyen duong: ")
    else:
        n = input("Nhap lai so nguyen duong: ")

#chuyen n tu str sang int, de chay phan ben duoi
n = int(n)


for i in range(1, n +1):
    if sqrt(i)%1 == 0 and doi_mot_khac_nhau(i):
        print(i, end = " ")



###W4A10



#khong kiem tra user nhap dung hay sai nua, mac dinh la nhap dung di, met quaa
n = int(input("Nhap vao 1 so nguyen duong: "))

ans_count = 0           #so buoc chay lon nhat
longest_collatz = 0     #so co day collatz dai nhat
value = 0               #co dinh gia tri cua i de i chay 

for i in range(1, n + 1):
    count = 0           #bien dem so buoc chay
    value = i

    if i == 1:
        ans_count = 0
        longest_collatz = 1

    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = i*3 + 1
        count += 1
    if count > ans_count:
        ans_count = count
        longest_collatz = value

print("So co day Collatz dai nhat: ", longest_collatz)
print("So buoc: ", ans_count)
    



###W4A11


n = int(input("Nhap so nguyen duong < 10^6: "))
so_uoc_chan = 0

while n >= 10**6 or n <= 0:
    n = int(input("Nhap lai de em oi: "))

for i in range(1, n + 1):
    if n%i == 0 and i%2 == 0:
        so_uoc_chan += 1

print(f"So uoc chan cua so da nhap: {so_uoc_chan}")




###W4A12


print("Lai suat moi thang: 0,7%")
x = int(input("So tien gui vao theo don vi dong: "))
n = int(input("So thang tien duoc gui trong ngan hang: "))

#chi dung voi so thang >= 1
for i in range(1, n + 1):
    x = x + x*0.7/100

#lam tron
if x%1 >= 0.5:
    x = int(x) + 1
else:
    x = int(x)

print(f"So tien rut duoc sau {n} thang la: {x}")




###W4A13



#cap so than thiet

print("Kiem tra 2 so co phai la than thiet khong")

x1 = int(input("So thu nhat: "))
x2 = int(input("So thu hai: "))

#ham tinh tong cac uoc cua 1 so tru chinh so do
def cc(x):
    huhu = 0 #tong
    for i in range(1, int(x/2 + 1)): #uoc lon nhat tru so do khong lon hon 1/2 so do
                                     #chuyen thanh int vi no co the la float
        if x%i == 0:
            huhu += i
    return huhu

if cc(x1) == x2  and cc(x2) == x1:
    print("True")
else:
    print("False")




###W4A14



print("Tim uoc chung lon nhat cua hai so nguyen duong.")

x1 = int(input("Nhap so nguyen duong thu nhat: "))
x2 = int(input("Nhap so nguyen duong thu hai: "))

ucln = 0

if x1 < x2:
    for i in range(1, x1 + 1):
        if x1%i == 0 and x2%i == 0:
            ucln = i
elif x1 == x2:
    ucln = x1
else:
    for i in range(1, x2 + 1):
        if x1%i == 0 and x2%i == 0:
            ucln = i

print(f"Uoc chung lon nhat cua hai so: {ucln}")



###W4A15




tong_con = int(input("Nhap tong so con ga va cho: "))
tong_chan = int(input("Nhap tong so chan: "))

# ga + cho = tong_con
# 2.ga + 4.cho = tong_chan
# cho = (tong_chan - 2.tong_con) / 2
# ga = tong_con - cho

cho = (tong_chan - 2*tong_con) / 2
if cho == int(cho):
    ga = tong_con - cho
    print(f"So cho va ga lan luot la: {cho}, {ga}")
else:
    print("Invalid ")

#Rieng bai nay khong can test, cho vao file btvn luon

    


























 





        





    



    




    












