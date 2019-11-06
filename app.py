from flask import Flask, render_template, request
from python.histogram import run_file
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    num = str(request.args.get('num'))
    # Checking inputs
    if num.isnumeric():
        num = int(num)
    else:
        num = randint(5, 20)
    # Generates a sentence of length num
    sent = run_file(num)
    return render_template('index.html', sent=sent)
