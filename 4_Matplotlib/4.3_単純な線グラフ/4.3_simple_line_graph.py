# ----------------------------
# ----- 4.3 単純な線グラフ -----
# ----------------------------
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# すべてのプロットに対して，図(figure)と座標軸(axes)の作成を最初に行う．
fig = plt.figure()
ax = plt.axes()

# axesを作成したら，ax.plot関数を使用してデータをプロットすることができる．
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
# plt.plot(x, np.sin(x))

# 1つのFigureに複数の線を描きたい場合には，単にplot関数を複数回呼び出す．
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))





# ---------------------------------------------
# ----- 4.3.1 プロットの制御：線の色とスタイル -----
# ---------------------------------------------
plt.plot(x, np.sin(x - 0), color='blue')            # 色の名前で指定
plt.plot(x, np.sin(x - 1), color='g')               # カラーコード(rgbcmyk)による指定
plt.plot(x, np.sin(x - 2), color='0.75')            # 0から1の間のグレースケールを指定
plt.plot(x, np.sin(x - 3), color='#FFDD44')         # 16進コードで指定(RRGGBBを00からFFで表す)
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))   # 0から1のRGB値をダブルで指定
plt.plot(x, np.sin(x - 5), color='chartreuse')      # サポートされているHTMLカラーネームで指定

# 同様に，linestyleキーワードを使用して線のスタイルを調整することもできる．
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')

plt.plot(x, x + 4, linestyle='-')   # 直線
plt.plot(x, x + 5, linestyle='--')  # 破線
plt.plot(x, x + 6, linestyle='-.')  # 一点鎖線
plt.plot(x, x + 7, linestyle=':')   # 点線





# -----------------------------------------
# ----- 4.3.2 プロットの制御：座標軸の範囲 -----
# -----------------------------------------
# Matplotlibは軸の範囲を自動的かつ最適に選択するが，場合によっては細かく制御したい場合がある．
# 軸の範囲を調整する最も基本的な方法は，plt.xlim()とplt.ylim()メソッドを使用すること．
plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# 関連する有用な関数にplt.axis()がある．
# plt.axis()メソッドに[xmin, xmax, ymin, ymax]を指定するリストを渡すことで，
# xとyの範囲を1回の呼び出しで設定できる．
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])

# plt.axis()のさらに有益な使い方として，
# 現在のプロット周辺の境界を自動的に狭く(tight)することができる．
plt.plot(x, np.sin(x))
plt.axis('tight')

# 画面上でx軸とy軸が同じ比率となるように，
# アスペクト比を等しくするなどの高度な機能も提供している．
plt.plot(x, np.sin(x))
plt.axis('equal')





# ------------------------------------
# ----- 4.3.3 プロットへのラベル付け -----
# ------------------------------------
# タイトルと軸のラベルは最も簡単なラベル．
# ラベルを素早く設定するためのメソッドが用意されている．
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
pkt.xlabel("x")
pkt.ylabel("sin(x)")

# 凡例(legend)を付加してそれぞれの線にラベルを付けるとわかりやすくなる．
# plot関数のlabelキーワードを使用して，それぞれの線にラベルを指定するのが最も簡単．
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.sin(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend()
plt.show()
# plt.legend()メソッドは，線のスタイルと色を記憶し，正しいラベル付けを行う．