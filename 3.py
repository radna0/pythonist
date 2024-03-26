
# # # For loop

# # # # # # # # # for i in range([start], [end], [step]):
# # # # # # # # #  [noi_dung_vong_lap]
# # # # # # # # #  (break)
# # # # # # # # #  (continue)

# tong [0,3) hoac [0,2]
for i in range(3):
    print(i)


# tong [2,6) hoac [2,5]

for i in range(2, 6):
    print(i)
# total = 0
# for x in range(3, 6):
#     total += x
# print(total)

# tong [0, 6) hoac [0, 5], bo qua so chia het cho 3

for n in range(0, 7):
    if n % 3 == 0:
        continue
    print(n)

# tong [5, 9) hoac [5, 8], dung lai khi gap so chia het cho 4
for n in range(5, 9):
    if n % 4 == 0:
        break
    print(n)

# tong [12, 17) hoac [12, 16], print gia tri truoc va dung lai khi gap so chia het cho 5

for n in range(12, 17):
    print(n)
    if n % 5 == 0:
        break


# tong cac so tu [input1] den [input2]
x = int(input("Nhap vao so dau tien: "))
y = int(input("Nhap vao so dau tien: "))

total = 0
for i in range(x, y + 1):
    total += i
print(total)


# for y in range(0, 7, 2):
#   print(y)


# for i in range(8, 3, -1):
#     print(i)

# Bai Luyen Tap
# 1.Tinh tong cac so tu 0 den 5

# 2.Tinh tong cac so tu 9 den 6

# 3.Tinh tong cac so tu 0 den 10 la so chan

# 4.Tinh tong cac so tu [input1] den [input2]
# neu gap mot so chia het cho 5, dung vong lap
# neu gap mot so chia het cho 3, bo qua so do


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # While loop

# # # # # # # # # while [dieu_kien_dung]:
# # # # # # # # #  [noi_dung_vong_lap]
# # # # # # # # #  (break)
# # # # # # # # #  (continue)


while True:
    print("Hello")

n = 0
while n < 5:
    print(n)
    n += 1

n = 5
while n <= 10:
    print(n)
    n += 2

n = 9
while n >= 0:
    print(n)
    n -= 3


# # # Bai Luyen Tap
# 1.Tinh tong cac so tu 0 den 5

# 2.Tinh tong cac so tu 3 den -5

# 3.Tinh tong cac so tu 0 den 10 la so le


# count = 0
# while count < 5:
#     print(count)
#     count += 1


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
