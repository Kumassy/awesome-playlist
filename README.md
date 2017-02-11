# Awesome Playlist
「さいきょうのぷれいりすと」を作るためのスクリプトです。[Anison Generation](http://anison.info/) からダウンロードできる CSV データから、Google Play Music のサブスクリプションプランで聴けるアニソンを抽出し、プレイリストを作成します。

# 使い方
## データベースのダウンロード
[Anison Generation](http://anison.info/) の「ダウンロード」ページより、「アニメOP/ED」のデータをダウンロードして展開します。

```
$ tree .

.
├── README.md
├── anison.csv
├── make_playlist.py
├── search_artist.py
└── search_song.py
```

## 環境変数の設定
お使いの Google アカウントのユーザー ID とパスワードを export します

```
$ export GMUSIC_USER=your_account@gmail.com
$ export GMUSIC_PW=****password****
```

## 実行
予め必要なパッケージをインストールしておきます

```
$ pip install pandas
$ pip install IPython
$ pip install gmusicapi
```

そして、スクリプトを実行します

```
$ python make_playlist.py
```

プレイリストが 1000 曲を超えるとプレイリストに曲が追加できなくなるため、例外が投げられてスクリプトの実行が終わりますが、適当にスクリプトを書き換えてうまく対応してください....

# 注意事項
- このスクリプトは Google Play Music の非公式 API を大量に使用するため、Google に BAN されてしまう可能性が否定できません。スクリプトを実行する際は自己責任でお願いします。

# ライセンス
MIT
