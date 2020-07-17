import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

x = np.arange(100).reshape(-1, 1)
y = np.arange(0, 1000, 10)

noise = np.random.rand(100) * 100
y_noise = y + noise
y_noise = y_noise.reshape(-1, 1)

plt.scatter(x, y_noise, label="train")
plt.xlim(-10, 110)
plt.ylim(-10, 1100)
plt.savefig("results/regressor_data.png")

# 学習データとテストデータに分割
x_train, x_test, y_train, y_test = train_test_split(x, y_noise)

# モデルの定義
reg = KNeighborsRegressor(n_neighbors=3)

# 学習の実施
reg.fit(x_train, y_train)

# 推論
pred = reg.predict(x_test)

plt.scatter(x_test, pred, c="red", label="predict")
plt.legend()
plt.savefig("results/regressor_result.png")