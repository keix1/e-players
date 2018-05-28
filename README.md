# Mimaco DB API
## Database Structure
今のところこんな感じ。

| id | username | email | point|
|:---:|:---:|:---:|:---:|
| 1 | me | me@mail.com | 0 |
| 2 | you | you@mail.com | 0 |
| 3 | he | he@mail.com | 0 |

## How to use
下記のurlに対して、`GET`, `POST`, `PUT`, `DELETE`のいずれかの操作が行えます。
データのやりとりは全てjson形式で行います。

https://mimaco.herokuapp.com/user

* `GET`: 登録されている全データを返します。URL末尾に`id`を追加すると、対応するユーザのみ返します。
* `POST`: `username`, `email`, `point`が格納されたjsonデータを渡し、データベースに追加します。
* `PUT`: URL末尾に`id`を追加して使用。`username`, `email`, `point`が格納されたjsonデータを渡し、データベースを書き換えます。
* `DELETE`: URL末尾に`id`を追加して使用。対応するユーザのデータを削除します。

## 使ったライブラリ
Flask, SQLAlchemy, Marshmallow

## 補足
その辺に落ちてるコードを99.9%使い回しました。
現状世界中の誰でもデータを自由に書き換えられてしまう状況です。
これをなんとかするのが今後の課題。
