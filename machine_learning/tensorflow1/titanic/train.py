import os
import csv

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

from make_data import make_data


class Convolutional_neural_network:
    def __init__(self):
        # 入力データ
        self.data, self.label, self.test_data, self.passenger_id = make_data()

        # パラメーター
        # バッチサイズ
        self.batch_size = 32
        # 学習回数
        self.train_step = 500
        # 学習中の出力頻度
        self.log_freq = 50
        # ドロップアウト率
        self.prob_1 = 0.2
        self.prob_2 = 0.5
        
        # 入力層
        self.input_size = 7
        # 隠れ層
        self.hidden_size = 32
        # 出力層
        self.output_size = 2

        self.x = tf.placeholder(tf.float32, name='x')
        self.labels = tf.placeholder(tf.float32, name='labels')
        self.p1 = tf.placeholder(1.0, name='p1')
        self.p2 = tf.placeholder(1.0, name='p2')

        self.sess = tf.Session()
        self._make_graph()

    def matmul_plus_bias_with_dropout(self, x, w, b, p):
        return tf.matmul(tf.nn.dropout(x, keep_prob=p), w) + b

    def make_mini_batch(self, data_org, label_org, batch_size=32):
        i = 0
        while True:
            batch_data = data_org[i:i+batch_size]
            batch_label = label_org[i:i+batch_size]

            i += batch_size
            if i > data_org.shape[0] - batch_size:
                i = 0
            
            return batch_data, batch_label

    def _make_graph(self):
        W1 = tf.Variable(tf.zeros([self.input_size ,self.hidden_size]))
        b1 = tf.Variable([0.1] * self.hidden_size)
        l1 = tf.nn.relu(self.matmul_plus_bias_with_dropout(self.x, W1, b1, self.p1))

        W2 = tf.Variable(tf.zeros([self.hidden_size, self.output_size]))
        b2 = tf.Variable([0.1] * self.output_size)
        self.y = tf.nn.softmax(self.matmul_plus_bias_with_dropout(l1, W2, b2, self.p2))

        self.loss = -tf.reduce_sum(self.labels * tf.log(self.y))
    
        self.optimizer = tf.train.AdamOptimizer().minimize(self.loss)

        self.prediction_match = tf.equal(tf.argmax(self.y, axis=1), tf.argmax(self.labels, axis=1))
        self.accuracy = tf.reduce_mean(tf.cast(self.prediction_match, tf.float32), name='accuracy')

    def train(self):
        # 学習の実行
        self.sess.run(tf.global_variables_initializer())
        for i in range(self.train_step):
            batch_x, batch_y = self.make_mini_batch(self.data, self.label, self.batch_size)
            if i % self.log_freq == 0:
                train_accuracy = self.sess.run(self.accuracy, feed_dict={
                    self.x: batch_x, 
                    self.labels: batch_y,  
                    self.p1: 1.0, 
                    self.p2: 1.0
                })
                print('step {:d}, accuracy {:.2f}'.format(i, train_accuracy))
            self.sess.run(self.optimizer, feed_dict={
                self.x: batch_x, 
                self.labels: batch_y, 
                self.p1: self.prob_1, 
                self.p2: self.prob_2, 
            })
    
    def predict(self):
        prediction = self.sess.run(self.y, feed_dict={
            self.x: self.test_data, 
            self.p1: 1.0, 
            self.p2: 1.0, 
        })

        return np.argmax(prediction, axis=1)

    def save_result(self, result):
        os.makedirs("result", exist_ok=True)

        # 提出データをcsv出力
        with open("result/dnn.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["PassengerId", "Survived"])
            for i, p in zip(self.passenger_id, result):
                writer.writerow([i, p])


if __name__ == "__main__":
    n = Convolutional_neural_network()
    n.train()
    result = n.predict()
    n.save_result(result)