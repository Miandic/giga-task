from flask import Flask, redirect, request, render_template, make_response
import psycopg2
import functions

app = Flask (__name__)

inputs = []
urlForTemp = ""
conn = None
cur = None
command  = ""
userId = 0
userBoardId = 0
columnId = 0
conn, cur = functions.set_connection(conn , cur)


@app.route('/', methods=['GET', 'POST'])
def index(name=None, nick=None, create='true', other = None):
    #проверка по кукам что аккаунт войдён
    #если нет, то\
    global userId
    if (request.cookies.get('login') != None):
        flag = False
        name = request.cookies.get('login')
        users = functions.get_users(conn, cur)
        for user in users:
            if user['login'] == name:
                nick = user['nickname']
                userId = user['id']
                flag = True
        if (not flag):
            return redirect('/login')
        print(userId)
        boards = functions.get_boards(conn, cur, userId)
        print(boards)
        if request.method == 'POST':
            nameBoard = 'Новый автомат'
            if (len(boards) >= 1):
                nameBoard = nameBoard + ' ' +  str(len(boards))

            newBoardId = functions.add_board_for_user(conn, cur, userId, nameBoard)
            redir = '/board/' + str(newBoardId)
            return redirect(redir)
        for board in boards:
            if board['userright'] == 'creator':
                create = None
            if board['userright'] != 'creator':
                other = 'true'
        print(create)
        return  render_template('index.html', name=name, nick=nick, boards=boards, create=create, other=other)
    else:

        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login(valid= None):
    global userId
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
def reg(name = None):
    if  request.method == 'POST':
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        tempPhone = request.form['phone']
        functions.add_user(conn, cur, tempLogin, tempLogin, tempPassword, tempPhone)
        return redirect('/login')
    else:
        return render_template('reg.html')


@app.route('/logout')
def logout():
    return redirect('/login')


@app.route('/boards', methods= ['GET', 'POST'])
def boards():
    global userId
    boards = functions.get_boards(conn ,cur, userId)
    return render_template('boards.html', boards = boards)


@app.route('/board/<boardId>', methods= ['GET' , "POST"])
def board(boardId):
    global conn
    global cur
    global inputs
    global userBoardId
    global columnId
    userBoardId = boardId
    conn, cur = functions.set_connection(conn ,cur)
    command = ("""
        select columnName, posOnBoard, boardColumn.id
        from boardColumn
        where boardColumn.boardId = %s
        ORDER BY posOnBoard
    """)
    cur.execute(command, [boardId])
    columns = functions.get_values(cur)
    print(columns)

    cur.execute("SELECT * from boards where id = %s ",  [boardId])
    board = functions.get_values(cur)
    board = board[0]
    tasks = []
    \
    for i in range(1, int(board['columncnt']) +1):
        command = """
            select taskName, taskColour, taskContent, tasks.id , tasks.timetobedone
            from tasks
            where tasks.boardId = %s  and tasks.columnid = %s
        """
        cur.execute(command, [userBoardId, columns[i-1]['id']])
        tasks.append(functions.get_values(cur))
    if request.method == 'POST':
        columnId = request.form['columnId']
        inputs = ['taskname' , 'timedobedone' , 'taskContent', 'taskcolour']
        return redirect('/temp')
    print(tasks)
    return render_template('board.html', board=board, columns=columns, tasks=tasks )

@app.route('/temp', methods = ["POST" , "GET"])
def temp():
    global  inputs
    global userId
    global userBoardId
    global columnId
    if request.method == 'POST':
        taskName = request.form['taskname']
        timedobedone = request.form['timedobedone']
        taskContent = request.form['taskContent']
        taskcolour = request.form['taskcolour']

        functions.add_task(conn, cur, userId, userBoardId, columnId, taskName, timedobedone, taskContent, taskcolour)
        return redirect(f'board\{userBoardId}')
    else :
        return render_template('temp.html' , inputs = inputs)

app.run(debug = True)
