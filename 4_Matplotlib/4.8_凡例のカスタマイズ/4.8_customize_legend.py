# -------------------------------
# ----- 4.8 凡例のカスタマイズ -----
# -------------------------------
# ここでは，Matplotlibの凡例の配置と見た目をカスタマイズする方法を取り上げる．
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# 凡例のカスタマイズ法はさまざま．
# 例えば，位置を指定して枠線(frame)を消すことができる．
ax.legend(loc='upper left', frameon=False)

# ncolパラメータを使って，凡例の列数を指定できる．
ax.legend(frameon=False, loc='lower center', ncol=2)

# 角丸(fancybox)を使用する，影をつける，フレームの透明度(alpha値)を上げる．
# テキストの周囲の余白を変更することも可能．
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)





# ------------------------------
# ----- 4.8.1 凡例要素の選択 -----
# ------------------------------
# plt.plot()メソッドは，一度に複数の線を作成し，作成した線インスタンスのリストを返す．
# これらのいずれかをラベル指定と共にplt.legend()に渡すと，その線インスタンスの凡例が表示される．
y = np.sin( x[:,np.newaxis] + np.pi * np.arange(0, 2, 0.5) )
lines = plt.plot(x, y)

plt.legend(lines[:2], ['first', 'second'])

# 実際には，凡例に表示するプロット要素に対してラベルを付与しておくという，
# 最初の方法を使用するほうが明快．
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True)
# デフォルトでは，ラベル属性が設定されていないすべての要素は凡例に表示されない．





# ------------------------------
# ----- 4.8.2 点サイズの凡例 -----
# ------------------------------
# 時には，デフォルトの凡例では不十分な場合もある．
# 例えば，データの特徴を点の大きさで示すとして，その凡例を作成する．
import pandas as pd
cities = pd.read_csv('data/california_cities.csv')

# 着目しているデータを抜き出す
lat, lon = cities['latd'], cities['longd'] # 経度，緯度
population, area = cities['population_total'], cities['area_total_km2'] # 人口，面積

# 各地点に色と大きさを指定した散布図をプロットする．ラベルは付与しない．
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# ここで，凡例を加える
# 点の大きさとラベルを指定した上で，空のリストをプロットする．
for area in [100, 300, 500]:
  plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + ' km$^2$')
  plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')

plt.title('California Cities: Area and Population')

# 凡例は常にプロットされたオブジェクトを参照するので，
# 特定の図形を表示するにはプロットしなけれならない．
# この例では，必要とするオブジェクト(灰色の円)はプロット上にないので，
# 空のリストをプロットしてそれらを仮に作る．
# 凡例は，ラベルが指定されたプロット要素のみを表示することにも注意．

# 空のリストをプロットすることで，凡例として選ばれるラベル付きのプロットオブジェクトを作成する．
# これにより，凡例は必要とする情報を示すようになった．





# --------------------------
# ----- 4.8.3 複数の凡例 -----
# --------------------------
# プロットのデザイン上，1つの軸に対して複数の凡例が必要となる場合がある．
# 残念ながら，Matplotlibでは簡単に実現できない．
# 標準の凡例インターフェースでは，プロット全体に対して1つの凡例しか作成できないため．

# これを解決するには，新しい凡例を作成し，低レベルインターフェースである
# ax.add_artist()メソッドを使用して2つ目のartistとして手作業でプロットに追加する．
fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
  lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')

ax.axis('equal')

# 1つ目の凡例の行とラベルを追加する
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)

# 2つ目の凡例を生成し，そのartistインスタンスを手動で追加する
from matplotlib.legend import Legend
leg = Legend(ax, lines[:2], ['line C', 'line D'], loc='lower right', frameon=False)
ax.add_artist(leg)

plt.show()