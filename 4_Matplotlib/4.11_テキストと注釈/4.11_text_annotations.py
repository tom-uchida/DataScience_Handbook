# -----------------------------
# ----- 4.11 テキストと注釈 -----
# -----------------------------
# 優れた可視化では，図がストーリーを持ち，読み手を誘導する．
# 場合によってはちょっとしたテキストやラベルなどの手がかりが必要．
# 最も基本的な注釈は軸ラベルとタイトルだが，それ以外にもさまざまなオプションがある．
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd





# -----------------------------------------------
# ----- 4.11.1 事例：米国出生率における休日の影響 -----
# -----------------------------------------------
# データを整形して，結果をプロットする．
births = pd.read_csv('data/births.csv')

quartiles = np.percentile(births['births'], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d')
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
births_by_date.index = [pd.datetime(2012, month, day) for (month, day) in births_by_date.index]

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# このようにデータを示す場合には，特徴のある箇所に注釈を付けて
# 読み手の注意を引くことが有益な場合がある．
# これはplt.text/ax.textを用いて行える．
# このコマンドは，指定したx/y座標にテキストを配置する．
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# プロットにラベルを付ける
style = dict(size=10, color='gray')

ax.text('2012-1-1', 3950, "New Year's Day", **style)
ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
ax.text('2012-9-4', 4850, "Labor Day", ha='center',**style)
ax.text('2012-10-31', 4600, "Halloween", ha='right',**style)
ax.text('2012-11-25', 4450, "Thanksgiving", ha='center',**style)
ax.text('2012-12-25', 3850, "Christmas", ha='right',**style)

# 軸ラベルを追加
ax.set(title='USA births by day of year(1969-1988)', ylabel='average daily births')

# x軸に月のラベルをセンタリングして配置
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))

# ax.textメソッドは，x座標，y座標，文字列に加え，テキストの色，サイズ，スタイル，配置
# などのプロパティを指定するオプションのキーワード引数を取る．
# ここでは，ha='right'とha='center'を使用した．
# haは水平整列(horizontal alignment)の省略形．





# ----------------------------------
# ----- 4.11.2 テキスト位置の変換 -----
# ----------------------------------
# 前の例では，テキスト注釈をデータの位置に固定した．
# 場合によっては，データの位置とは無関係に，テキストを軸または図の中に配置することが望ましい場合がある．
# Matplotlibでは，このために変換(transform)を使用する．
# ax.transData    : データ座標軸に関連付けられた変換
# ax.transAxes    : (軸の次元の単位で)軸に関連付けられた変換
# fig.transFigure : (figureの次元の単位で)figureに関連付けられた変換
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure)

# 軸の範囲を変更すると，transDataの座標だけが影響を受け，他の座標系は固定されたままであることがわかる．
ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)





# ---------------------------
# ----- 4.11.3 矢印と注釈 -----
# ---------------------------
# 単純な矢印は，目盛りとテキストに次ぐ有用な注釈である．
# Matplotlibによる矢印の描画は，思ったよりもすっと難しい作業．
# plt.arrow()メソッドが用意されているが，推奨しない．
# 代わりに，plt.annotate()を使う．
# このメソッドはテキストと矢印を作成し，非常に柔軟な指定が可能．
fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('local minimum', xy=(5*np.pi, -1), xytext=(2, -6),
            arrowprops=dict(arrowstyle="->", connectionstyle="angle3, angleA=0, angleB=-90"))


# 辞書arrowpropsに指定する非常に多数のオプションを通して，矢印のスタイルを制御できる．


plt.show()
# 残念ながらこれらの作業は手作業で調整する必要がある．
# なお，ここで使用したスタイルは決してデータを表示するためのベストプラクティスではなく，
# 単に使用可能なオプションの例を示すためのものです．