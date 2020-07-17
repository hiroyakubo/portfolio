"""
kaggleのタイタニック号のデータをSVMを使って分類.
"""

import os
import csv

import numpy as np
from sklearn import model_selection, svm, metrics

from make_data import make_data

# データのインポート
data, label, test_data, passenger_id = make_data()

# 学習データ、テストデータの数
train_size = 650
test_size = 62

# 学習データ、テストデータを分割
data_train, data_test, label_train, label_test = model_selection.train_test_split(data, label, test_size=test_size, train_size=train_size)

# モデルの定義
clf = svm.SVC()

# 学習の実施
clf.fit(data_train, label_train)

# 推論の実施
pred = clf.predict(data_test)

# 正解率を算出
ac_score = metrics.accuracy_score(label_test, pred)
print(ac_score)

# kaggle提出用データを推論
test_prediction = clf.predict(test_data)
print(test_prediction)

os.makedirs("result", exist_ok=True)

# 提出データをcsv出力
with open("result/svm.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["PassengerId", "Survived"])
    for i, p in zip(passenger_id, test_prediction):
        writer.writerow([i, p])