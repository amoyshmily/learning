from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


# 自动重定向到add方法所在url
@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('add'))


@app.route('/calculator', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = request.form['adder1']
        b = request.form['adder2']
        my_result = int(a)+int(b)
        return render_template('index.html', result=str(my_result))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080)
