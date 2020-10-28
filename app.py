from flask import Flask, render_template, request
from scripts.markov import main
# from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    n = str(request.args.get('n'))
    num = str(request.args.get('num'))
    # Checking inputs
    if n.isnumeric():
        n = int(n)
    else:
        n = 2
    # Uses a markov chain of order n
    if n < 1:
        n = 1
    if num.isnumeric():
        num = int(num)
    else:
        num = 1
    # Generates a sentence of length num
    if num < 1:
        num = 1

    sent = main(3, num)
    return render_template('index.html', sent=sent, n=n, num=num)
