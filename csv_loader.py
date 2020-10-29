import pandas as pd
import matplotlib.pyplot as plt

print('【はじめに】Pythonユーザー: csvファイルをこのexeファイルと同じディレクトリに入れてください')
print('【はじめに】Colaboratoryからの実行: csvファイルをMy Drive直下に入れてください')
print('【はじめに】csvファイルの表以外の部分(ヘッダーとフッダー)を削除してください\n\n')

print('ファイル名を入力してください.  例) ./hoge.csv  注)./ は必要')
print('ファイル名: ', end='')
path = input()

df = pd.read_csv(str(path), header=0)
df_h = pd.read_csv(str(path), header=None)

print('\n----------------------------------------')
print('{:7s} {:s}\n'.format('[INFO]', path))
print(df)
print('----------------------------------------')

data_tag = []
x_tag = 0
for i in range(len(df.columns)):
    data_tag.append(df_h[i][0])

nx = df['TIME']
ny = []

print('\nグラフにするデータ列を選んでいきます.')
for i in data_tag:
    if (i == "TIME"):
        continue
    else:
        print('TIMEを横軸, {:s}を縦軸としてグラフを作成しますか? (はい: yes , いいえ: その他のコマンド(何かを入力))'.format(i))
        check = input()
        if (check == 'yes'):
            ny.append(df[i])

print('\nタイトルを入力 >>> ', end='')
title = input()

print('\nグラフを作成しています')

cs = ["m", "u", "n"]
cb = ["k", "M", "G"]
x = []
y = [[] for i in range(len(ny))]
for i in nx:
    x.append(i)

xmin = x[0]
for i in range(len(x)):
    x[i] -= xmin

xmax = x[len(x)-1]
xc = 0
while xmax < 1:
    xmax *= 10
    xc += 1
c = xc // 3 + 1

for i in range(len(x)):
    x[i] *= 10 ** (3 * c)
xc += 1



for i in range(len(ny)):
    for j in ny[i]:
        y[i].append(j)

plt.figure(figsize = (12, 3*len(y)))
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.major.width"] = 1.5
plt.rcParams["ytick.major.width"] = 1.5
plt.rcParams["xtick.minor.width"] = 1.0
plt.rcParams["ytick.minor.width"] = 1.0
plt.rcParams["xtick.major.size"] = 10
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["xtick.minor.size"] = 5
plt.rcParams["ytick.minor.size"] = 5
plt.rcParams["font.size"] = 14
plt.rcParams["axes.linewidth"] = 1.5

for i in range(len(y)):
    plt.subplot(len(y), 1, i+1)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.minor.visible"] = True
    plt.rcParams["ytick.minor.visible"] = True
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["xtick.minor.width"] = 1.0
    plt.rcParams["ytick.minor.width"] = 1.0
    plt.rcParams["xtick.major.size"] = 10
    plt.rcParams["ytick.major.size"] = 10
    plt.rcParams["xtick.minor.size"] = 5
    plt.rcParams["ytick.minor.size"] = 5
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.linewidth"] = 1.5
    if (i == 0):
        plt.title(title)
    plt.tick_params(labelbottom=False)
    plt.ylim((-2.5, 7.5))
    index = 0
    while (y[i][index] < 5):
        index += 1
    fs = index
    while (y[i][index] > 0):
        index += 1
    while (y[i][index] < 5):
        index += 1
    fe = index

    while (y[i][fs] < 2.5):
        fs += 1
    while (y[i][fs] < 2.5):
        fe += 1
    p1 = plt.vlines([x[fs]], -2.5, 7.5, "black", linestyles='dashed')
    p2 = plt.vlines([x[fe]], -2.5, 7.5, "black", linestyles='dashed')
    plt.text(x[fe], 6, "T={:3.2f}[{:s}s], f={:3.2f}[{:s}Hz]".format(x[fe]-x[fs], cs[c], 1000 / (x[fe]-x[fs]) , cb[c-2]), size=15)
    plt.ylabel("Voltage [V]")
    plt.plot(x, y[i], color = "black")
plt.tick_params(labelbottom=True)
plt.xlabel("time [{:s}s]".format(cs[c]))

print('作成完了 保存先: ./result.png')
plt.savefig('result.png')
print("Successed!")
plt.show()