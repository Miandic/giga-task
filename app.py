from flask import Flask, render_template, request
import random
app = Flask(__name__)

global login

def checkAccount(log, pas, new):
    if new == 1:
        if log != '' and pas != '':
            print('Valid')
            return 'Valid'
        print('Invalid')
        return 'Invalid'
    else:
        if 1 == 1:  #Сверить по базе
            print('Valid')
            return 'Valid'
        else:
            print('Degenerat blyat')
            return 'Invalid'
    #Cheking ... Cheking...


@app.route('/')
def index(name = None):
    return render_template('index.html', name=name)


@app.route('/user')
def user(name = None, valid = None):
    global login
    if login != '':
        name = login
        valid = 'Valid'
    else:
        valid = 'Invalid'
    return render_template('profile.html', name=name, valid=valid)


@app.route('/reg', methods=['GET', 'POST'])
def registr(name = None):
    global login
    if request.method == 'POST':
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        print("Input! Login: " + tempLogin + "; Password: " + tempPassword)
        if checkAccount(tempLogin, tempPassword, 1) == 'Valid':
            login = tempLogin
            return render_template('index.html', name=name)
        else:
            name = 'Invalid'
        return render_template('reg.html', name=name)
    else:
        return render_template('reg.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login(name = None):
    global login
    if request.method == 'POST':
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        print("Login attempt! Login: " + tempLogin + "; Password: " + tempPassword)
        if checkAccount(tempLogin, tempPassword, 0) == 'Valid':
            name = tempLogin
            valid = 'Valid'
            return render_template('profile.html', name=name, valid=valid)
        else:
            name = 'Invalid'
        return render_template('reg.html', name=name)
    else:
        return render_template('reg.html', name=name)

@app.route('/upload')
def upload(name = None):
    return render_template('upload.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
