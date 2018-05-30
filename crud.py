from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


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
    username = request.json['username']
    email = request.json['email']

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
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    point = request.json['point']

    user.email = email
    user.username = username
    user.point = point

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
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

    def __init__(self, username, major, minor):
        self.username = username
        self.major = major
        self.minor = minor


class WatchedUserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'major', 'minor')


watched_user_schema = WatchedUserSchema()
watched_users_schema = WatchedUserSchema(many=True)


# endpoint to create new user
@app.route("/watched_user", methods=["POST"])
def add_watched_user():
    username = request.json['username']
    major = request.json['major']
    minor = request.json['minor']

    new_user = WatchedUser(username, major, minor)

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
    user = WatcheUser.query.get(id)
    return watched_user_schema.jsonify(user)


# endpoint to update user
@app.route("/watched_user/<id>", methods=["PUT"])
def watched_user_update(id):
    user = WatcheUser.query.get(id)
    username = request.json['username']
    major = request.json['major']
    minor = request.json['minor']

    user.email = email
    user.major = major
    user.minor = minor

    db.session.commit()
    return watched_user_schema.jsonify(user)


# endpoint to delete user
@app.route("/watched_user/<id>", methods=["DELETE"])
def watched_user_delete(id):
    user = WatcheUser.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return watched_user_schema.jsonify(user)


# Main
if __name__ == '__main__':
    app.run(debug=True)
