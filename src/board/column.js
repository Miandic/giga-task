import React from "react";
import RawAddButton from "./rawaddbutton";
import Task from "./task"

export default function Column({column, add, onChange, changeTaskName, changeTaskText, changeTaskWorker, deleteTask, deleteColumn}){

    return(
        <div className="column">
            <input className="column-name" type="text" name="column-name" value={column.colName} onChange={e => onChange(e.target.value, column.colId)}/>
            <i className="fa-solid fa-trash-can" onClick={() => deleteColumn(column.colId)}></i>
            { column.colRaws.map( raw => {
                if (!(raw.rawName === "upupdowndownleftrightleftrightAB")){
                    return <Task task={raw} changeTaskName={changeTaskName} changeTaskText={changeTaskText} changeTaskWorker={changeTaskWorker} deleteTask={deleteTask} colId={column.colId} key={raw.rawId}/>
                }
                else{
                    return <RawAddButton colId={column.colId} key={column.colId} onChange={add}/>
                }
            })}
        </div>
    )
}