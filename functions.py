import psycopg2
from psycopg2 import sql
import psycopg2.extras
import secret

conn = None
cur = None
command = ""

def set_connection(conn, cur):
    conn = psycopg2.connect(user=secret.DBuser, password=secret.DBpassword,
                                  host=secret.DBhost,
                                  port=secret.DBport,
                                  database="alpha")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    return (conn , cur)
def close_connection(conn , cur):
        cur.close()
        conn.commit()

        if conn is not None:
                conn.close()

        return (conn , cur)

def get_values(cur):
    ans = []

    res = cur.fetchall()

    for value in res:
        ans.append(dict(value))

    return ans

def get_boards(conn, cur , userId):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """select * from boards where userId = %s """

    cur.execute(command, [userId])
    ans = get_values(cur)

    return ans

def get_tasks(conn ,cur, boardId):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """select * from tasks where boardId = %s """

    cur.execute(command, [userId])
    ans = get_values(cur)

    return ans


def get_users(conn, cur):

    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = "SELECT * From users"
    cur.execute(command)

    ans = get_values(cur)

    return ans
def get_board_user(conn , cur):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = """
        select taskName, taskColour, taskContent, tasks.id , tasks.timetobedone
        from tasks, boardColumn, boards
        where tasks.boardId = boards.id and boardColumn.posOnBoard = '1' and boardColumn.taskid = tasks.id
    """


def add_user(conn, cur, login, nickName,  password, phn):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """INSERT INTO USERS(login, nickname, password, phonenumber) values(%s, %s, %s,%s)"""
    values = (login, nickName, password, phn)

    cur.execute(command, values)
    conn.commit()


def add_task(conn, cur, userid, boardid, columnId, taskname, timetobedone, taskcontent, taskcolour):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = """INSERT INTO TASKS(userid, boardid, columnid, taskname, timetobedone, taskcontent, taskcolour) values(%s, %s,%s, %s, %s, %s, %s)"""
    values = (userid, boardid, columnId, taskname, timetobedone, taskcontent, taskcolour)

    cur.execute(command, values)
    conn.commit()


def add_boardColumn(conn, cur, name, boardid, posOnBoard ):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """INSERT INTO boardCOlumn(name, boardid, posOnBoard) values(%s, %s, %s)"""
    values = (name, taskid, boardid, posOnBoard)

    cur.execute(command, values)
    conn.commit()

def add_board_for_user(conn, cur, userId,  boardName):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """INSERT INTO Boards(userId, name, userright, columncnt ) VALUES(%s, %s, 'creator',  3) """
    values = (userId, boardName)
    cur.execute(command, values)

    conn.commit()

    cur.execute("select * from boards where userId = %s and  name = %s and userright = 'creator'" , [userId, boardName])
    conn.commit()

    board = get_values(cur)

    board = board[0]
    command =  """
    insert Into boardColumn(columnName, boardid, posOnBoard) values
    ('to-do', %s, 1),
    ('in-progress', %s, 2),
    ('done', %s, 3)
    """

    values = (board['id'], board['id'],board['id'])
    cur.execute(command,values)
    conn.commit()
    return board['id']

def edit_user(conn, cur, userid, login, nickname, password, phonenumber):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = """UPDATE Users
    set login = %s, nickname = %s, password = %s, phonenumber = %s
    where  id = %s
    """

    values = (login, nickname, password, phonenumber, userid)

    cur.execute(command, values)
    conn.commit()

def edit_board(conn ,cur, boardid ,  name, columncnt, userright, userid ):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = """UPDATE boards
    set name = %s, columncnt = %s, userright = %s, userid = %s
    where  id = %s
    """

    values = ( name, columncnt, userright, userid , boardid)

    cur.execute(command, values)
    conn.commit()

def edit_boardColumn(conn, cur, columnId, name, taskid, boardid, posOnBoard ):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)


    command = """UPDATE boards
    set columnname = %s, taskid = %s, boardid = %s, posOnBoard = %s
    where  id = %s
    """

    values = ( name, boardid, userright, boardid , posOnBoard, columnId )

    cur.execute(command, values)
    conn.commit()


def edit_tasks(conn, cur, taskId, userid, boardid, taskname, timetobedone, taskcontent, taskcolour ):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)
    command = """UPDATE boards
    set userid = %s, taskid = %s, boardid = %s, taskname = %s, timetobedone = %s, taskcontent = %s, taskcolour = %s
    where  id = %s
    """

    values = ( userid, boardid, userright, boardid, taskname, timetobedone, taskcontent, taskcolour, taskId    )

    cur.execute(command, values)
    conn.commit()

def delete(conn, cur, tableName, elementId):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = f"DELETE FROM {tableName} WHERE id = {elementId}"
    values = (elementId)

    cur.execute(command, values)
    conn.commit()

def getStatUser(conn, cur, boardId,  userId):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = f"""
        select columnname, id
        from boardColumn
        where boardid = {boardId}
    """

    cur.execute(command)
    columns = get_values(cur)
    stat = {}
    for column in columns:
        command = f"""
            select COUNT(*)
            from tasks
            where tasks.columnId = {column['id']} AND tasks.userid = {userId}
        """
        cur.execute(command)
        stat[column['columnname']] = cur.fetchall()[0][0]
