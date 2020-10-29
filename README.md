# CSV グラフ化プログラム
## リリースノート
### v2.4 (最新)
・4F実験室のオシロスコープ専用にハードコーディングしたものであり、それ以外の.CSVファイルでは動かない   
・NNCTの学生はこっちを推奨
・とりあえずの完成版
### v1.1 (推奨)
・ヘッダとフッダさえ消せばどのCSVにも対応可能の汎用性の高いバージョン   
・NNCTの学生でない人はこっちを推奨

## 概要
1) CSVのデータをグラフに変換します.   
2) Excelでグラフを整形するのが面倒な人は使ってみてください.   
<img src="https://github.com/NekoMimi-Cateye/CSVtoGraph_forNNCT3J/blob/master/result.png" alt="result.png" title="表示結果" width="50%" height="50%">

## 使用方法
### 1) Pythonを持っている場合
1) csv_loader.pyのコードをコピーまたはクローンする.   
2) プログラムのあるディレクトリでコンソールを開く.
3) $python csv_loader.py で実行   
(新しいファイル名で保存した場合は適宜読み替えてください).
4) コンソールの指示に従ってください.
5) 結果は"result.png"に保存されます. 既にあれば上書きされます.

### 2) Pythonを持っていない場合
0) Googleアカウントを作成
1) Google提供のColaboratoryにアクセス   
URL: https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja
2) ファイル--> ノートブックを新規作成   
<img src="https://github.com/NekoMimi-Cateye/CSVtoGraph_forNNCT3J/blob/master/step1.png" alt="step1.png" title="step1"width="100%" height="50%">
3) 以下のコードを入力して実行
```Python
from google.colab import drive
drive.mount('/content/drive')
```
<img src="https://github.com/NekoMimi-Cateye/CSVtoGraph_forNNCT3J/blob/master/step2.png" alt="step2.png" title="step2" width="50%" height="50%">

4) 表示されたURLに移動して、表示されたコードをURLの下の入力ボックス内にコピーし、Enterキーを押す。   
<img src="https://github.com/NekoMimi-Cateye/CSVtoGraph_forNNCT3J/blob/master/step3.png" alt="step3.png" title="step3" width="50%" height="50%">

5) 以下のコードを入力して実行(cd コマンド)
```
%cd /content/drive/My Drive
```
6) csv_loader.pyのコードをコピー&ペーストして実行

7) あとはPythonを持っている場合の4-5を参照   
(注意1: この場合ファイルはGoogleドライブ内の'My Drive'直下においてください)   
(注意2: フォントがTimes New Romanでは無くなります。)

## 注意
1) pandasとmatplotlibを使用しているので, Pythonで実行する場合はpandas,matplotlib, numpyの3つのライブラリがインストールされているか確認してください.   
2) 本プログラム内での表以外の部分とは、ヘッダーとフッダーのことを指します.    
ex. NNCT 3J工学実験実習 オシロスコープデータの場合>>>
ヘッダー:1-15行目
フッダー:なし   
3) 横軸が共有されたグラフが作成されます.
### ライブラリ確認方法
```
pip list //pipの場合
conda list //condaの場合
```

### numpy インストール方法
・numpyが入っていないとpandasとmatplotlibは正常動作しません.
```
pip install numpy //pipの場合
conda install numpy //condaの場合
```

### pandas インストール方法
```
pip install pandas //pipの場合
conda install pandas //condaの場合
```

### matplotlib インストール方法
```
pip install matplotlib //pipの場合
conda install matplotlib //condaの場合
```