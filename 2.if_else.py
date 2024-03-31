# # # If statement

# tuoi = nam_nay - nam_sinh
# if tuoi < 18:
#     print("chua du tuoi")
# if tuoi > 18:
#     print("da du tuoi")

#  nam beu lay dau vao lay so hoc sinh nam va nu trong 1 lop hoc
#  nam beu so sanh so hoc sinh nam va nu
#  neu nam nhieu hon nu, in ra "nam nhieu hon nu"
#  neu nu nhieu hon nam, in ra "nu nhieu hon nam"
#  neu bang nhau, in ra "bang nhau"

# so_hoc_sinh_nam = int(input("so hoc sinh nam: "))
# sohocsinhnu = int(input("so hoc sinh nu: "))
# if so_hoc_sinh_nam < sohocsinhnu:
#     print("so hoc sinh nam it hon so hoc sinh nhu: ")
# elif so_hoc_sinh_nam > sohocsinhnu:
#     print("so hoc sinh nam nhieu hon so hoc sinh nu")
# else:
#     print("so hoc sinh nam bang so hoc sinh nu")


# neu tuoi cua nguoi do nho hon 20, in ra "nguoi do tre"
# nam beu lay dau vao la nam hien tai, va nam sinh cua 1 nguoi,
# nam_hien_tai = int(input("nam hien tai: "))
# namsinhcuamotnguoi = int(input("nam sinh cua mot nguoi: "))
# tuoicuanguoido = nam_hien_tai - namsinhcuamotnguoi
# if tuoicuanguoido > 40:
#     print("nguoi do gia")
# elif tuoicuanguoido < 20:
#     print("nguoi do tre")
# else:
#     print("nguoi do la nguoi trung nien")


# nam beu lay dau vao la 1 so, kiem tra xem so do co phai la so chan hay khong
# neu la so 0, in ra "so 0"
# neu la so chan, in ra "so chan"
# neu la so le, in ra "so le"
# dauvaolamotso = int(input("so: "))
# is_even = (dauvaolamotso % 2 == 0)
# if dauvaolamotso == 0:
#     print("0")
# elif is_even:
#     print("la so chan")
# else:
#     print("la so le")


# neu ban dc buoi sang thi so luong ca ban dc bi chia doi, 5 -> 2.5 => 2, 6 -> 3
# neu ban dc buoi chieu <=5 con thi la cong them ca,
# con neu ban dc buoi chieu >5 con thi la ban duoc
# print so ca con lai la bao nhieu, co the am hoac duong

# vi du: 10
# buoi sang ban dc 13 con: 10 - 6 = 4
# buoi chieu ban dc 7 con: print "het ca de ban"

# vi du: 20
# buoi sang ban dc 3 con: 20 - 1 =  19
# buoi chieu ban dc 5 con: 19 + 5 = 24

# vi du: 7
# buoi sang ban dc 0: 7
# buoi chieu ban dc 7 con: 7-7 = 0

cur_fish = int(input("bac ban hang co bao nhieu con ca: "))
sold_mor_fish = int(input("so ca ban duoc buoi sang: "))
sold_aft_fish = int(input("so ca ban duoc buoi chieu: "))

real_sold_mor_fish = sold_mor_fish // 2

remaining_fish = cur_fish - real_sold_mor_fish 

is_plus_aft_fish = sold_aft_fish <= 5

if is_plus_aft_fish:
    remaining_fish = remaining_fish + sold_aft_fish
else:
    remaining_fish = remaining_fish - sold_aft_fish

print(f"so ca con lai: {remaining_fish}")



# print("so ca con lai: " , so_ca_con_lai)
# print(f"so ca con lai: {so_ca_con_lai}")



