#tính, ngày sinh, quê quán, số điện thoại, Facebook)
#Đọc 1 file trên và in ra màn hình 5 dòng cuối cùng.
#(yêu cầu sinh viên lấy theo đúng thông tin của mình).
'''
f = open("/1951065673.txt", "r")
	
content = f.readlines()
length = len(content)
	
for i in range(length-5, length):
	    print(content[i])
'''
#Đọc 1 file, thống kê và in ra tần xuất xuất hiện của tất cả các từ trong file
#in theo thứ tự giảm dần của số lần xuất hiện
'''
f = open("./data.txt", "r")
content = f.readline()
count = {}
for i in content:
	    if i in count:
	        count[i] += 1
	    else:
	        count[i] = 1
	
sorted(count.values(), reverse=True)
	
print(count)
'''
#Nhập một từ điển D có các value là các số nguyên,
#hãy in ra màn hình 3 giá trị value lớn nhất

d = {1:100, 2:50, 3:25, 4:0, 5:101}
sorted(d.values())
for i in range(len(d) - 2, len(d)):
	    del d[i]
print(sorted(d.values(), reverse=False))

