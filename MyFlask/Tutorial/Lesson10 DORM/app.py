from model import db

app = db.app

@app.route('/')
def hello():
    return "hello"
