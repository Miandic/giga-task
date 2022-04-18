from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index(name = None):
    return render_template('index.html', name=name)


@app.route('/user')
def user(name = None):
    return render_template('profile.html', name=name)


@app.route('/reg')
def registr(name = None):
    return render_template('reg.html', name=name)


@app.route('/upload')
def upload(name = None):
    return render_template('upload.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
