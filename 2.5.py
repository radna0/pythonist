
# # # And / Or / Not + TRUE/FALSE (BOOLEAN)


# # # And

# # # True and True = True
# # # True and False = False
# # # False and True = False
# # # False and False = False

# x = int(input("so thu 1: "))
# y = int(input("so thu 2: "))

# if x > 0 and y > 0:
#     print("ca 2 so deu lon hon 0")
# elif x > 0 and y < 0:
#     print("so thu 1 lon hon 0, so thu 2 nho hon 0")
# elif x < 0 and y > 0:
#     print("so thu 1 nho hon 0, so thu 2 lon hon 0")
# else:
#     print("ca 2 so deu nho hon 0")


# # # Or

# # # True or True = True
# # # True or False = True
# # # False or True = True
# # # False or False = False


# x = int(input("mot so bat ky: "))

# #  uu tien su dung cach nay
# #  code nay de hieu, ngan gon, it dieu kien hon
# #  chi dung else khi co nhieu truong hop khac nhau
# #  ma khong can phai xac dinh ro rang
# if x == 0:
#     print("so do bang 0")
# else:
#     print("so do khac 0")

# if x > 0 or x < 0:
#     print("so do khac 0")
# else:
#     print("so do bang 0")


# x = int(input("so thu 1: "))
# y = int(input("so thu 2: "))

# if x > 0 and y > 0:
#     print("ca 2 so deu duong")
# elif (x > 0 and y < 0) or \
#         (x < 0 and y > 0):
#     print("ca 2 so trai dau")
# elif x == 0 and y == 0:
#     print("ca 2 so deu bang 0")
# else:
#     print("ca 2 so deu am")


# # # # Not

# input = True/False
# output = not(input)

# # # # not True = False
# # # # not False = True

# # # # not not True = True
# # # # not not False = False

#  + * - = -
#  - * - =  +


x = int(input("so bat ky: "))

is_even = (x % 2 == 0)

# uu tien su dung cach nay
# neu co the, hay so sanh ko dung NOT
if is_even:
    print("so chan")
else:
    print("so le")

if not is_even:
    print("so le")
else:
    print("so chan")
