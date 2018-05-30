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

### User DB
下記のurlに対して、`GET`, `POST`, `PUT`, `DELETE`のいずれかの操作が行えます。
データのやりとりは全てjson形式で行います。

https://mimaco.herokuapp.com/user

* `GET`: 登録されている全データを返します。URL末尾に`id`を追加すると、対応するユーザのみ返します。
* `POST`: `username`, `email`, `point`が格納されたjsonデータを渡し、データベースに追加します。
* `PUT`: URL末尾に`id`を追加して使用。`username`, `email`, `point`が格納されたjsonデータを渡し、データベースを書き換えます。
* `DELETE`: URL末尾に`id`を追加して使用。対応するユーザのデータを削除します。


### WatchedUser DB
下記のurlに対して、`GET`, `POST`, `PUT`, `DELETE`のいずれかの操作が行えます。
データのやりとりは全てjson形式で行います。

https://mimaco.herokuapp.com/watched_user

* `GET`: 登録されている全データを返します。URL末尾に`id`を追加すると、対応するユーザのみ返します。
* `POST`: `username`, `major`, `minor`が格納されたjsonデータを渡し、データベースに追加します。
* `PUT`: URL末尾に`id`を追加して使用。`username`, `major`, `minor`が格納されたjsonデータを渡し、データベースを書き換えます。
* `DELETE`: URL末尾に`id`を追加して使用。対応するユーザのデータを削除します。


## 使ったライブラリ
Flask, SQLAlchemy, Marshmallow


## データベースの更新方法
    python
    >>> from crud import db
    >>> db.create_all()


## 補足
その辺に落ちてるコードを99.9%使い回しました。
現状世界中の誰でもデータを自由に書き換えられてしまう状況です。
これをなんとかするのが今後の課題。
