dem = 0

dic1 = {}

for i in range(0, 10):
    if i % 2 == 0:
         dic1[dem] =i
         dem += 1
print("số chia hêt cho 2 là",dic1)
for i in range(0, dem):

    if(dic1[i] % 3 == 0):

       print("==> So chia het cho 3 la:", dic1[i])

dic1 = {}

for i in range(1, 21):
    
 dic1[i] = i * i
print(dic1)

