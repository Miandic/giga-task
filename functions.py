import psycopg2
import psycopg2.extras

conn = None
cur = None

command = ""

def set_connection(conn, cur):
    conn = psycopg2.connect(user="postgres", password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Poggers")
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

def get_users(conn, cur):
    conn, cur = set_connection(conn, cur)

    command = "SELECT * From users"
    cur.execute(command)

    ans = get_values(cur)

    return ans
