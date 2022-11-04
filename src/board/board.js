import React from "react";
import Column from "./column"
import ColAddButton from "./coladdbutton"

export default function Board({board, addRaw, addColumn, changeColumnName, changeTaskName, changeTaskText, changeTaskWorker, deleteTask, deleteColumn}){
    return (
        <div className="board">
            { board.cols.map(col => {
                if(!(col.colName === "upupdowndownleftrightleftrightAB")){
                    return <Column column={col} add={addRaw} key={col.colId} onChange={changeColumnName} changeTaskName={changeTaskName} changeTaskText={changeTaskText} changeTaskWorker={changeTaskWorker} deleteTask={deleteTask} deleteColumn={deleteColumn}/>
                }
                else{
                    return <ColAddButton addColumn={addColumn} key={1337}/>
                }
            })}
        </div>
    )
}