
# # # For loop


# # # # # # # # # for i in range([start], [end], [step]):
# # # # # # # # #  [noi_dung_vong_lap]
# # # # # # # # #  (break)
# # # # # # # # #  (continue)

# diem bat dau cua vong lap luon luon la i = 0
# vi tri i = vi tri hien tai - 1

# vi tri i cua cac vong lap trong ngon ngu = vi tri hien tai - 1
# tong [0,3) hoac [0,2]
# for i in range(3):
#     print(i)

# for i in range(0,3):
# print(i)

# tong [2,6) hoac [2,5]

# for i in range(2, 6):
#     print(i)
# total = 0
# for x in range(3, 6):
#     total += x
# print(total)

# tong [0, 6) hoac [0, 5], bo qua so chia het cho 3

#  ctrl + / de comment nhieu dong
# for n in range(0, 7):
#     if n % 3 == 0:
#         print("Bo qua so chia het cho 3: ", n)
#         continue
#     print(n)

# tong [5, 9) hoac [5, 8], dung lai khi gap so chia het cho 4
# for n in range(5, 10):
#     if n % 4 == 0:
#         break
#     print(n)

# tong [12, 17) hoac [12, 16], print gia tri truoc va dung lai khi gap so chia het cho 5

# for n in range(12, 17):
#     if n % 5 == 0:
#         break
#     print(n)


# # tong cac so tu [input1] den [input2]
# x = int(input("Nhap vao so dau tien: "))
# y = int(input("Nhap vao so dau tien: "))

# total = 0
# for i in range(x, y + 1):
#    total += i
# # total = total + i
# print(total)


# for y in range(0, 7, 2):
#   print(y)


# for i in range(8, 3, -1):
#     print(i)

# for i in range(3):
#     print(i)

# for i in range(0, 3, 1):
#     print(i)

# Bai Luyen Tap
# 1.Tinh tong cac so tu 0 den 5
# n = int(input("nhap so: "))
# m = int(input("nhap so: "))

# total = 0
# for i in range(n,m + 1):
#      total = total + i
# print(total)


# 2.Tinh so nhan cac so tu 4 den -3
# neu la so 0 thi bo qua, nhung ko dung
# n = int(input("????: "))
# m = int(input("????: "))

# total = 1
# for i in range(n, m, -1):
#     if i == 0: # if total == 0
#         continue
#     total = total * i
#     print(total)


# 3.Tinh tong cac so tu 0 den 10 la so chan
# n = int(input("?????: "))
# m = int(input("???: "))
# total = 0
# for i in range(n,m):
#     if i % 2 == 0:
#         total = total + i
#     print("so chan ", total)


# 4.Tinh tong cac so tu [input1] den [input2], 1, 16
# neu gap mot so chia het cho 5, nhan so do vao tong
# neu gap mot so chia het cho 3, bo qua so do
# neu gap mot so chia het cho 3 va ca 5, dung vong lap
# n = int(input("OMG: "))
# m = int(input("OMG: "))
# total = 0
# for i in range(n, m):
#     print("i = ", i)
#     if i % 3 == 0 and i % 5 == 0:
#         break
#     if i % 3 == 0:
#         continue
#     if i % 5 == 0:
#         total = total * i
#         print(total)
#     total = total + i
#     print("total + i ", total)

# n = int(input("OMG: "))
# m = int(input("OMG: "))
# total = 0
# for i in range(n, m):
#     print(f"i = {i}")
#     if i % 3 == 0 and i % 5 == 0:
#         break
#     elif i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         total *= i
#     else:
#         total += i

#     print("total + i", total)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # While loop

# # # # # # # # # while [dieu_kien_dung]:
# # # # # # # # #  [noi_dung_vong_lap]
# # # # # # # # #  (break)
# # # # # # # # #  (continue)


# while True:
#     print("Hello")

# n = 0
# while n < 3:
#     print(n)
#     n += 1

# n = 5
# while n <= 10:
#     print(n)
#     n += 2

# n = 9
# while n >= 0:
#     print(n)
#     n -= 3


# # # Bai Luyen Tap
# 1.Tinh tong cac so tu 0 den 5
# x = int(input("so: "))
# total = 0
# while x <= 5:
#     total += x
#     print(x)
#     x += 1
# print(total)
# 2.Tinh hieu cac so tu 3 den -5
# x = 3
# y = -5
# total = 0
# while x >= y:
#     total -= x
#     print(x)
#     x -= 1
# print(total)

# 3.Tinh tong cac so tu 0 den 10 la so le
# x = int(input("so: "))
# y = int(input("so: "))
# total = 0
# while x <= y:
#     if x % 2 == 1:
#         total += x
#         print("la so le", total)
#     x += 1

# while x <= y:
#     if x % 2 != 0:
#         total += x
#         print("la so le", total)

# while x <= y:
#     if not (x % 2 == 0):
#         total += x
#         print("la so le", total)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # Function

# Vi du:
# x = input("Nhap vao so x: ")
# y = int(x)
# str_y = str(y)
# print("So vua nhap la: ", str_y)


# # # # # # # # # def [ten_ham]([tham_so_1], [tham_so_2], ...):
# # # # # # # # #   [noi_dung_ham]
# # # # # # # # #   (return [gia_tri_tra_ve])

#  phuong trinh/ham chuyen doi input str -> int

# def input_to_int(input_str):
#     return int(input(input_str))


# nam_sinh = input_to_int("Nhap vao nam sinh: ")


# def check_even(num):
#     return num % 2 == 0


# tuoi = input_to_int("Nhap vao so tuoi: ")
# is_even = check_even(tuoi)
# if is_even:
#     print("So tuoi la so chan")
# else:
#     print("So tuoi la so le")


# def check_age(age):
#     if age < 20:
#         print("nguoi do tre")
#     elif age > 40:
#         print("nguoi do gia")
#     else:
#         print("nguoi do la nguoi trung nien")


# def compute_total(start, end, step=1):
#     total = 0
#     for i in range(start, end + 1, step):
#         total += i
#     return total


#
for i in range (5):
    print("lap lan thu", i + 6)
