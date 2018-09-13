# -------------------------------
# ----- 2.2.1 NumPy配列の属性 -----
# -------------------------------
import numpy as np
np.random.seed(0) # 同じ乱数を得るために，乱数シードを設定する

x1 = mp.random.randint(10, size=6)			# 1次元配列
x2 = mp.random.randint(10, size=(3, 4))		# 2次元配列
x3 = mp.random.randint(10, size=(3, 4, 5))	# 3次元配列

# 各配列には，属性として
#	ndim(次元数)
#	shape(各次元のサイズ)
#	size(配列の合計のサイズ)
#	dtype(配列のデータ型)
# をもつ．
print("x3 ndim: ", x3.ndim)		# x3 ndim: 3
print("x3 shape: ", x3.shape)	# x3 shape: (3, 4, 5)
print("x3 size: ", x3.size)		# x3 size: 60
print("x3 dtype: ", x3.dtype)	# x3 dtype: int64





# -------------------------------------------------
# ----- 2.2.3 配列のスライス：部分配列にアクセスする -----
# -------------------------------------------------
# 配列xのスライスにアクセスするには，次の指定方法を使う．
x[start:stop:step]
# デフォルト値は，start=0，stop=その次元のsize，step=1になる．


# 1次元配列のスライス
x = np.arange(10) 
# → array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x[:5] 	# 最初の5要素
# array([0, 1, 2, 3, 4])

x[5:] 	# 最初の5要素
# array([5, 6, 7, 8, 9])

x[4:7] 	# 中間の部分配列
# array([4, 5, 6])

x[::2] 	# 1つおきの要素
# array([0, 2, 4, 6, 8])

x[1::2] # インデクス1からはじめる1つおきの要素
# array([1, 3, 5, 7, 9])

# 潜在的に混乱するケースは，stepが負の場合．
# この場合，startとstopのデフォルト値が入れ替わる．
# つまり，配列を逆順にする一つの便利な方法となる．
x[::-1] 	# 逆順に全ての要素
# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

x[5::-2] 	# インデクス5から逆順に1つおきの要素
# array([5, 3, 1])


# 多次元配列のスライス
x2
# → array( [[12, 5, 2, 4],
# 		    [7, 6, 8, 8],
# 		    [1, 6, 7, 7]] )

x2[:2, :3] 		# 2行と3列
# array( [[12, 5, 2], 
#         [7, 6, 8]] )

x2[:3, ::2] 	# 3行と，1つおきの列
# array( [[12, 2], 
#         [7, 8],
#		  [1, 7]] )

x2[::-1, ::-1] 	# すべての次元を一度に逆にする
# array( [[7, 7, 6, 1], 
#         [8, 8, 6, 7],
#		  [4, 2, 5, 12]] )


# 配列のアクセスに関して，最も頻繁に行われる操作は，行または列の抽出．
# これは，インデクスと1つのコロンによる空のスライスとの組み合わせで行う．
print(x2[:, 0]) # x2の最初の列
# [12 7 1]

print(x2[0, :]) # x2の最初の行
# [12 5 2 4]

print(x2[0])    # x2の最初の行(x2[0, :]と等価)
# [12 5 2 4]







