# --------------------------------------------
# ----- 2.3 NumPy配列の計算：ユニバーサル関数 -----
# --------------------------------------------
# NumPy配列の計算は，非常に速くなる可能性もあれば，非常に遅くなる可能性もある．
# 速くするための鍵は，NumPyのユニバーサル関数(ufunc)を使って実装されたベクトル化演算を使用すること．
# この節では，配列要素に対する計算の繰り返しをより効率的に行うため，ufuncの必要性を説明する．



# -------------------------------
# ----- 2.3.1 低速なループ処理 -----
# -------------------------------
# 値の配列があり，それぞれの要素の逆数(reciprocal)を計算したいとする．
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
	output = np.empty(len(values))
	for i in range(len(values))
		output[i] = 1.0 / values[i]

	return output

values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)

# ここでのボトルネックは操作そのものではなく，
# ループの各サイクルでCPythonが行わなければならない型チェックと関数の呼び出しである．
# 逆数が計算されるたびに，Pythonは最初にオブジェクトの型を調べ，
# その型に使用する正しい関数を動的に検索する．
# コンパイルされたコードであるなら，コードが実行される前にこの型が判明しているため，
# 計算は効率的に行われる．





# ----------------------------
# ----- 2.3.2 ufuncの紹介 -----
# ----------------------------
# NumPyのベクトル化演算は，ufuncを使用して実装される．
# ufuncの主な目的は，NumPy配列の各要素に対して繰り返し演算を素早く実行すること．

# ufuncを使ったベクトル化演算は，特に配列のサイズが大きくなるにつれて
# Pythonループを使った実装よりもずっと効率的になる．





# ----------------------------------
# ----- 2.3.3 NumPy ufuncの調査 -----
# ----------------------------------
# ---------------------------
# ----- 2.3.3.1 配列演算 -----
# ---------------------------
x = np.arrange(4)
print("x      = ", x)		# x      = [0 1 2 3]
print("x + 5  = ", x + 5)	# x + 5  = [5 6 7 8]
print("x - 5  = ", x - 5)	# x - 5  = [-5 -4 -3 -2]
print("x * 2  = ", x * 2)	# x * 2  = [0 2 4 6]
print("x / 2  = ", x / 2)	# x / 2  = [0. 0.5 1.0 1.5]
print("x // 2 = ", x // 2)	# x // 2 = [0 0 1 1]

np.add(x, 2)
# array([2, 3, 4, 5])



# -------------------------
# ----- 2.3.3.2 絶対値 -----
# -------------------------
x = np.array([-2, -1, 0, 1, 2])
abs(x)
# array([2, 1, 0, 1, 2])

# NumPy ufuncは，np.absという別名でも使用できるnp.absolute．
np.absolute(x)
# array([2, 1, 0, 1, 2])
np.abs(x)
# array([2, 1, 0, 1, 2])



# ---------------------------
# ----- 2.3.3.3 三角関数 -----
# ---------------------------
# 角度の配列を定義．
theta = np.linspace(0, np.pi, 3)
# これらの値に対して三角関数を計算できる．
print("theta 	  = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))



# -----------------------------------
# ----- 2.3.3.4 指数関数と対数関数 -----
# -----------------------------------
x = [1, 2, 3]
print("x   = ", x)
print("e^x = ", np.exp(x))
print("2^x = ", np.exp2(x))
print("3^x = ", np.power(3, x))

x = [1, 2, 4, 10]
print("x        = ", x)
print("ln(x)    = ", np.log(x))
print("log2(x)  = ", np.log2(x))
print("log10(x) = ", np.log10(3, x))





# ---------------------------------
# ----- 2.3.4 高度なufuncの機能 -----
# ---------------------------------
# ----------------------------
# ----- 2.3.4.1 出力の指定 -----
# ----------------------------
# 一時的な配列を作成するのではなく，すべてのufuncでout引数を指定して
# 計算結果をあるべき場所へ直接書き込むことができる．
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out = y)
print(y)
# [ 0. 10. 20. 30. 40. ]

# これは配列ビューに対しても有効．
# 例えば，指定した配列の要素1つおきに計算結果を書き込むことができる．
y = np.zeros(10)
np.power(2, x, out = y[::2])
print(y)
# [1. 0. 2. 0. 4. 0. 8. 0. 16. 0.]



# -----------------------
# ----- 2.3.4.2 集約 -----
# -----------------------
# add ufuncでreduceを呼び出すと，配列内のすべての要素の合計を計算できる．
x = np.arange(1, 6)
np.add.reduce(x)
# 15

# 中間結果を残したい場合は，代わりにaccumulateを使う．
np.add.accumulate(x)
# array([1, 3, 6, 10, 15])