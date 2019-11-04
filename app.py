from flask import Flask, render_template, request
from python.histogram import run_file

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('num'):
        num = int(request.args.get('num'))
    else:
        num = 10
    sent = run_file(num)
    return render_template('index.html', sent=sent)
