import matplotlib.pyplot as plt

plt.bar([1 ,2 ,4 ,6 ,8],[10,15,20,25,30], label ='BT1',color='black')
plt.bar([21,41,16,28,33],[41,25,31,12,19],label='BT2',color='purple')
plt.legend()
plt. xlabel('Cột số')
plt. ylabel('Cột chiều cao')
plt.title('Kết nối  biểu đồ')
plt.show()

#biểu đồ hình tròn
import numpy as np

import matplotlib.pyplot as mp

data = {
    'Chó': 20,
    'Mèo': 10,
    "Chuột": 50,
    "Heo": 100,
    "Chim": 120,
    "Cá": 70
}
np.pie(list(data.values()), labels=list(data.keys()), autopct='%1.1f%%')
np.title("Thú cưng của tôi")
np.show()

