# bài 1Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải
#bội số của 5, nằm trong đoạn A và B (A, B nhập vào từ bàn phím)
'''
def nhap():
    a = int(input("Vui lòng nhập a: "))
    b = int(input("Vui lòng nhập b: "))
    if (a >= b):
        print("Bạn đã nhập sai .nhập lại!! ")
        nhap()
    else:
        j = []
        for i in range(a, b):
            if (i % 7 == 0) and (i % 5 != 0):
                j.append(str(i))
        print(j)
nhap()
'''
#Bài 3
'''
chuoi = input("Nhập chuỗi đầu vào: ")
tu = [tu for tu in chuoi.split(" ")]
print(sorted(tu))
'''
#Cách 2: Có hàm list() hay không cũng được
#print(sorted(list(tu)))

#Cách 3: print(sorted(list(set(tu))))
'''
'''
#Bài 6: Hãy tạo 1 file có tên là: <mã sinh viên>.txt (ví dụ sinh viên có mã sv
#là: 123 thì file cần đọc là: 123.txt). Mỗi thông tin sau trên 1 dòng: Họ tên,
#mã sinh viên, giới tính, ngày sinh, quê quán, số điện thoại). Đọc 1 file trên và
#in ra màn hình 5 dòng cuối cùng. (yêu cầu sinh viên lấy theo đúng thông tin
#của mình).
'''
with open("C:\\Users\\Quy Van\\Desktop\\Learn\\Kiểm Tra\\jax.txt", mode = 'w',
          encoding = 'utf-8') as f:
    f.write("Họ Tên: Nguyen Quy Văn \nMã sinh viên: 1951065673\nGiới tính: Nam\nNgày sinh: 28/2/2001\nQuê quán: TPHCM\nSố điện thoại: 0975398830")
    f.close
with open("C:\\Users\\Quy Van\\Desktop\\Learn\\Kiểm Tra\\jax.txt", mode = 'r',
          encoding = 'utf-8') as f:
    noidung = f.readlines()
    for i in range(len(noidung)):
        if i > len(noidung) - 6:
            print(noidung[i])
    f.close
'''


#Bài 8 : Cho D là từ điển định nghĩa cách đọc các chữ số ở tiếng Anh, hãy in
#ra các value của D theo thứ tự tăng dần
'''
d = {3:'there', 2:'two', 1:'one', 4:'four', 6:'six', 9:'nice', 10:'ten', 5:'five', 7:'seven', 11:'eleven', 8:'eight', 12:'twelve', 15:'fifteen', 17:'seventeen', 20:'twenty', 19:'nineteen', 16:'sixteen', 14:'fourteen'}
print(sorted(d.keys()))
#print(sorted(d.values()))
print(sorted(d.items()))
'''



#Bài 15 Đọc 1 file, tìm và in ra nội dung của dòng dài nhất trong file đó
'''
with open("C:\\Users\\Quy Van\\Desktop\\Learn\\bài tập\\1951065673.txt", mode = 'r',
          encoding = 'utf-8') as f:
    noidung = f.readlines()
    doanDaiNhat = noidung[0]
    for i in range(len(noidung)):
        if len(doanDaiNhat) < len(noidung[i]):
            doanDaiNhat = noidung[i]
    f.close
print(doanDaiNhat)
'''


#Bài 18 Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in
#một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng.
'''
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
#print(len(t) / 2)
print(t[ : int(len(t) / 2)])
print(t[int(len(t) / 2) : ])
'''



#Bài 20 Viết một chương trình để tạo ra và in tuple chứa các số chẵn được
#lấy từ tuple (1,2,3,4,5,6,7,8,9,10).
t = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(t)
for i in range(len(t)):
    if t[i] % 2 == 0:
        print(t[i])

