from flask import Flask, render_template, request

app = Flask(__name__)

global tempLogin
global tempPassword

def checkAccount(log, pas, new):
    #Cheking ... Cheking...
    return 'Valid'

@app.route('/')
def index(name = None):
    return render_template('index.html', name=name)


@app.route('/user')
def user(name = None):
    return render_template('profile.html', name=name)


@app.route('/reg', methods=['GET', 'POST'])
def registr(name = None):
    if request.method == 'POST':
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        print("Input! Login: " + tempLogin + "; Password: " + tempPassword)
        return render_template('reg.html', name=name)
    else:
        return render_template('reg.html', name=name)

@app.route('/validate_reg')
def validate_reg(name = None):
    if checkAccount(tempLogin, tempPassword, 1) == 'Valid':
        return render_template('profile.html', name=name)
    else:
        return render_template('reg.html', name=name)

@app.route('/upload')
def upload(name = None):
    return render_template('upload.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
