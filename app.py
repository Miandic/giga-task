from flask import Flask, redirect, request, render_template, make_response
import psycopg2

app = Flask (__name__)

conn  = None
cur = None
command  = ""



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
        login = request.form['login']
        password = request.form['password']
        #есть в базе на самом деле
        if  login == '123' and   password == '123' :
            resp = make_response(redirect('/'))
            resp.set_cookie('login',  login )
            resp.set_cookie('password', password)
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
