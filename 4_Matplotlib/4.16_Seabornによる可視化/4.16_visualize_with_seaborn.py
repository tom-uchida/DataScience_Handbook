# ----------------------------------
# ----- 4.16 Seabornによる可視化 -----
# ----------------------------------
# Seabornは適切な描画スタイルとデフォルトの配色，
# 一般的な統計プロットに対するシンプルで高水準の関数定義，
# そしてpandas DataFrameとの機能統合を，MatplotlibのAPIとして提供する．





# --------------------------------------
# ----- 4.16.1 Seaborn対Matplotlib -----
# --------------------------------------
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd

# ランダムウォークのデータを作る．
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Matplotlibのデフォルトでプロットする．
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')

# Seabornを使ってプロットする．
import seaborn as sns
sns.set()
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')





# --------------------------------------
# ----- 4.16.2 Seabornプロットの探索 -----
# --------------------------------------
# この後で紹介する例は，すべてMatplotlibを使ってもプロット可能．



# -----------------------------------------
# ----- 4.16.2.1 ヒストグラム，KDE，密度 -----
# -----------------------------------------
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
  plt.hist(data[col], normed=True, alpha=0.5)

# ヒストグラムではなく，Seabornのsns.kdeplotを使ったカーネル密度推定により，
# 分布のなめらかな推定が可能．
for col in 'xy':
  sns.kdeplot(data[col], shade=True)

# distplotを使えば，KDEとヒストグラムを同時に描ける．
sns.distplot(data['x'])
sns.distplot(data['y'])

# 完全な2次元のデータセットをkdeplotに渡せば，2次元の可視化が行われる．
sns.kdeplot(data)

# sns.jointplotを使用して，結合分布と周辺分布を同時に見ることができる．
with sns.axes_style('white'):
  sns.jointplot("x", "y", data, kind='kde')

# jointplotにはその他のパラメータも渡せる．
# 例として，六花系グリッドのヒストグラムをプロットする．
with sns.axes_style('white'):
  sns.jointplot("x", "y", data, kind='hex')

plt.show()



# -------------------------------
# ----- 4.16.2.2 ペアプロット -----
# -------------------------------



# ----------------------------------
# ----- 4.16.2.3 層別ヒストグラム -----
# ----------------------------------



# ------------------------------------
# ----- 4.16.2.4 ファクタープロット -----
# ------------------------------------



# ----------------------------
# ----- 4.16.2.5 結合分布 -----
# ----------------------------



# ----------------------------
# ----- 4.16.2.6 棒グラフ -----
# ----------------------------





# ----------------------------------------------
# ----- 4.16.3 事例：マラソンのゴール時間の調査 -----
# ----------------------------------------------