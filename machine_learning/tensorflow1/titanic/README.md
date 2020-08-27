# kaggle タイタニック号

## 手順
```
docker build -t tensorflow-1.14 .
```
```
docker run --gpus all -it --rm -v {local}:{container} tensorflow-1.14
```

## 結果
![result](image/result.png)