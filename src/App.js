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
            rawName: "upupdowndownleftrightleftrightAB"
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
            rawName: "upupdowndownleftrightleftrightAB"
          }
        ],
        colId: 1
      },
      {
        colName: "upupdowndownleftrightleftrightAB"
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
      rawId: rawId-1
    })
    newboard.cols[colId].colRaws.push({
      rawName: "upupdowndownleftrightleftrightAB"
    })
    setBoard(newboard)
    console.log(board)
  }

  return (
    <div className='wrapper'>
      <Header board={board}/>
      <Board board={board} addRaw={addRaw} />
    </div>
  );
}

export default App;
