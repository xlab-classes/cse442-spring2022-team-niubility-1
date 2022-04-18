from . import db
from . import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    task = db.relationship('Task', backref='task_user')

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    name =db.Column(db.String(64),nullable=True)
    begin = db.Column(db.DateTime(64),nullable=True)
    begin_time = db.Column(db.String(64),nullable=True)
    priority = db.Column(db.String(64),nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.name