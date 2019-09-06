from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def addUser(self):
        """
        新增用户
        :return:
        """
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            return 0

    def isExisted(self):
        temp_user = User.query.filter_by(username=self.username, password=self.password).first()
        return 1 if temp_user else 0


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    sender = db.Column(db.String(32))

    def __init__(self, content, sender):
        self.content = content
        self.sender = sender

    def addEntry(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            return 0


def getAllEntry():
    entry_list = list()
    entry_list = Entry.query.filter_by().all()
    return entry_list


if __name__ == '__main__':
    db.create_all()
    e = Entry('hi', 'jike')
    e.addEntry()
