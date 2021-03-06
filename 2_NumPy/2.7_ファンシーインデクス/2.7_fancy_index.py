# ---------------------------------
# ----- 2.7 ファンシーインデクス -----
# ---------------------------------
# ----------------------------------------
# ----- 2.7.1 ファンシーインデクスの調査 -----
# ----------------------------------------
# ファンシーインデクスの概念は単純．
# インデクスの配列を渡して，複数の配列要素に同時にアクセスする．
import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)
# [51 92 14 71 60 20 82 86 74 74]

# この中の3つの要素にアクセスしたい場合，おそらく次の方法を使う．
[x[3], x[7], x[2]]
[71, 86, 14]

# インデクスのリストまたは配列を渡して，同じ結果が得られる．
ind = [3, 7, 4]
x[ind]
# array([71, 86, 60])


# ファンシーインデクスを使うと，
# その結果の形状は元の配列の形状ではなく，
# インデクス配列の形状が反映される．
ind = np.array([[3, 7],
                [4, 5]])
x[ind]
# array([[71, 86],
#        [60, 20]])


# ファンシーインデクスは複数の次元でも機能する．
X = np.arange(12).reshape((3, 4))
X
# array([[0, 1,  2,  3],
#        [4, 5,  6,  7],
#        [8, 9, 10, 11]])

# 標準的なインデクスと同様に，
# 1番目のインデクスは行を参照し，
# 2番目のインデクスは列を参照する．
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]
# array([2, 5, 11])
# 結果の最初の値は，X[0, 2]，2番目の値はX[1, 1]，3番目の値はX[2, 3]


# ファンシーインデクスの結果は，元の配列の形状ではなく，
# ブロードキャストされたインデクスの形状を反映することを常に意識することが重要． 





# -------------------------------------
# ----- 2.7.2 インデクスの組み合わせ -----
# -------------------------------------
# ファンシーインデクスと単純なインデクスを組み合わせる．
X[2, [2, 0, 1]]
# array([10, 8, 9])

# ファンシーインデクスとスライスの組み合わせは次のようになる．
X[1:, [2, 0, 1]]
# array([[ 6, 4, 5],
#        [10, 8, 9]])

# ファンシーインデクスとマスクの組み合わせも可能．
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]
# array([[0,  2],
#        [4,  6],
#        [8, 10]])





# -----------------------------------------
# ----- 2.7.3 事例：ランダムポイントの選択 -----
# -----------------------------------------
# ファンシーインデクスの一般的な使用法の1つが，
# 行列から行のサブセットを選択すること．
# 例えば，2次元正規分布に従うD次元のNポイントを表すN行D列の行列があるとする．
mean = [0, 0]
cov  = [[1, 2],
        [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape
# (100, 2)
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

plt.scatter(X[:, 0], X[:, 1])
plt.show()

# ファンシーインデクスを使用して20のランダムなポイントを選択する．
# これを行うには，最初に重複のない20個のランダムなインデクスを選択し，
# これらのインデクスを使用して元の配列の一部を選択する．
indices = np.random.choice(X.shape[0], 20, replace=False)
indices
# array([93, 45, 73, 81, 50, 10, 98, 94, 4, 64, 65, 89, 47, 84, 82, 
#        80, 25, 90, 63, 20])

selection = X[indices] # ここでファンシーインデクスを使う
selection.shape
# (20, 2)

# どのポイントが選択されたかを確認するために，
# 選択したポイントの位置に大きな円を重ねて表示してみる．
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', s=200, edgecolor='black')
plt.show()





# ------------------------------------------------
# ----- 2.7.4 ファンシーインデクスを使った値の変更 -----
# ------------------------------------------------
# ファンシーインデクスは配列の一部にアクセスするために使用できるように，
# 配列の一部を変更するためにも使用できる．
# 例えば，インデクスの配列があるとして，
# そのインデクスの要素をある値に変更したいとする．
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)
# [ 0 99 99 3 99 5 6 7 99 9]

# この操作では，任意の代入演算子も使用できる．
x[i] -= 10
print(x)
# [ 0 89 89 3 89 5 6 7 89 9]





# ------------------------------------
# ----- 2.7.5 事例：データのビニング -----
# ------------------------------------
# 効率的にデータをビンに分けて，手作業でヒストグラムを作成する．
# 例えば，1000個の値があり，どのビンに属するのかを素早く見つけたいとする．
# ufunc.atを使って次のように計算することができる．
np.random.seed(42)
x = np.random.randn(100)

# 手作業でヒストグラムを作成する
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins) # 各ビン内のデータの数であり，これがヒストグラムになる．

# 各xに対して，適切なビンを選択する
i = np.searchsorted(bins, x)

# それらのビンに1を加える
np.add.at(counts, i, 1)

# 結果をプロットする
plt.plot(bins, counts, linestyle='step')
plt.show()


# 独自に作ったアルゴリズムの方が，NumPyの最適化アルゴリズムより数倍高速．
# というのも，np.histogramは単純な検索とカウントよりもかなり複雑であるため．
# これは，NUmPyのアルゴリズムがより柔軟であり，
# 特にデータ数が多くなるとパフォーマンスが向上するように設計されているから．