# 課題

## 禁則事項
`test_main.py` を修正した場合、不正行為があったと見なされ本講義を含む今学期の全ての単位を失う可能性があります。

## 内容
1. <img src="https://latex.codecogs.com/gif.latex?X=\begin{bmatrix}x_1&space;&&space;x_2&space;&&space;\dots&space;&&space;x_N&space;\end{bmatrix}^\top" /> を入力として、
<img src="https://latex.codecogs.com/gif.latex?\Sigma=\dfrac{1}{N}\sum_{n=1}^N&space;(x_n-\mu)&space;(x_n-\mu)^\top" /> を出力する関数 `covariance` を完成させよ。
ただし <img src="https://latex.codecogs.com/gif.latex?\mu&space;=&space;\dfrac{1}{N}\sum_{n=1}^N&space;x_n" /> とし、入出力形式は以下の通りとする。
	- 入力: N x D の `numpy.ndarray` （N: サンプルサイズ、D: 次元）
	- 出力: D x D の `numpy.ndarray`

1. 対称行列 A を入力とし、その固有値からなる `numpy.ndarray` と対応する固有ベクトルからなる `numpy.ndarray` を返す関数 `eig` を完成させよ。ただし入出力は以下の通りとする。
   - 入力: D x D の `numpy.ndarray`
   - 出力:
	 - `eig_val_array`: 長さD の `numpy.ndarray` で、 A の固有値が昇順に並んでいる（小さい固有値がはじめ、大きい固有値が後ろ）。
	 - `eig_vec_array`: D x D の `numpy.ndarray` で、A の固有ベクトルからなる。 `eig_vec_array[:, i]` は `eig_val_array[i]` に対応する長さ1の固有ベクトル。

1. PCA を実行する関数を完成させよ
   - 入力
	 - `X`: N x D の `numpy.ndarray` （N: サンプルサイズ、D: 次元）
	 - `K`: 1 以上D以下の `int`
   - 出力
	 - `Z`: N x K の `numpy.ndarray` （`Z[n, :]`は、PCAを用いて`X[n, :]`をK次元に落としたもの）
	 - `U`: K x D の `numpy.ndarray` （PCAで次元圧縮するときに用いる、D次元ベクトルをK次元ベクトルに変換する行列）

## 実行環境の作り方
`pip3 install -r requirements.txt`

## 実行コマンド
`python3 test_main.py`
