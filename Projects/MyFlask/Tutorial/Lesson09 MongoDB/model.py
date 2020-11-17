import pymongo


def getCollection():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.jikexueyuan
    user = db.user_collection

    return user


class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        user = {"name": self.name, "email": self.email}
        coll = getCollection()
        id = coll.insert(user)
        print(id)

    @staticmethod
    def query_users():
        coll = getCollection()
        users = coll.find()
        return users


if __name__ == '__main__':
    # u = User(name='cifer01', email='cifer01@cifer.com')
    # u.save()
    us = User.query_users()
    for user in us:
        print(user)
