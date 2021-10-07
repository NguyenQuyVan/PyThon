string = input('Nhập chuỗi từ bàn phím: ')
count={}
for i in string:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1 
for i in sorted(count, key=count.get, reverse=False):
    print(i, count[i])
