# ------------------------------
# ----- 4.10 複数サブプロット -----
# ------------------------------
# この節では，Matplotlibでサブプロットを作成するための4つの機能について説明する．
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np





# ----------------------------------------------------
# ----- 4.10.1 plt.axes：サブプロットのマニュアル作成 -----
# ----------------------------------------------------
# plt.axesメソッドを使用するのが，軸を作成する最も基本的な方法．
# 例えば，x軸とy軸の位置を0.65(つまり，図形の幅の65%と高さの65%から始める)に位置する，
# xとyの範囲を0.2(つまり，軸のサイズは元の幅と高さのそれぞれ20%)とする埋め込みの軸を作成する．
ax_main = plt.axes()
ax_sub  = plt.axes([0.65, 0.65, 0.2, 0.2])

# オブジェクト指向インターフェイスでこのメソッドに相当するのは，fig.add_axes()．
# これを使って縦に積み重ねた2つの軸を作成する．
fig = plt.figure()
ax_upper = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
ax_lower = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax_upper.plot(np.sin(x))
ax_lower.plot(np.cos(x))





# -------------------------------------------------------
# ----- 4.10.2 plt.subplot：サブプロットの単純なグリッド -----
# -------------------------------------------------------
# グリッド内に1つのサブプロットを作成する．
# 例で示すように，このメソッドは行の数，列の数，
# サブプロットのインデクス(左上から右下ヘ順に値を割り当てる)の3つの引数を渡す．
for i in range(1, 7):
  plt.subplot(2, 3, i)
  plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

# plt.subplots_adjust()メソッドを使用して，これらのプロットの間隔を調整できる．
# 次のコードは，オブジェクト指向インターフェイスの等価なメソッドである
# fig.add_subplot()を使用している．
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
  ax = fig.add_subplot(2, 3, i)
  ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

# plt.subplots_adjust()メソッドのhspaceとwspace引数を使用して，
# 図の高さと幅に沿った間隔をサブプロットサイズの単位(この場合，間隔はサブプロットの幅と高さの40%)で指定した．





# --------------------------------------------------------
# ----- 4.10.3 plt.subplots：グリッド全体を一度に作成する -----
# --------------------------------------------------------
# plt.subplots()関数は，単一のサブプロットを作成するのではなく，
# 一回の呼び出しでサブプロットのグリッドを作成し，NumPy配列として返す．
# 引数は，行数と列数，およびオプションのキーワード引数sharexとsharey．
# これらを使って，軸と軸の間の関係を指定できる．
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')

# メソッドの戻り値として得られるaxはNumPy配列として返され，
# 標準の配列インデクス表記を使用して目的の軸を指定できる．
for i in range(2):
  for j in range(3):
    # axは2次元配列として[行, 列]で指定可能
    ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')





# --------------------------------------------
# ----- 4.10.4 plt.GridSpec：より複雑な配置 -----
# --------------------------------------------
# 単純なグリッドではなく，複数の行や列にまたがるサブプロットを作るには，plt.GridSpec()が最適なツール．
# plt.GridSpec()オブジェクトを作成しただけではプロットを描画しない．
# これはplt.subplot()が認識する単なるインターフェイス．

# 例えば，幅と高さを指定した2行3列のグリッドのgridspecは，次のように作成する．
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])


# こうした柔軟なグリッド配置には，さまざまな用途がある．
# 筆者は，次に示すような多軸ヒストグラムを作成するときに使用する．
# 正規分布データを作成
mean = [0, 0]
cov  = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# gridspaceによる軸配列を作成
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# 主軸に散布図をプロット
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# 付随するヒストグラムをプロット
x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical', color='gray')
x_hist.invert_yaxis()
y_hist.hist(y, 40, histtype='stepfilled', orientation='horizontal', color='gray')
y_hist.invert_xaxis()

plt.show()

# 余白に分布を描くこのタイプのプロットはよく使用されるため，
# Seabornライブラリに専用のAPIがある．