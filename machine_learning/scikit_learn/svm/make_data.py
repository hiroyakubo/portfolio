import os

import numpy as np
import pandas as pd

def make_data(data_dir="../data/titanic/", csv_list = ["train.csv", "test.csv"]):
    """
    タイタニック号データの前処理スクリプト.

    Args: 
        data_dir:   str
                    学習データおよびテストデータが入ったディレクトリへのパス
        csv_list:   list
                    学習データおよびテストデータのcsvファイル名

    Returns: 
        学習データ、教師データ、テストデータ
    """
    input_list = []
    for c in csv_list:
        data_file = os.path.join(data_dir, c)
        df = pd.read_csv(data_file)
        
        # if c = "train.csv":
        #     # 欠損値がある行を削除.
        #     df = df.dropna().dropna()
        # else:
        # 欠損値の処理
        df["Age"] = df["Age"].fillna(df["Age"].median())
        df["Embarked"] = df["Embarked"].fillna("S")
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())
        
        # 各種データを数値化する.
        df["Sex"][df["Sex"] == "male"] = 0
        df["Sex"][df["Sex"] == "female"] = 1
        df["Embarked"][df["Embarked"] == "S" ] = 0
        df["Embarked"][df["Embarked"] == "C" ] = 1
        df["Embarked"][df["Embarked"] == "Q"] = 2

        if c == "test.csv":
            passenger_id = df["PassengerId"]
        
        # 不要な列を削除.
        del df["PassengerId"]
        del df["Name"]
        del df["Ticket"]
        del df["Cabin"]

        # 学習データは教師データを抽出.
        if c == "train.csv":
            df_label = df["Survived"]
            del df["Survived"]
            label_arr = df_label.values

        # df -> ndarrayの変換を行い、正規化.
        input_arr = df.values
        input_arr[:, 0] = input_arr[:, 0] / 3
        input_arr[:, 2] = input_arr[:, 2] / 100
        input_arr[:, 5] = input_arr[:, 5] / 513
        input_arr[:, 6] = input_arr[:, 6] / 2

        input_list.append(input_arr)

    return input_list[0], label_arr, input_list[1], passenger_id

if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf)
    i, l, t, p = make_data()
    print(i.shape)
    print(l.shape)
    print(t.shape)
    print(p.shape)