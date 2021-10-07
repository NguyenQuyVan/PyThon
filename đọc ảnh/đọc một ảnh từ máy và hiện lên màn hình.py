import matplotlib.pyplot as plt
import matplotlib.image as Ima

image =Ima.imread("abc1.png.jpg")
fig, axs = plt.subplots(2,2,figsize = (8,8))
axs[0,0].imshow(image)
axs[0,1].imshow(image)
axs[1,0].imshow(image)
axs[1,1].imshow(image)
plt.show()
#lưu file
plt.savefig('a.png')
plt.savefig('a.pdf')

#hiện số ngẫu nhiên lên màn hình
import pandas as pd
import numpy as np

S= pd.Series(np.random.randint(500, size=10))

print(S)
print(S.index)
print(S.values)

#
'''
import pandas as pd
import numpy as np

chi_so = ["chó","mèo ","chuột","heo","chim","cá"]

gia_tri = [20,10,50,100,8,60]

S= pd.Series(gia_tri, index = chi_so)

print(S)
print(S.index)
print(S.values)
'''
