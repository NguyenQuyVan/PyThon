import time
password = "04022001"
passw = ""
while passw != password:
    passw =input("Nhập ngày sinh của Bé Yêu: ")
    if passw != password:
        print("mày nhập sai kìa :(( \n")
    else :
        print("*******--------------------------------------------------****")
    
for i in range(0,109,10):
    print("Vui lòng chờ...đang tải..." + str(i)+ "%")
    time.sleep(0.4)
print("\n bạn đã nhập thành công \n")

with open("data.txt","r") as file:
    line =file.read()

for x in line:
    print(x,end = "")
    #time.sleep(0.000000000000000000000000000000000000000000000000000000000001)
