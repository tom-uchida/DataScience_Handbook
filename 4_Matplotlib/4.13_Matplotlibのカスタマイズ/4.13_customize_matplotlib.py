# ---------------------------------------------------------
# ----- 4.13 Matplotlibのカスタマイズ：設定とスタイルシート -----
# ---------------------------------------------------------
# ------------------------------------
# ----- 4.13.1 手作業でカスタマイズ -----
# ------------------------------------
# この章では，プロットそれぞれの設定を微調整してデフォルトよりも見栄えを良くする方法をみていく．
# 例えば，次のようなありふれたヒストグラムで考えてみる．
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.random.randn(1000)
plt.hist(x)

# これを手作業で修正し，見た目に優れたプロットに変更する．
# ①背景をグレーに変更する．
ax = plt.axes(facecolor='#E6E6E6')
ax.set_axisbelow(True)

# ②グリッド(grid)線を白の実線に
plt.grid(color='w', linestyle='solid')

# ③枠線(spine)を非表示
for spine in ax.spines.values():
  spine.set_visible(False)

# ④上と右の目盛りを非表示
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# ⑤目盛りとラベルを明るいい色に設定．
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
  tick.set_color('gray')
for tick in ax.get_yticklabels():
  tick.set_color('gray')

# ⑥ヒストグラムの面と境界の色を設定
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666')

# ここに至るまでに多くの努力を払ったが，これをプロットを作成するたびに毎回行う気にはならない．
# この調整を一度行えば，すべてのプロットで有効にする方法がある．





# ------------------------------------------
# ----- 4.13.2 デフォルトの変更：rcParams -----
# ------------------------------------------
# Matplotlibがロードされるたびに実行時設定(rc:runtime configuration)
# が読み込まれ，すべてのプロット要素のデフォルトスタイルが定義される．
# この設定は，plt.rc関数を使用していつでも変更できる．
# 現在のセッションで行う変更を簡単に元に戻せるように，最初にrcParams辞書のコピーを保存する．
default = plt.rcParams.copy()

from matplotlib import cycler
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
plt.hist(x)

# このrc設定を使うと，単純な線グラフがどのように表示されるかを見てみる．
for i in range(4):
  plt.plot(np.random.rand(10))

# この設定は，.matplotlibrcファイルに保存することができる．
# 詳しくは，Matplotlibのドキュメントを参照．
# http://matplotlib.org/users/customizing.html
# とは言うものの，スタイルシートを使ってMatplotlibをカスタマイズする方法を筆者は好んで使用している．





# -------------------------------
# ----- 4.13.3 スタイルシート -----
# -------------------------------
# 独自のスタイルを作成しなくても，デフォルトのスタイルシートが十分に役に立つ．
# 利用可能なスタイルの一覧がplt.style.available
# スタイルシートの切り替えは，基本的に次のように行う．
# plt.style.use('stylename')
# しかし，これ以後すべてのスタイルが変更されてしまうことに注意が必要．
# スタイルを一時的に設定するなら，スタイル・コンテキスト・マネージャを使用する．
# with plt.style.context('stylename')
#    make_a_plot()

# 簡単な2つのプロットを作成する関数を作る．
def hist_and_lines():
  np.random.seed(0)
  fig, ax = plt.subplots(1, 2, figsize=(11, 4))

  # ヒストグラム
  ax[0].hist(np.random.randn(1000))

  # 折れ線
  for i in range(3):
    ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')



# ------------------------------------
# ----- 4.13.3.1 デフォルトスタイル -----
# ------------------------------------
# ランタイム設定をデフォルトの設定に戻してみる．
plt.rcParams.update(default)
hist_and_lines()



# -------------------------------------------
# ----- 4.13.3.2 FiveThirtyEightスタイル -----
# -------------------------------------------
# FiveThirtyEightは，はっきりした色使い，太い線，薄い軸に特徴がある．
with plt.style.context('fivethirtyeight'):
  hist_and_lines()



# ---------------------------
# ----- 4.13.3.3 ggplot -----
# ---------------------------
# ggplotパッケージは，非常に人気のあるR言語の可視化ツール．
with plt.style.context('ggplot'):
  hist_and_lines()



# --------------------------------------------------------
# ----- 4.13.3.4 ハッカーのためのベイジアンメソッドスタイル -----
# --------------------------------------------------------
with plt.style.context('bmh'):
  hist_and_lines()



# ----------------------------------
# ----- 4.13.3.5 暗い背景スタイル -----
# ----------------------------------
# プレゼンで使用する図は，明るい背景よりも暗い背景のほうが適していることがある．
with plt.style.context('dark_background'):
  hist_and_lines()



# ---------------------------------
# ----- 4.13.3.6 グレースケール -----
# ---------------------------------
# 時には，白黒印刷のための図を用意するかもしれない．
with plt.style.context('grayscale'):
  hist_and_lines()



# -----------------------------------
# ----- 4.13.3.7 Seabornスタイル -----
# -----------------------------------
import seaborn
hist_and_lines()

plt.show()