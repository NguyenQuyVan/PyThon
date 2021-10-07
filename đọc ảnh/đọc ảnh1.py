import matplotlib.pyplot as plt
import matplotlib.image as img

image1 = img.imread("abc1.png.jpg")
image2 = img.imread("abc2.png.jpg")
image3 = img.imread("abc3.jpg.jpg")
image4 = img.imread("abc4.png.jpg")

fig, axs = plt.subplots(2, 2, figsize = (8, 8))

axs[0, 0].imshow(image1)
axs[0, 1].imshow(image2)
axs[1, 0].imshow(image3)
axs[1, 1].imshow(image4)

plt.show()

#Lưu file
plt.savefig('a.png')
plt.savefig('a.pdf')
