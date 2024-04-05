#  viet phuon trinh nhap so nguyen
#  cac so cach nhau bang dau phay (,)
#  ting tong cac so nguyen duong chan
#  dua ket qua ra man hinh
#  vi du: 2,4,6,8,10,-2,-4
#  tong = 30

ipt_str = input("Nhap so nguyen: ")
# ipt_str = "2,4,6,8,10"
ipt_list = ipt_str.split(",")
# ipt_list = ["2","4","6","8","10"]
total = 0
for i in range(0, len(ipt_list)):
    num_str = ipt_list[i] # i = 0 => num_str = "2"
    num = int(num_str) # num = 2
    if num > 0 and num % 2 == 0:
        total += num
print(total)
