import React from "react";
import RawAddButton from "./rawaddbutton";
import Task from "./task"
import { useDispatch, useSelector } from 'react-redux'

import { changeColumnName, deleteColumn, changeTaskName,moveTask } from "../store/boardSlice";

export default function Column({column}){

    const dispatch = useDispatch();
    const { dragTarget } = useSelector(state => state.dnd);


    return(
        <div className="column" onDrop={
            (e) => {
                e.preventDefault();
                dispatch(moveTask({
                    colIdCur: dragTarget.colId,
                    rawIdCur: dragTarget.rawId,
                    colId: column.colId,
                    rawId: 0
                }))
            }
        }
        onDragOver={e => e.preventDefault()}
        >
            <input className="column-name" type="text" name="column-name" value={column.colName} onChange={e => dispatch(changeColumnName({
                name: e.target.value,
                colId: column.colId
            }))}/>
            <i className="fa-solid fa-trash-can" onClick={() => dispatch(deleteColumn({
                colId: column.colId
            }))}></i>
            { column.colRaws.map( raw => {
                if (!(raw.rawName === "upupdowndownleftrightleftrightAB")){
                    return <Task task={raw} changeTaskName={changeTaskName} colId={column.colId} key={raw.rawId}/>
                }
                else{
                    return <RawAddButton colId={column.colId} key={column.colId}/>
                }
            })}
        </div>
    )
}