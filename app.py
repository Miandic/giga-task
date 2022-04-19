from flask import Flask, redirect, request, render_template, make_response
import psycopg2
import functions

app = Flask (__name__)


conn = None
cur = None
command  = ""
userID = 0


conn, cur = functions.set_connection(conn , cur)


@app.route('/')
def index(name = None):
    #проверка по кукуам что аккаунт войдён
    #если нет, то
    if (request.cookies.get('login') != None):
        return  render_template('index.html')
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login(valid= None):
    if request.method == 'POST':
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        #есть в базе на самом деле
        users = functions.get_users(conn, cur)
        for user in users:
            if user['login'] == tempLogin and user['password'] == tempPassword:
                resp = make_response(redirect('/'))
                resp.set_cookie('login',  tempLogin )
                resp.set_cookie('password', tempPassword)
                userId = user['id']
                return resp
        else:
            valid = 'Invalid'
            return render_template('login.html', valid=valid)
    else:
        return render_template('login.html', valid=valid)


@app.route('/reg', methods=['GET', 'POST'])
def registr(name = None):
    pass


app.run()
