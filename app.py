from flask import Flask
from histogram import run_file

app = Flask(__name__)


@app.route('/')
def index():
    sent = run_file()
    return sent
