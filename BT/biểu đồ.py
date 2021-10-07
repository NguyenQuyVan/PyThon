import matplotlib.pyplot as plt

data={'chó':20,'Mèo':50,'chuột':60,'Heo':90,'chim':200,'cá':10}
plt.bar(range(len(data)),list(data.values()))
plt.xticks(range(len(data)),data.keys())
plt.title('thú cưng của tôi')
plt.show()
