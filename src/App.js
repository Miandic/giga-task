import React from 'react';
import Header from './board/header';
import Board from './board/board'

function App() {
  const [board, setBoard] = React.useState({
    name: "fix me pls", 
    cols: [
      {
        colName: "ToDo",
        colRaws: [
          {
            rawName: "Re-make DB",
            rawText: "Please develop new DB ASAP",
            rawWorker: "Stepankov",
            rawId: 0
          },
          {
            rawName: "New logo",
            rawText: "We need new one!",
            rawWorker: "Yoza",
            rawId: 1
          },
          {
            rawName: "upupdowndownleftrightleftrightAB",
            rawId: 2
          }
        ],
        colId: 0
      },
      {
        colName: "Doing",
        colRaws: [
          {
            rawName: "New front",
            rawText: "Rewrite front in React",
            rawWorker: "Miandic",
            rawId: 0
          },
          {
            rawName: "upupdowndownleftrightleftrightAB",
            rawId: 1
          }
        ],
        colId: 1
      },
      {
        colName: "upupdowndownleftrightleftrightAB",
        colId: 3
      }
    ]
  })

  function addRaw (colId) {
    let rawId = board.cols[colId].colRaws.length
    let newboard = {...board}
    newboard.cols[colId].colRaws.pop()
    newboard.cols[colId].colRaws.push({
      rawName: "Task name",
      rawText: "Task text",
      rawWorker: "Task worker",
      rawId: rawId - 1
    })
    newboard.cols[colId].colRaws.push({
      rawName: "upupdowndownleftrightleftrightAB",
      rawId: rawId
    })
    setBoard(newboard)
  }

  function addColumn() {
    let colId = board.cols.length
    let newboard = {...board}
    newboard.cols.pop()
    newboard.cols.push({
      colName: "Column",
      colRaws: [
        {
          rawName: "upupdowndownleftrightleftrightAB"
        }
      ],
      colId: colId - 1
    })
    newboard.cols.push({
      colName: "upupdowndownleftrightleftrightAB",
      colId: colId
    })
    setBoard(newboard)
  }

  function changeBoardName(name){
    let newboard = {...board}
    newboard.name = name
    setBoard(newboard)
  }

  function changeColumnName(name, colId){
    let newboard = {...board}
    newboard.cols[colId].colName = name
    setBoard(newboard)
  }

  function changeTaskName(name, colId, rawId){
    let newboard = {...board}
    newboard.cols[colId].colRaws[rawId].rawName = name
    setBoard(newboard)
  }

  function changeTaskText(text, colId, rawId){
    let newboard = {...board}
    newboard.cols[colId].colRaws[rawId].rawText = text
    setBoard(newboard)
  }

  function changeTaskWorker(worker, colId, rawId){
    let newboard = {...board}
    newboard.cols[colId].colRaws[rawId].rawWorker = worker
    setBoard(newboard)
  }

  function deleteColumn(colId){
    let newboard = {...board}
    console.log(newboard.cols)
    newboard.cols.splice(colId, 1)
    for(let i = colId; i < newboard.cols.length; i+=1){
      newboard.cols[i].colId -= 1
    }
    console.log(newboard.cols)
    setBoard(newboard)
  }

  function deleteTask(colId, rawId){
    let newboard = {...board}
    newboard.cols[colId].colRaws.splice(rawId, 1)
    for(let i = rawId; i < newboard.cols[colId].colRaws.length; i+=1){
      newboard.cols[colId].colRaws[i].rawId -= 1
    }
    setBoard(newboard)
  }

  return (
    <div className='wrapper'>
      <Header board={board} onChange={changeBoardName}/>
      <Board
        board={board}
        addRaw={addRaw}
        addColumn={addColumn}
        changeColumnName={changeColumnName}
        changeTaskName={changeTaskName}
        changeTaskText={changeTaskText}
        changeTaskWorker={changeTaskWorker}
        deleteTask={deleteTask}
        deleteColumn={deleteColumn}
        />
    </div>
  );
}

export default App;
