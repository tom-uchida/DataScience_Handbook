# ---------------------------------------------------
# ----- 2.4 集約：最大，最小，その他データ間にあるもの -----
# ---------------------------------------------------
# 大量のデータに対峙した際，一番最初に行うのはデータの要約統計量を計算すること．
# NumPyには，配列を処理して集計値を高速に計算する関数が提供されている．



# ------------------------------
# ----- 2.4.1 配列を合計する -----
# ------------------------------
# 配列内のすべての要素を合計する．
import numpy as np
L = np.random.random(100)
sum(L)      # Pythonに組み込みのsum関数
np.sum(L)   # NumPyのsum関数





# --------------------------
# ----- 2.4.2 最大と最小 -----
# --------------------------
min(big_array), max(big_array)          # Pythonに組み込みのmin，max関数
np.min(big_array), np.max(big_array)    # NumPyのmin，max関数

# min，max，sumおよびその他いくつかの集約を行うには，
# 配列オブジェクトのメソッドを使用する方が簡単．

# NumPy配列を操作する場合は，可能な限りNumPyの集約関数を使用する．



# ---------------------------------
# ----- 2.4.2.1 多次元配列の集約 -----
# ---------------------------------
M = np.random.random((3, 4))
print(M)
# デフォルトでは，NumPy集約関数は配列全体を集約する．
M.sum()
# 集約関数は，集約を計算する軸を指定するオプションの引数を持つ．
# 例えば，min関数にaxis=0を指定すると，各列内の最小値を見つけることができる．
M.min(axis=0) # 各列内
M.min(axis=1) # 各行内





# -------------------------------------------
# ----- 2.4.3 事例：米国大統領の平均身長は？ -----
# -------------------------------------------
import pandas as pd
data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

# このデータ配列から，さまざまなようやく統計量を計算できる．
print("Mean height        : ", heights.mean())
print("Standard deviation : ", heights.std())
print("Minimum height     : ", heights.min())
print("Maximum height     : ", heights.max())

# 分位数も計算できる．
print("25th percentile : ", np.percentile(heights, 25))
print("Median : ", np.median(heights))
print("75th percentile : ", np.percentile(heights, 75))

import matplotlib.pyplot as plt
import seaborn; seaborn.set(); # set plot style
plt.hist(heights)
plt.title("Height Distribution of US Presidents")
plt.xlabel("height(cm)")
plt.ylabel("number")
plt.show()