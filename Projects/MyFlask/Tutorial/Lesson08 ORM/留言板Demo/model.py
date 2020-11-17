from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


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
            return None


def getAllEntry():
    entry_list = Entry.query.filter_by().all()
    return entry_list


if __name__ == '__main__':
    data = getAllEntry()
    for d in data:
        print(d.content)
