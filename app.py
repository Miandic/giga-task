from flask import Flask, render_template, request
import psycopg2
import random
import os


app = Flask(__name__)

global login
global conn
global cur

def set_connection():
    global conn
    global cur
    conn = psycopg2.connect(user="postgres", password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pog")
    cur = conn.cursor()

def close_connection():
        global conn
        global cur

        cur.close()
        conn.commit()

        if conn is not None:
                conn.close()

def insert_value(login , password):
    set_connection()

    command = """insert into users(login, password, photocnt) values (%s,  %s, %s)"""
    value  =  (login, password, 0)

    cur.execute(command, value)

    close_connection()


def get_values():
    set_connection()

    command = "SELECT * FROM Users"
    cur.execute(command)

    ans = []

    result = cur.fetchall()
    for x in result:
        ans.append(x)

    close_connection()
    return ans

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
        #need check login on unique
        if checkAccount(tempLogin, tempPassword, 1) == 'Valid':


            login = tempLogin

            dirName = f'Photos/{login}'
            os.makedirs(dirName)

            insert_value(tempLogin, tempPassword)

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
        users = get_values()
        print(users)
        flag = False
        for user in users:
            if (user[1] == tempLogin and  user[2] == tempPassword):
                flag = True
        if checkAccount(tempLogin, tempPassword, 0) == 'Valid' and flag  :
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
