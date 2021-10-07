f = open(r"C:\\Users\\Quy Van\\Desktop\\Learn\\Kiểm Tra\\g.txt", "r", encoding='utf-8')
noidung = f.readlines()
string = 'Cô em má đỏ hồng hồng \nCho anh xin hỏi có chồng hay chưa? \nAnh hỏi thì em xin thưa \nCon em bốn đứa nhưng chưa có chồng.'
str = string.split(" ")
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in sorted(count, key=count.get, reverse=False):
       print(i, count[i])
print(noidung())
'''
print(noidung[1])
print(noidung[2])
print(noidung[3])
