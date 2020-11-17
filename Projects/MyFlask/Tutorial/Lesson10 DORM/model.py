from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'jikexueyuan', 'host': '127.0.0.1', 'port': 27017}
db = MongoEngine(app)


class User(db.Document):
    username = db.StringField()
    email = db.StringField()

    def __str__(self):
        return "name:{} email:{}".format(self.username, self.email)

    @staticmethod
    def query_users():
        users = User.objects.all()
        for u in users:
            print(u)


if __name__ == '__main__':
    # s = User(username='cifer02', email='cifer02@cifer.com')
    # s.save()

    User.query_users()
