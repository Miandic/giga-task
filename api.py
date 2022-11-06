from flask import Flask, jsonify, request
import secret
import functions
import unicodedata
import json
app = Flask(__name__)

@app.route('/getBoard', methods = ['GET'])
def getBoard(charset = 'utf-8'):
    boardId = request.args.get('id')
    conn, cur = None, None
    conn, cur = functions.set_connection(conn ,cur)
    ansData = dict()
    cur.execute("SELECT * from boards where id = %s ",  [boardId])
    board = functions.get_values(cur)
    board = board[0]
    tasks = []
    ansData['name'] = board['name']
    print(ansData['name'])
    ansData['cols'] = []
    #get all columns from base for this board
    command = ("""
        select columnName, posOnBoard, boardColumn.id
        from boardColumn
        where boardColumn.boardId = %s
        ORDER BY posOnBoard
    """)
    cur.execute(command, [boardId])
    columns = functions.get_values(cur)
    print(columns)
    for i in range(0, len(columns)):
        #get tasks for column in base
        command = """
            select taskName, taskColour, taskContent, tasks.id , tasks.timetobedone
            from tasks
            where tasks.boardId = %s and tasks.columnid = %s
        """
        cur.execute(command, [boardId, columns[i]['id']])

        tasks.append(functions.get_values(cur))

    for i in range(0, len(columns)):
        colDict = dict()
        colDict['colName'] = columns[i]['columnname']
        colDict['colRaws'] = []
        colDict['coldId'] = columns[i]['posonboard']

        for x in range(0, len(tasks[i])):
            colDict['colRaws'].append({'rawName' : tasks[i][x]['taskname'] , 'rawText' : tasks[i][x]['taskcontent'], 'rawID' : tasks[i][x]['id']})
        ansData['cols'].append(colDict)
    print(ansData)

    return ansData

app.run(debug = False)
