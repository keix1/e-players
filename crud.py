from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import line

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)


# User DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    point = db.Column(db.Integer)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.point = 0


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email', 'point')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    try:
        username = request.json['username']
        email = request.json['email']
    except (ValueError, KeyError, TypeError):
        abort(400)

    exists = User.query.filter_by(username=username).first()
    if exists:
        abort(409)
    else:
        new_user = User(username, email)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    exists = User.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        user = User.query.get(id)
        return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    exists = User.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        try:
            username = request.json['username']
            email = request.json['email']
            point = request.json['point']
        except (ValueError, KeyError, TypeError):
            abort(400)

        user = User.query.get(id)
        user.email = email
        user.username = username
        user.point = point

        db.session.commit()
        return user_schema.jsonify(user)


# # endpoint to update user's point
# @app.route("/user/<id>", methods=["PATCH"])
# def point_update(id):
#     '''
#         指定したidのuserのポイントをpoint_increment分だけ足す。
#     '''
#     exists = User.query.filter_by(id=id).first()
#     if not exists:
#         abort(404)
#     else:
#         try:
#             point_increment = request.json['point_increment']
#         except (ValueError, KeyError, TypeError):
#             abort(400)
#
#         user = User.query.get(id)
#         point = user.point
#         user.point = point + point_increment
#
#         db.session.commit()
#         return user_schema.jsonify(user)



# endpoint to update user
@app.route("/user/<string:username>", methods=["POST"])
def point_update(username):
    try:
        username = request.json['username']
        major = request.json['major']
        minor = request.json['minor']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
    except (ValueError, KeyError, TypeError):
        abort(400)

    watched_usr = WatchedUser.query.filter_by(major=major,minor=minor).first()
    # major, minorが一致するユーザがいないとき、新規追加
    if not watched_usr:
        try:
            watched_username = request.json['watched_username']
        except (ValueError, KeyError, TypeError):
            abort(409)
        watched_usr = WatchedUser(watched_username, major, minor)
        db.session.add(watched_usr)
        db.session.commit()
    # いるとき、latitudeとlongitudeを更新（あとで行追加として再実装したい）
    else:
        watched_usr.longitude = longitude
        watched_usr.latitude = latitude

        db.session.commit()

    usr = User.query.filter_by(username=username).first()
    if not usr:
        abort(404)
    else:
        usr.point += 1
        db.session.commit()

    line_message = username + "が" + watched_usr.username + "を見つけました"
    line.lineNotify(line_message)

    return user_schema.jsonify(usr), watched_user_schema.jsonify(watched_usr)





# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    exists = User.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)



# WatchedUser DB
class WatchedUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    major = db.Column(db.Integer, unique=True)
    minor = db.Column(db.Integer, unique=True)
    latitude = db.Column(db.String(80))
    longitude = db.Column(db.String(80))

    def __init__(self, username, major, minor, latitude, longitude):
        self.username = username
        self.major = major
        self.minor = minor
        self.latitude = latitude
        self.longitude = longitude


class WatchedUserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'major', 'minor', 'latitude', 'longitude')


watched_user_schema = WatchedUserSchema()
watched_users_schema = WatchedUserSchema(many=True)


# endpoint to create new user
@app.route("/watched_user", methods=["POST"])
def add_watched_user():
    try:
        username = request.json['username']
        major = request.json['major']
        minor = request.json['minor']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
    except (ValueError, KeyError, TypeError):
        # print(username,major,minor,latitude,longitude)
        abort(400)

    exists = WatchedUser.query.filter_by(username=username).first()
    if exists:
        abort(409)
    else:
        new_user = WatchedUser(username, major, minor, latitude, longitude)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user)


# endpoint to show all users
@app.route("/watched_user", methods=["GET"])
def get_watched_user():
    all_users = WatchedUser.query.all()
    result = watched_users_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/watched_user/<id>", methods=["GET"])
def watched_user_detail(id):
    exists = WatchedUser.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        user = WatcheUser.query.get(id)
        return watched_user_schema.jsonify(user)


# endpoint to update user
@app.route("/watched_user/<id>", methods=["PUT"])
def watched_user_update(id):
    exists = WatchedUser.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        try:
            username = request.json['username']
            major = request.json['major']
            minor = request.json['minor']
            latitude = request.json['latitude']
            longitude = request.json['longitude']
        except (ValueError, KeyError, TypeError):
            abort(400)

        user = WatcheUser.query.get(id)

        user.email = email
        user.major = major
        user.minor = minor
        user.latitude = latitude
        user.longitude = longitude

        db.session.commit()
        return watched_user_schema.jsonify(user)


# endpoint to delete user
@app.route("/watched_user/<id>", methods=["DELETE"])
def watched_user_delete(id):
    exists = WatchedUser.query.filter_by(id=id).first()
    if not exists:
        abort(404)
    else:
        user = WatcheUser.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return watched_user_schema.jsonify(user)


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(409)
def error_handler(error):
    '''
     Description
      - abortした時にレスポンスをレンダリングするハンドラ
    '''
    response = jsonify({ 'message': error.name, 'result': error.code })
    return response, error.code

# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
