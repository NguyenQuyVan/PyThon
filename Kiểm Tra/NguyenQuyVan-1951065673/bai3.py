#a
'''
tuple = (11,12,13,14,15,16,17,18,19,20)
t1 = ();
for i in tuple:
 if i % 2 == 1:
     t1=t1+(i,);
print (t1)
'''
#b
import matplotlib.pyplot as plt
import matplotlib.image as img

image1 = img.imread("abc1.png.jpg")
fig, axs = plt.subplots(2, 2, figsize = (128, 128))
axs[0, 0].imshow(image1)

plt.savefig('a.png')
plt.savefig('a.pdf')
