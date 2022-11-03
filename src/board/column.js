import React from "react";
import Task from "./task"

export default function Column({column}, onChange){

    return(
        <div className="column">
            <input className="column-name" type="text" name="column-name" value={column.colName} onChange = {() => onChange()}/>
            { column.colRaws.map( raw => {
                return <Task task={raw} key={raw.rawId}/>
            })}
        </div>
    )

}