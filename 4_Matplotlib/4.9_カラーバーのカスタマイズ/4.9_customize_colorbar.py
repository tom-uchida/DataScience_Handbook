# ------------------------------------
# ----- 4.9 カラーバーのカスタマイズ -----
# ------------------------------------
# 凡例は離散的な点の離散的なラベルを識別するために使用される．
# 点，線，領域などの色に基づく連続的なラベルが必要な場合，カラーバーは素晴らしいツールとなる．
# Matplotlibにおいて，カラーバーはプロット内の色の意味を示すための軸となる．

# 最も単純なカラーバーはplt.colorbar()メソッドで作成できる．
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

#plt.imshow(I)
#plt.colorbar()





# --------------------------------------
# ----- 4.9.1 カラーバーのカスタマイズ -----
# --------------------------------------
# 描画関数に対してcmap引数を使用して，カラーマップ(colormap)を指定できる．
#plt.imshow(I, cmap='gray')



# -----------------------------------
# ----- 4.9.1.1 カラーマップの選択 -----
# -----------------------------------
# 「よりよい図のための10の簡単なルール」(Ten Simple Rules for Better Figures)
#   https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833
# 「Matplotlibのオンラインドキュメント」
#   https://matplotlib.org/1.4.1/users/colormaps.html

# まず，カラーマップの3つのカテゴリに注意する必要がある．
# 1. 順次的カラーマップ
#    段階的に変化する一連の色で構成される（例えば，binaryまたはviridis）
# 2. 発散的カラーマップ
#    平均からの正および負の偏差を示す2つの異なる色から構成される（例えば，RdBuまたはPuOr）
# 3. 定性的カラーマップ
#    特定の色の変化を伴わない混合色で構成される（例えば，rainbowまたはjet）

# Matplotlibバージョン2.0以前のデフォルトであったjetカラーマップは，定性的カラーマップの一例．
# 定性的カラーマップは通常，値が増すに連れて輝度が一定の増加をしないという点に問題がある．
# jetカラーバーを，グレースケールカラーバーに変換することで，この問題点がわかりやすくなる．
from matplotlib.colors import LinearSegmentedColormap

def grayscale_cmap(cmap):
  # 渡されたカラーマップのグレースケール版を返す
  cmap = plt.cm.get_cmap(cmap)
  colors = cmap(np.arange(cmap.N))

  # RGBAを知覚輝度に変換する
  # http://alienryderflex.com/hsp.html
  RGB_weight = [0.299, 0.587, 0.114]
  luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
  colors[:, :3] = luminance[:, np.newaxis]

  return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)

def view_colormap(cmap):
  # カラーマップをグレースケール版と並べて表示する
  cmap = plt.cm.get_cmap(cmap)
  colors = cmap(np.arange(cmap.N))

  cmap = grayscale_cmap(cmap)
  grayscale = cmap(np.arange(cmap.N))

  fig, ax = plt.subplots(2, figsize=(6, 2), subplot_kw=dict(xticks=[], yticks=[]))
  ax[0].imshow([colors], extent=[0, 10, 0, 1])
  ax[1].imshow([grayscale], extent=[0, 10, 0, 1])


# viridisは，範囲全体に渡って均一な輝度変化を持つように特別に構成されている．
# そのため，色の認識だけでなく，グレースケールでの印刷にもうまく対応する．
#view_colormap('jet')
#view_colormap('viridis')
#view_colormap('cubehelix')
#view_colormap('RdBu')



# -----------------------------------
# ----- 4.9.1.2 色の範囲制限と拡張 -----
# -----------------------------------
# カラーバー自体は単なるplt.Axesのインスタンスなので，
# これまでに学んだ軸と目盛りに関する書式設定のすべてを適用可能．
# extendプロパティを設定すると，カラーバーが示す色の範囲を狭め，
# 範囲外の値を上と下の三角矢印で示すことができる．
# これは，ノイズの影響を受けやすい画像を表示する場合などに便利な機能．

# 画像のピクセルに1%のノイズを加える
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

#plt.figure(figsize=(10, 3.5))

#plt.subplot(1, 2, 1)
#plt.imshow(I, cmap='RdBu')
#plt.colorbar()

#plt.subplot(1, 2, 2)
#plt.imshow(I, cmap='RdBu')
#plt.colorbar(extend='both')
#plt.clim(-1, 1)

# extend_colorbat.png
# 左側の図では，デフォルトの色範囲がノイズピクセルに引っ張られて決められたことで，
# 関心のある箇所をまったくわかりにくくしてしまっている．

# 右側の図では，色の制限が設定され，
# この制限よりも上または下の値を示すためにカラーバーの形が変わっている．
# その結果，データをよりよく可視化することができている．



# ---------------------------------
# ----- 4.9.1.3 離散的カラーバー -----
# ---------------------------------
# カラーマップは通常連続的だが，離散値を表現したい場合がある．
# これを行うには，plt.cm.get_cmap()関数に，カラーマップの名前と目的のビンの数を渡せばよい．
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1)

plt.show()



# ---------------------------------
# ----- 4.9.2 事例：手書きの数字 -----
# ---------------------------------