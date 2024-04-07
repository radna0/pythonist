# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # Function

# # Vi du:
# x = input("Nhap vao so x: ")  # '123'
# y = int(x)  # 123
# str_y = str(y)  # '123'
# print(f"So vua nhap la: {str_y}")
# y_list = str_y.split("")    # ['1', '2', '3']
# str_y = ''.join(y_list)   # '123'


# # # # # # # # # def [ten_ham]([tham_so_1], [tham_so_2], ...):
# # # # # # # # #   [noi_dung_ham]
# # # # # # # # #   (return [gia_tri_tra_ve])

#  phuong trinh/ham chuyen doi input str -> int

# x = int(input("Nhap vao so x: "))  # '123'


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


# x = input_to_int("Nhap vao so x: ")  # '123'
# y = input_to_int("Nhap vao so y: ")  # '123'


# def check_age(age):
#     if age < 20:
#         print("nguoi do tre")
#     elif age > 40:
#         print("nguoi do gia")
#     else:
#         print("nguoi do la nguoi trung nien")


# # def compute_total(start, end, step=1):
# #     total = 0
# #     for i in range(start, end + 1, step):
# #         total += i
# #     return total


# # x = compute_total(0, 2, 2)
# # y = compute_total(1, 4)

# # print(x, y)

# # # # Bai Luyen Tap
# # # # 1.Tinh so nhan cac so tu 4 den -3, bo qua so 0
# x = int(input("nhap so x: "))
# y = int(input("nhap so y: "))

# total = 1
# for i in range(x,y, -1):
#     if i == 0:
#         continue
#     total *= i
#     print(total)


# # # # # # # # # #  vi du giai
# # # # # # # # # #
# # # # # # # # # #

# def input_to_int(input_str):
#     return int(input(input_str))


# def compute_total_multiply(start, end, step=1):
#     total = 1
#     for i in range(start, end + 1, step):
#         if i == 0:
#             continue
#         total *= i
#     return total


# x = input_to_int("nhap so x: ")
# y = input_to_int("nhap so y: ")

# total = compute_total_multiply(x, y, -1)

# print(total)

# # # # # # # # # #  cach toi uu, khi co truong hop ngoai le
# # # # # # # # # #
# # # # # # # # # #

# x = int(input("nhap so x: "))
# y = int(input("nhap so y: "))

# # x = -3
# # y = 4
# if x < y:
#     # -3
#     tmp = x
#     # x = 4
#     x = y
#     # y = -3
#     y = tmp

# x = 4
# y = -3

# for i in range(x, y, -1):
#     if i == 0:
#         continue
#     total *= i
#     print(total)


# def compute_total(start, end, step=1):
#     total = 0
#     for i in range(start, end + 1, step):
#         total += i
#     return total


# # # 2.lay ten cua 1 nguoi, va mot chu cai, neu chu cai do co trong ten nguoi do thi in ra "chu cai hien o vi tri thu: ",
# # # neu khong co thi in ra "chu cai khong co trong ten nguoi do"
# ten_nguoi = input("Nhap ten cua mot nguoi: ")
# chu_cai = input("nhap chu cai: ")

# vi_tri = ten_nguoi.index(chu_cai) + 1
# vi_tri2 = ten_nguoi.find(chu_cai) + 1

# if chu_cai in ten_nguoi:
#     print("chu cai hien o vi tri thu: ", vi_tri2)
# else:
#     print("chu cai hien khong co trong ten nguoi:")


# # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# lists/arrays
#      0  1  2  3  4
# arr = [1, "nam", 3, "huy", "bach"]
# print(arr)
# print(arr[0])
# print(arr[-1])
# leng = len(arr)
# print(arr[leng - 1])
# print(arr[1:3])


# # list out all list operations
# # O(1) - constant time
# arr.append(6)
# print(arr)

# # O(1) - constant time
# arr.pop()
# print(arr)

# # [1, 2, 3, 4, 5]
# # O(n) - linear time
# arr.insert(0, 0)
# # [0, 1, 2, 3, 4, 5]
# print(arr)

# # [0, 1, 2, 3, 4, 5]
# # O(n) - linear time
# arr.remove(0)
# print(arr)
# # [1, 2, 3, 4, 5]


# for i in range(0, leng):
#     print(f"number {i+1} ", arr[i])

# Bai luyen tap
# tao danh sach ten nguoi, in ra ten moi nguoi do
arr = ["nam", "bach", "huy"]
for i in arr:
    print(i)




for i, n in enumerate(arr):
    print(i, n)


# # Dictionaries
# my_dict = {"name": "John", "age": 30}
# print("Age:", my_dict["age"])


# # Tuples
# my_tuple = (1, 2, 3)
# print("Second element:", my_tuple[1])
