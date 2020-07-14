import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

np.random.seed(0)

d1_x = np.zeros(10) + np.random.rand(10)
d1_y = np.zeros(10) + np.random.rand(10)
d1_x = d1_x.reshape(-1, 1)
d1_y = d1_y.reshape(-1, 1)
d1_xy = np.hstack((d1_x, d1_y))

d2_x = np.zeros(10) * -1 - np.random.rand(10)
d2_y = np.zeros(10) + np.random.rand(10)
d2_x = d2_x.reshape(-1, 1)
d2_y = d2_y.reshape(-1, 1)
d2_xy = np.hstack((d2_x, d2_y))

d3_x = np.zeros(10) * -1 - np.random.rand(10)
d3_y = np.zeros(10) * -1 - np.random.rand(10)
d3_x = d3_x.reshape(-1, 1)
d3_y = d3_y.reshape(-1, 1)
d3_xy = np.hstack((d3_x, d3_y))

d4_x = np.zeros(10) + np.random.rand(10)
d4_y = np.zeros(10) * -1 - np.random.rand(10)
d4_x = d4_x.reshape(-1, 1)
d4_y = d4_y.reshape(-1, 1)
d4_xy = np.hstack((d4_x, d4_y))

plt.scatter(d1_x, d1_y, c="red")
plt.scatter(d2_x, d2_y, c="green")
plt.scatter(d3_x, d3_y, c="blue")
plt.scatter(d4_x, d4_y, c="black")
plt.savefig("results/sample.png")
plt.cla()

X = np.concatenate([d1_xy, d2_xy, d3_xy, d4_xy])
Y = np.array([0]*10 + [1]*10 + [2]*10 + [3]*10)

x_train, x_test, y_train, y_test = train_test_split(X, Y)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train, y_train)
pred = clf.predict(x_test)
print(clf.score(x_test, y_test))

for xt, pr in zip(x_test, pred):
    if pr == 0:
        color = "red"
    elif pr == 1:
        color = "green"
    elif pr == 2:
        color = "blue"
    elif pr == 3:
        color = "black"
    plt.scatter(*xt, c=color)

plt.savefig("results/prediction.png")