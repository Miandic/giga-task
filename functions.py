import psycopg2
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

def add_user(conn, cur, login, password, phn):
    if  conn == None or cur == None:
        conn, cur = set_connection(conn, cur)

    command = """INSERT INTO USERS(login, nickname, password, phonenumber) values(%s, %s, %s,%s)"""
    values = (login, login, password, int(phn))

    cur.execute(command, values)
