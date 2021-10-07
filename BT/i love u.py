chuoi = "I LOVEU somuch"
chuoi1 = "I loved you too "
print(chuoi.title())
print(chuoi1.swapcase())
# căn chỉnh lề :
chuoi = "anh yeu em "
print(chuoi.rjust(50," "))

chuoi = "anh yeu be "
print(chuoi.ljust (60,"+"))

chuoi = "v555 YÊU Y747 "
print (chuoi.center (50,"8"))
#khởi tạo list gồm 10 phần tử trong đó các phần tử đều chia hết cho 2

a = [a%2 for a in range(1,21)]
print(a)
#Cho 1 list gồm 4 phần tử
# a. thêm phần tử 4,6,9,8 vào cuối list
# b. Xóa phần tử thứ 4 trong list
# c. Đếm số lượng phần tử có trong list

listt = [5]*4
print(listt)
listt.extend([4,6,9,8])
print(listt)
listt.pop(4)
print(listt)

#
def cmp(a,b):
    return (a > b) - (a < b)
list1 = [100]*5
list2 = [3,6,9,12,16]
if(cmp(list1, list2) < 0):
    print("list 1 lon hon")
else:
    if (cmp(list1,list2) > 0):
        print("list 2 lon hon")
    else:
        print("hai list bằng nhau")
print("Tong list1: ",sum(list1))
print("Tong list2: ",sum(list2))
print("Tong 2 list: ",sum(list1+list2))

