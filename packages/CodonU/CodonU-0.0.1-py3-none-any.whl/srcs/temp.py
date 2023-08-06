import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [_x ** 2 for _x in x]
s = [i for i in y]

plt.scatter(x, y, s)
plt.show()
