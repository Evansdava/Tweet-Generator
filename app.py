from flask import Flask, render_template, request
from scripts.markov import main
# from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    num = str(request.args.get('num'))
    # Checking inputs
    if num.isnumeric():
        num = int(num)
    else:
        num = 1
    # Generates a sentence of length num
    if num < 1:
        num = 1

    sent = main(3, num)
    return render_template('index.html', sent=sent, num=num)
