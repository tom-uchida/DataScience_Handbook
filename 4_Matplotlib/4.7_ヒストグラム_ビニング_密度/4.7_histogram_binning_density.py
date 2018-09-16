# ---------------------------------------
# ----- 4.7 ヒストグラム，ビニング，密度 -----
# ---------------------------------------
# 簡単なヒストグラムは，データセットを理解するための最初の重要なステップ．
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')

data = np.random.randn(1000)
# plt.hist(data)


# hist()関数には，計算と表示の両方を調整するためのオプションが数多く用意されている．
# よりカスタマイズされたヒストグラムの例を次に示す．
# plt.hist(data, bins=30, density=True, alpha=0.5, 
#          histtype='stepfilled', color='steelblue', edgecolor='none')

# 異なる分布のヒストグラムを比較する際には，histtype='stepfilled'オプションを使い．
# 透過度alphaを設定すると見やすいグラフになる．
x1 = np.random.normal( 0, 0.8, 1000)
x2 = np.random.normal(-2,   1, 1000)
x3 = np.random.normal( 3,   2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
plt.show()

# 単にヒストグラムの計算だけを行い(つまり，指定されたビン内のポイントの数を数えて)，
# それを表示しないのであれば，np.histogram()関数が利用できる．
counts, bin_edges = np.histogram(data, bins=5)
print(counts)
# [12 190 468 301 29]





# ------------------------------------------
# ----- 4.7.1 2次元のヒストグラムとビニング -----
# ------------------------------------------
# データ列をビンに分割して1次元のヒストグラムを作成するのと同様に，
# 2次元のビンにデータを分割して2次元ヒストグラムを作成することもできる．
# まず，多変量ガウス分布から得られたxおよびy配列のデータを定義する．
mean = [0, 0]
cov  = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T



# ------------------------------------------------
# ----- 4.7.1.1 plt.hist2d：2次元のヒストグラム -----
# ------------------------------------------------



# ---------------------------------------------
# ----- 4.7.1.2 plt.hixbin：六角形のビニング -----
# ---------------------------------------------



# ---------------------------------
# ----- 4.7.1.3 カーネル密度推定 -----
# ---------------------------------