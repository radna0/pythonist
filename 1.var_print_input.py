# # # Variable Declaration

# String
name = "Nam beu"
# bien bi thay doi dc
# var [bien] = "Nam beu"
name = "Huy beu"


name1 = "bach"

name2 = "beu"
new_name = name1 + " " + name2

# print(new_name)

# print("My name: ", name)

# print(f"Hello {name1} {name2}")

# Number
number = 1
new_number = number + 1


number = 1
number += 2  # number = number + 2
# number +=, -=, *=, /=, %=


number = 11
number %= 2  # number = number % 2

# Floats
fl = 1.5
# print(fl)
fl = 1.5 + 2.55
# print(fl)

# inf = float("inf")
inf = float("inf")
neg_inf = float("-inf")
# print(inf)

# print(fl > 1)
# print(fl < 10)
# print(fl > inf)
# print(999999999999999 == inf)
# print(inf < neg_inf)


# Boolean
is_true = True
is_false = False

# print(is_true)
# print(is_false)

is_Even = 2 == 2
# print(is_Even)

# None
empty = None

error = None


# lay thong tin nam beu
name = "Nam beu"
age = 15
height = 1.7


# Input

# x = input("Enter a one-digit number: ")
x = "32"
type_x = type(x)
# print(type_x)
# print(type(x))

length_x = len(x)
# print(length_x)

if length_x != 1:
    x = int(x)
    # print("x is an integer")
    # print("is equal 5: ", x == 5)

# tinh so_tuoi_hien_tai = nam_hien_tai - nam_sinh
nam_nay = 2024
str_nam_sinh = input("nam sinh: ")
nam_sinh = int(str_nam_sinh)

tuoi = nam_nay - nam_sinh
if tuoi < 18:
    print("chua du tuoi")
if tuoi > 18:
    print("da du tuoi")

