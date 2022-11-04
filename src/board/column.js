import React from "react";
import RawAddButton from "./rawaddbutton";
import Task from "./task"

export default function Column({column, add}){

    return(
        <div className="column">
            <input className="column-name" type="text" name="column-name" value={column.colName}/>
            { column.colRaws.map( raw => {
                if (!(raw.rawName === "upupdowndownleftrightleftrightAB")){
                    return <Task task={raw} key={raw.rawId}/>
                }
                else{
                    return <RawAddButton colId={column.colId} key={column.colId} onChange={add}/>
                }
            })}
        </div>
    )
}