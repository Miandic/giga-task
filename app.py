from flask import Flask, redirect, request, render_template, make_response
import psycopg2
import functions
import requests
import secret
#from bot import getChat


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

"""
def sendAlarm(user, message):
    chat = getChat(user)
    if chat == 'Sorry':
        print('Aboba')
        return 'AlarmOff'
    else:
        url = "https://api.telegram.org/bot" + secret.TOKEN + "/sendMessage?chat_id=" + str(chat) + "&text=" + message
        res = requests.get(url)
        print(res)
"""
#sendAlarm(8, 'Ебать ты...')


'''
———————————No Data Bases?———————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————
'''


@app.route('/', methods=['GET', 'POST'])
def index(name=None, nick=None, create='true', other = None):
    #проверка по кукам что аккаунт войдён
    #если нет, то\
    global userId
    if (request.cookies.get('login') != None):
        #check cookie in base
        flag = False
        name = request.cookies.get('login')
        users = functions.get_users(conn, cur)
        for user in users:
            if user['login'] == name:
                nick = user['nickname']
                userId = user['id']
                flag = True
        #ifdata from cookie dont exsist in baseredirect on login
        if (not flag):
            return redirect('/login')

        boards = functions.get_boards(conn, cur, userId)
        if request.method == 'POST':
            #if create new autoName for new board
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
#variable 'creator' for check out boards in page and return pagewith boadrs
        return  render_template('index.html', name=name, nick=nick, boards=boards, create=create, other=other)
    else:

        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login(valid= None):
    global userId
    if request.method == 'POST':
        #get from page
        tempLogin = request.form['login']
        tempPassword = request.form['password']
#get all users to check data pageswith base
        users = functions.get_users(conn, cur)
        for user in users:
            if user['login'] == tempLogin and user['password'] == tempPassword:
#set cookies ifdata is right
                resp = make_response(redirect('/'))
                resp.set_cookie('login',  tempLogin )
                resp.set_cookie('password', tempPassword)

                userId = user['id']
                return resp
        else:
            #check for validinput
            valid = 'Invalid'
            return render_template('login.html', valid=valid)
    else:
        return render_template('login.html', valid=valid)


@app.route('/reg', methods=['GET', 'POST'])
def reg(name = None):
    if  request.method == 'POST':
        #gets all data from reg
        tempLogin = request.form['login']
        tempPassword = request.form['password']
        tempPhone = request.form['phone']
        #andcreate attribute with this database
        functions.add_user(conn, cur, tempLogin, tempLogin, tempPassword, tempPhone)
        return redirect('/login')
    else:
        return render_template('reg.html')


@app.route('/logout')
def logout():
#reset cookie for logout
    resp.set_cookie('login',  '' )
    resp.set_cookie('password', '')
    return redirect('/login')


@app.route('/board/<boardId>', methods= ['GET' , "POST"])
def board(boardId):
    #get allneededvariable
    global conn
    global cur
    global inputs
    global userBoardId
    global columnId
    global userId
    #set boardId and set connection
    userBoardId = boardId
    conn, cur = functions.set_connection(conn ,cur)

    #get board attribute from base
    cur.execute("SELECT * from boards where id = %s ",  [boardId])
    board = functions.get_values(cur)
    board = board[0]
    tasks = []

#get all columns from base for this board
    command = ("""
        select columnName, posOnBoard, boardColumn.id
        from boardColumn
        where boardColumn.boardId = %s
        ORDER BY posOnBoard
    """)
    cur.execute(command, [boardId])
    columns = functions.get_values(cur)

    for i in range(1, int(board['columncnt']) +1):
        #get tasks for column inbase
        command = """
            select taskName, taskColour, taskContent, tasks.id , tasks.timetobedone
            from tasks
            where tasks.boardId = %s  and tasks.columnid = %s
        """
        cur.execute(command, [userBoardId, columns[i-1]['id']])
        tasks.append(functions.get_values(cur))
    if request.method == 'POST':
        print("Хуй")
        flag = False
        try:
            posonboard = int(request.form['addColumn']) + 1
            flag = True
            print("t1")
        except Exception as e:
            flag = False
            print("e1")

        if flag:
            print("посонборд")
            print(posonboard)
            for column in columns:
                if int(column['posonboard']) >= posonboard:
                    functions.edit_boardColumn(conn, cur, column['id'], column['columnname'], userBoardId, int(column['posonboard']) + 1 )
                    print(column)
            print("член")
            functions.edit_board(conn ,cur, board['id'],  board['name'], int(board['columncnt']) + 1, board['userright'], board['userid'] )
            print("большоё")
            functions.add_boardColumn(conn, cur, 'Новая колонка', userBoardId, posonboard)
            print("неплох")
            return redirect('/board/' + str(boardId))

        flag = False
        try:
            columnId = request.form['columnId']
            flag = True
            print("t2")
        except Exception as e:
            flag = False
            print("e2")

        if flag:
            print("колумнид")
            print(columnId)
            return render_template('board.html', board=board, columns=columns, tasks=tasks, flag=flag)
        else:
            taskName = request.form['taskname']
            timedobedone = request.form['timetobedone']
            taskContent = request.form['taskContent']
            taskcolour = request.form['taskcolour']
            userLogin = request.form['login']
            users = functions.get_users(conn, cur)
            for user in users:
                if user['login'] == userLogin:
                    functions.add_task(conn, cur, user['id'], userBoardId, columnId, taskName, timedobedone, taskContent, taskcolour)
                    return redirect('/board/' + str(boardId))
            print(boardId, columnId)

        return redirect('/board/' + str(boardId))
    return render_template('board.html', board=board, columns=columns, tasks=tasks)

app.run(debug = True)
