# Mimaco DB API
## Database Structure
今のところこんな感じ。

### User DB
| id | username | email | point|
|:---:|:---:|:---:|:---:|
| 1 | me | me@mail.com | 0 |
| 2 | you | you@mail.com | 0 |
| 3 | he | he@mail.com | 0 |


### WatchedUser DB
| id | username | major | minor|
|:---:|:---:|:---:|:---:|
| 1 | she | 11111 | 22222 |


## How to use
データのやりとりは全てjson形式で行います。
もし投げるjsonの形式が間違っている場合、`400`エラーを返します。
既にあるデータを参照するときに、指定したデータが存在しない場合、`404` エラーを返します。
新しくデータを追加するときなどに、既にそのデータが存在するときは、`409`エラーを返します。
ここでいうエラーコードとは、
```
{
    "message": "Bad Request",
    "result": 400
}
```
などのjsonファイルのことです。
以下、各DBに対して使用できるAPIについての説明です。

### User DB
下記のurlに対して、`GET`, `POST`, `PUT`, `PATCH`, `DELETE`のいずれかの操作が行えます。

https://mimaco.herokuapp.com/user

* `GET`: 登録されている全データを返します。URL末尾に`id`を追加すると、対応するユーザのみ返します。
  * 入力データ：なし
  * 出力データ：{"username", "email", "point"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。
* `POST`: 入力データをもとに新たにユーザを作成します。
  * 入力データ：{"username", "email", "point"}が格納されたjsonデータ
  * 出力データ：登録された{"username", "email", "point"}が格納されたjsonデータ
  * エラー処理：既に"username"が存在していたら、`409`エラーを返します。
* `PUT`: 指定された`id`のuserのデータを書き換えます。
  * 入力データ：{"username", "email", "point"}が格納されたjsonデータ。全て必要。
  * 出力データ：上書きされた{"username", "email", "point"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。
* `PATCH`: 指定した`id`のユーザのポイント指定した数だけ足します。
  * 入力データ：{"point_increment"}が格納されたjsonデータ
  * 出力データ：ポイントが足されたユーザの{"username", "email", "point"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。

* `DELETE`: 指定した`id`に対応するユーザのデータを削除します。
  * 入力データ：なし
  * 出力データ：削除された{"username", "email", "point"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。


### WatchedUser DB
下記のurlに対して、`GET`, `POST`, `PUT`, `DELETE`のいずれかの操作が行えます。

https://mimaco.herokuapp.com/watched_user

* `GET`: 登録されている全データを返します。URL末尾に`id`を追加すると、対応するユーザのみ返します。
  * 入力データ：なし
  * 出力データ：{"username", "minor", "major"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。
* `POST`: 入力データをもとに新たにユーザを作成します。
  * 入力データ：{"username", "minor", "major"}が格納されたjsonデータ
  * 出力データ：登録された{"username", "minor", "major"}が格納されたjsonデータ
  * エラー処理：既に"username"が存在していたら、`409`エラーを返します。
* `PUT`: 指定された`id`のuserのデータを書き換えます。
  * 入力データ：{"username", "minor", "major"}が格納されたjsonデータ。全て必要。
  * 出力データ：上書きされた{"username", "minor", "major"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。
* `DELETE`: 指定した`id`に対応するユーザのデータを削除します。
  * 入力データ：なし
  * 出力データ：削除された{"username", "minor", "major"}が格納されたjsonデータ
  * エラー処理：`id`が存在しない場合、`404`エラーを返します。


## 使ったライブラリ
Flask, SQLAlchemy, Marshmallow


## 自分用：データベースの更新方法
    python
    >>> from crud import db
    >>> db.create_all()
