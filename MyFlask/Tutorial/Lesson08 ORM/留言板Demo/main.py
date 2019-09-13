"""
使用Flask-wtf插件优化
2019-8-10 17:17:18
cifer woods
"""

from flask import Flask, request, redirect, render_template, url_for
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from model import *
from model import db

app = db.app  # 千万不要app = Flask(__name__)，否则会报错'SQLALCHEMY_TRACK_MODIFICATIONS'


class PublishForm(Form):
    inp_content = StringField("content", [validators.data_required()])
    inp_sender = StringField("sender", [validators.data_required()])
    btn_submit = SubmitField("submit")


@app.errorhandler(404)
def notFound(e):
    return redirect(url_for('show'))


@app.route('/show', methods=['GET', 'POST'])
def show():
    my_entry_form = PublishForm(request.form)
    entries = getAllEntry()
    print(len(entries))
    if request.method == 'POST':
        e = Entry(my_entry_form.inp_content.data, my_entry_form.inp_sender.data)
        e.addEntry()
        entries = getAllEntry()
        return render_template('show.html', re_form=my_entry_form, re_entries=entries)
    return render_template('show.html', re_form=my_entry_form, re_entries=entries)


if __name__ == '__main__':
    app.run(port=8888, debug=True)
