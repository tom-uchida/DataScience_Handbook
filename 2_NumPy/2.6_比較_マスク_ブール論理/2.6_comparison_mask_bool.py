# ------------------------------------
# ----- 2.6 比較，マスク，ブール論理 -----
# ------------------------------------
# ------------------------------
# ----- 2.6.1 事例：雨天日数 -----
# ------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254 # convert 1/10mm to inches
inches.shape
# (365,)

plt.hist(inches, 40)
plt.show()



# --------------------------------
# ----- 2.6.1.1 データの深掘り -----
# --------------------------------
# NumPyのufuncをループの代わりに使用して配列に対する要素ごとの算術演算を高速に行うことができる．
# 同様に，別のufuncを使用して配列に対する要素ごとの比較を行い，その結果に操作を施す．





# ---------------------------------
# ----- 2.6.2 ufuncの比較演算子 -----
# ---------------------------------
# 比較演算子の結果は，常にブール型の配列．
x = np.array([1, 2, 3, 4, 5])

x < 3 # less than (np.less)
# array([ True, True, False, False, False], dtype=bool)

x > 3 # greater than (np.greater)
# array([ False, False, False, True, True], dtype=bool)

x <= 3 # less than or equal (np.less_equal)
x >= 3 # greater than or equal (np.greater_equal)
x != 3 # not equal (np.not_equal)
x == 3 # equal (np.equal)

# 2つの配列を要素ごとに比較したり，式を組み合わせることもできる．
(2*x) == (x**2)
# array([False, True, False, False, False], dtype=bool)

# 算術演算子の場合と同様に，比較演算子もufuncとして実装されている．
# 例えば，x < 3と書くと，内部でNumPyはnp.less(x, 3)を使用する．





# ---------------------------------
# ----- 2.6.3 ブール値配列の操作 -----
# ---------------------------------
# ブール値配列を与えると実行できる便利な操作が多数ある．
# 先に作成した2次元配列xを使って例を示す．
print(x)
# [[5 0 3 3]
#  [7 9 3 5]
#  [2 4 7 6]]



# --------------------------------
# ----- 2.6.3.1 要素のカウント -----
# --------------------------------
# ブール値配列のTrueエントリの数を数えるためには，np.count_nonzeroを使う．
np.count_nonzero(x < 6) # 6より小さい値の個数
# 8

# 値の一部またはすべてがTrueであるかどうかを素早く確認したい場合は，
# np.any()またはnp.all()を使用する．
np.any(x > 8) # 8より大きい値の有無
# True

np.any(x < 0) # 0より小さい値の有無
# False

np.all(x < 10) # すべての値が10より小さいか
# True

np.all(x == 6) # すべての値が6と等しいか
# False

# 特定の軸に沿ってnp.all()とnp.any()を使用することもできる．
np.all(x < 8, axis=1) # 各行ごとにすべての値が8より小さいか
# array([ True, False, True], dtype=bool)



# ------------------------------
# ----- 2.6.3.2 ブール演算子 -----
# ------------------------------
# マスキングと集約を組み合わせて計算できる結果のいくつかを以下に示す．
print("Number days without rain       : ", np.sum(inches == 0))
print("Number days wit rain           : ", np.sum(inches != 0))
print("Days with more than 0.5 inches : ", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches   : ", np.sum( (inches > 0) & (inches < 0.2) )
# Number days without rain       : 215 # 降雨のなかった日数
# Number days wit rain           : 150 # 降雨のあった日数
# Days with more than 0.5 inches : 37  # 0.5インチ以上の降水量があった日数
# Rainy days with < 0.1 inches   : 75  # 降水量が0.1未満の日数





# -----------------------------------------
# ----- 2.6.4 マスクとしてのブール演値配列 -----
# -----------------------------------------
# 前の節では，ブール値配列を直接計算して集約値を求めた．
# より強力なパターンは，ブール値配列をマスクとして使用して．
# データ自体の特定のサブセットを選択すること．
# 先に作成した配列の中で，例えば5より小さい値だけを含む配列が必要であるとする．
x
# array([[5, 0, 3, 3],
#        [7, 9, 3, 5],
#        [2, 4, 7, 6]])

# 既に見たように，この条件のブール値配列を得るのは簡単．
x < 5
# array([[False,  True,  True,  True],
#        [False, False,  True, False],
#        [ True,  True, False, False]])

# ここで配列からこれらの値を選択するには，
# このブール値配列をインデクスとして指定すればよい．
# これは，マスキング操作として知られている．
x[x < 5]
# array([0, 3, 3, 3, 2, 4]) # 5より小さい値だけを含む配列

# この条件を満たす1次元配列が返される．
# つまり，マスク配列がTrueの位置にあるすべての値が得られる．
# この後，これらの値を自由に操作できる．

# 例えば，シアトル市の降水量に関する統計量を計算してみる．
# 降雨日すべてのマスクを作る
rainy = (inches > 0) 

# 夏季を表すマスクを作る(6月21日は172日目)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

print("Median precip on rainy days in 2014 (inches)    : ", np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches)   : ", np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches)  : ", np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches) : ", np.median(inches[rainy & ~summer]))
# Median precip on rainy days in 2014 (inches)    : 0.194881889764 # 2014年における降雨日の降水量中央値(インチ)
# Median precip on summer days in 2014 (inches)   : 0.0            # 2014年における夏季の降水量中央値(インチ)
# Maximum precip on summer days in 2014 (inches)  : 0.850393700787 # 2014年における夏季の最大降水量(インチ)
# Median precip on non-summer rainy days (inches) : 0.200787401575 # 2014年における夏季以外の日の降水量中央値(インチ)

# andとorはオブジェクト全体に対して1つの真偽値を評価する場合に使用し，
# &と|はオブジェクトの内容(それぞれのビットやバイト)に対する複数の真偽値を評価する場合に使用する．
# NumPy配列に対するブール式の評価に適しているのは，ほぼ常に後者．