ten_nguoi = input("Nhap ten cua mot nguoi: ")
chu_cai = input("nhap chu cai: ")
vi_tri = ten_nguoi.index(chu_cai) + 1
if chu_cai in ten_nguoi:
    print("chu cai hien o vi tri thu: ", vi_tri)
else:
    print("chu cai hien khong co trong ten nguoi")