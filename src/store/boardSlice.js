import { createSlice } from '@reduxjs/toolkit'

export const boardSlice = createSlice({
  name: 'board',
  initialState: {
    board: {
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
      },
  },
  reducers: {
    addRaw: (state, action) => {
        const colId = action.payload.colId;
        let rawId = state.board.cols[colId].colRaws.length
        state.board.cols[colId].colRaws.pop()
        state.board.cols[colId].colRaws.push({
          rawName: "Task name",
          rawText: "Task text",
          rawWorker: "Task worker",
          rawId: rawId - 1
        })
        state.board.cols[colId].colRaws.push({
          rawName: "upupdowndownleftrightleftrightAB",
          rawId: rawId
        })
    },
    addColumn: (state) => {
        let colId = state.board.cols.length
        state.board.cols.pop()
        state.board.cols.push({
          colName: "Column",
          colRaws: [
            {
              rawName: "upupdowndownleftrightleftrightAB"
            }
          ],
          colId: colId - 1
        })
        state.board.cols.push({
          colName: "upupdowndownleftrightleftrightAB",
          colId: colId
        })
    },
    changeBoardName: (state, action) => {
        state.board.name = action.payload.name
    },
    changeColumnName: (state, action) => {
        state.board.cols[action.payload.colId].colName = action.payload.name
    },
    changeTaskName: (state, action) => {
        state.board.cols[action.payload.colId].colRaws[action.payload.rawId].rawName = action.payload.name
    },
    changeTaskText: (state, action) => {
        state.board.cols[action.payload.colId].colRaws[action.payload.rawId].rawText = action.payload.text
    },
    changeTaskWorker: (state, action) => {
        state.board.cols[action.payload.colId].colRaws[action.payload.rawId].rawWorker = action.payload.worker
    },
    deleteColumn: (state, action) =>{
        state.board.cols.splice(action.payload.colId, 1)
        for(let i = action.payload.colId; i < state.board.cols.length; i+=1){
            state.board.cols[i].colId -= 1
        }
    },
    deleteTask: (state, action) => {
        state.board.cols[action.payload.colId].colRaws.splice(action.payload.rawId, 1)
        for(let i = action.payload.rawId; i < state.board.cols[action.payload.colId].colRaws.length; i+=1){
          state.board.cols[action.payload.colId].colRaws[i].rawId -= 1
        }
    },
    moveTask: (state, action) => {
        let task = state.board.cols[action.payload.colIdCur].colRaws[action.payload.rawIdCur]
        task.rawId = state.board.cols[action.payload.colIdCur].colRaws.length - 1;
        state.board.cols[action.payload.colIdCur].colRaws.splice(action.payload.rawIdCur, 1)
        for(let i = action.payload.rawIdCur; i < state.board.cols[action.payload.colIdCur].colRaws.length; i+=1){
          state.board.cols[action.payload.colIdCur].colRaws[i].rawIdCur -= 1
        }
        state.board.cols[action.payload.colId].colRaws.splice( state.board.cols[action.payload.colIdCur].colRaws.length, 0, task);
        state.board.cols[action.payload.colId].colRaws[state.board.cols[action.payload.colId].colRaws.length - 1].rawId+=1;
    },
    moveColumn: (state, action) => {
        let column = state.board.cols[action.payload.colIdCur]
        column.colId = action.payload.colId
        state.board.cols.splice(action.payload.colIdCur, 1)
        for(let i = action.payload.colIdCur; i < state.board.cols.length; i+=1){
            state.board.cols[i].colIdCur -= 1
        }
        state.board.cols.splice(action.payload.colId, 0, column)
        for (let i = action.payload.colId+1; i < state.board.cols.length; i+=1){
            state.board.cols[i].colId += 1
        }
      }
  },
})

export const { addRaw, addColumn, changeBoardName, changeColumnName, changeTaskName, changeTaskText, changeTaskWorker, deleteColumn, deleteTask, moveTask, moveColumn } = boardSlice.actions

export default boardSlice.reducer