from flask import Flask, render_template, request
from python.histogram import run_file
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('num'):
        num = int(request.args.get('num'))
    else:
        num = randint(5, 20)
    sent = run_file(num)
    return render_template('index.html', sent=sent)
