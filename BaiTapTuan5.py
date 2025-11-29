#BaiTapTuan5

#W5A1

def Max_Of_Two(a, b):
    if a > b:
        return a
    else:
        return b
    
#W5A2

def swap(a, b):
    i = a
    a = b
    b = i
    return a, b

#W5A3

'''Kiem tra so nguyen to'''
def snt(a):
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a%i == 0:
                return False
        return True


    
#W5A4

'''Kiem tra so hoan hao'''
def cc(a):
    total = 0
    for i in range(1, int(a/2 + 1)):
        if a%i == 0:
            total += i
    if total == a:
        return True
    else:
        return False
    
#W5A5

def huhu(list, k):
    for i in list:
        if i == k:
            return list.index(i)    #khong can break, vi return tu no break
    return -1

#W5A6

def giai_thua(x):
    for i in range(1, x):
        x = x*i
    return x

#W5A7

def tinh(num1, num2, operat):
    if operat == "-":
        print("num1 - num2 = ", num1 - num2)
    elif operat == "+":
        print("num1 + num2 = ", num1 + num2)
    elif operat == "/":
        print("num1/num2 = ", num1/num2)
    else:
        print("num1*num2 = ", num1*num2)

#W5A8

#viet ham chuyen tu so nguyen sang so thap phan dang string
def int_to_bi(ii):
    str_bi = ""
    while ii != 0:
        if ii%2 == 0:
            str_bi = "0" + str_bi
        else:
            str_bi = "1" + str_bi
        ii = ii//2
    return str_bi

x1 = int(input("Nhap vao so nguyen duong 1: "))
x2 = int(input("Nhap vao so nguyen duong 2: "))

#chuyen so nguyen sang nhi phan dang string
x1 = int_to_bi(x1)
x2 = int_to_bi(x2)
len1 = len(x1)  #de sau nay chay chuoi khong phai tinh lai len nhieu lan
len2 = len(x2)

if len1 > len2:
    big_len = len1
    small_len = len2
else:   #len(x1) = len(x2) cung dung
    big_len = len2
    small_len = len1

# 4 = 100
# 1 = 1
#khac nhau = 2 => so sanh tu trai sang phai

k = big_len - small_len
hamming = k
for i in range(0, big_len - k):
    if x1[i] != x2[i]:
        hamming += 1

print("Khoang cach hamming: ", hamming)

#W5A9

def tong_chu_so(n):
    n = str(n)
    total = 0
    for i in n:
        total = total + int(i)
    return total

#W5A10

#lap ham tim tat ca vi tri cua 1 ki tu trong string
def loca(chuoi, ki_tu):
    vi_tri = []
    for x in chuoi:
        if x == ki_tu:
            vi_tri.append(chuoi.index(x))
    return vi_tri

#de bai cho hai tu dau vao cung do dai, khong can kiem tra do dai
def ktra_dang_cau(str1, str2):
    for x in str1:
        if x == str2[str1.index(x)]:
            pass
        elif loca(str1, x) == loca(str2, str2[str1.index(x)]):
            pass
        else:
            return False
    return True

#neu muon viet input de hoan thien chuong trinh thi viet input tu day












