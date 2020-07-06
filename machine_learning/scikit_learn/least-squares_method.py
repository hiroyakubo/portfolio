"""
scikit learnを用いて最小二乗法をする.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 模擬データの作成.
x = np.arange(5).reshape(-1, 1)
y = np.arange(0, 100, 20)

# yの値にノイズを加える.
noise = np.random.rand(5) * 20
y_noise = y + noise
y_noise = y_noise.reshape(-1, 1)

# 最小二乗法の計算をする.
model = linear_model.LinearRegression()
model.fit(x, y_noise)
print(model.coef_)
print(model.intercept_)

# 近似式
y_appr = model.coef_ * x + model.intercept_

plt.scatter(x, y_noise)
plt.plot(x, y_appr)
plt.xlim([0, 4])
plt.ylim([0, 100])
plt.savefig("./results/least-squares_method.png")