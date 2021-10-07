for i in range (1,101):
 if i % 3 == 0:
  print (i)

# xuất các chử trong note pad
f = open(r"C:\Users\admin\Desktop\word and learn\Python 3.9\bài tập\a.txt", "w", encoding='utf-8')
str = 'Công cha như núi Thái Sơn\nNghĩa mẹ như nước trong nguồn chảy ra\nMột lòng thờ mẹ, kính cha\ncho tròn chữ hiếu mới là đạo con.'
         
f.write(str)
         
f.close()
         
f = open(r"C:\Users\admin\Desktop\word and learn\Python 3.9\bài tập\a.txt", "r", encoding='utf-8')
         
noidung = f.readlines()
         
print(noidung[1])
print(noidung[3])
