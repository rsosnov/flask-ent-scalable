import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True,
                         index=True)
    password = db.Column(db.String(255))
    posts = db.relationship("Post", backref="user", lazy="dynamic")

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"<User '{self.username}'>"


tags = db.Table("post_tags",
                db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
                db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")))


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
    comments = db.relationship("Comment", backref="post", lazy="dynamic")
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    tags = db.relationship("Tag",
                           secondary=tags,
                           backref=db.backref("posts", lazy="dynamic"))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"<Post '{self.title}'>"


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"<Tag '{self.title}'>"


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.now)
    post_id = db.Column(db.Integer(), db.ForeignKey("post.id"))

    def __repr__(self):
        return f"<Comment '{self.text[:15]}'>"

# Changed to show the git diff command
@app.route('/')
def home():
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
