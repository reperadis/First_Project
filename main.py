from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homak')
def homak():
    return render_template('getrickroledlmao.html')

@app.route('/calc')
def calc():
    n1 = 55
    n2 = 108
    return render_template('calc.html', num1=n1, num2=n2)


app.run(debug=True)