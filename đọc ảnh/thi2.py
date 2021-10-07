t = tuple()
for i in range(1,1000):
    dem = 0;
    for j in range(1,i+1):
        if(i%j == 0):
            dem = dem + 1
#dem =2 chia hết cho 1 và chính nó
    if(dem == 2):
        t=t+(i,)
print(t)
