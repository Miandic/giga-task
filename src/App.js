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
          }
        ],
        colId: 1
      },
      {
        colName: "upupdowndownleftrightleftrightAB"
      }
    ]
  })

  return (
    <div className='wrapper'>
      <Header board={board}/>
      <Board board={board}/>
    </div>
  );
}

export default App;
