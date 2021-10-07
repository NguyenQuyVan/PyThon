a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))
c = int(input("Nhap gia tri c: "))

max = a;
if (max < b):
	max = b;

if (max < c):
	max = c;

print("==> gia tri lon nhất là: ",max)