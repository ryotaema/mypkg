# mypkg

[![test](https://github.com/ryotaema/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ryotaema/mypkg/actions/workflows/test.yml)

ロボットシステム学2023で使っているリポジトリです。
ros2を利用してtalkerから出した信号をlissonerで受信して値を表示します。
talkerから出る信号は「f」か「j」の入力に応じて変化します。

## 詳細

### コマンドの説明

* talker

開始した後、「f」もしくは「j」を押ことにより値を出力するノードです。「f」を入力することで値は＋１され、「j」を入力することで値はー１されます。「f」か「j」以外が入力された場合には値は変化しません。

* listener

出力された値をパブリッシャーから受け取り標準出力するノードです。

### 使用方法

GitHubとPython、ROS2が利用できる環境で、以下のコマンドでディレクトリを移動してください。

```
$ cd ros2_ws
$ cd src
```

以下のコマンドを入力し、自分の環境にコピーしてください。

```

$ git clone https://github.com/ryotaema/mypkg.git

```

以下のコマンドでファイルがダウンロードされていることを確認してください。

```
$ ls
```

以下のようにコピーしてきたディレクトリに移動し、ビルドしてください。

```

$ cd ~/ros2_ws

$ colcon build
$ source ~/.bashrc

```

### 実行方法,結果

talker.pyとlistener.pyをそれぞれ異なる端末で実行します。
実行方法とその結果は以下の通りです。

*端末1(talker.py)

```

$ cd ~/ros2_ws
$ ros2 run mypkg talker

$ f
$ f
$ j
$ g

```

*端末2(listener.py)

```

$ cd ~ros2_ws
$ ros2 run mypkg listener

[INFO] [1703932910.449369287] [listen_node]: Listen: 0
[INFO] [1703932913.412028479] [listen_node]: Listen: 1
[INFO] [1703932913.959791715] [listen_node]: Listen: 2
[INFO] [1703932916.062654816] [listen_node]: Listen: 1
[INFO] [1703932927.329383762] [listen_node]: Listen: 1

```

## 必要なソフトウェア

* Python
  * テスト済み: 3.7~3.10
* ros2
  * ver.humble

## テスト環境

* Ubuntu20.04.2 LTS
* ros2 humble

## ライセンス関連

### plusについて

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを一部加筆し，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)


© 2023 Ryota Ema
