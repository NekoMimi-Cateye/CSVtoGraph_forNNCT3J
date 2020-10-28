import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

print('【はじめに】Pythonユーザー: csvファイルをこのexeファイルと同じディレクトリに入れてください')
print('【はじめに】Colaboratoryからの実行: csvファイルをMy Drive直下に入れてください')
print('【はじめに】csvファイルの1-15行目(表以外の部分)を削除してください\n')
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

while(1):
    print('横軸にしたいデータ列のタグを選択してください (タグ: ', end='')
    for i in data_tag:
        print('{:s}, '.format(i), end='')
    print(')')
    check = input()
    if (check in data_tag):
        nx = df[check]
        x_tag = check
        break
    else:
        print('[ERROR] \'{:s}\' という名前のタグは見つかりません. もう一度選択してください'.format(check))

nx = df['TIME']
ny = []

print('\n縦軸にするデータ列を選んでいきます.')
for i in data_tag:
    if (i == x_tag):
        continue
    else:
        print('{:s}を横軸, {:s}を縦軸としてグラフを作成しますか? (はい: yes , いいえ: その他のコマンド)'.format(x_tag, i))
        check = input()
        if (check == 'yes'):
            ny.append(df[i])

print('\nグラフの題名を入力してください')
title = input()

print('\nグラフを作成しています')
print('作成完了 保存先: ./result.png')

x = []
y = [[] for i in range(len(ny))]
for i in nx:
    x.append(i)

for i in range(len(ny)):
    for j in ny[i]:
        y[i].append(j)

plt.figure(figsize = (12, 12))
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
    if (i == 0):
        plt.title(title)
    plt.tick_params(labelbottom=False)
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
    plt.ylim((-2.5, 7.5))
    plt.plot(x, y[i])
plt.tick_params(labelbottom=True)

plt.savefig('result.png')
print("Successed!")
plt.show()