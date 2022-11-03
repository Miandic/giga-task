import React from "react";
import Column from "./column"
import ColAddButton from "./coladdbutton"

export default function Board({board}, onChange){
    return (
        <div className="board">
            { board.cols.map(col => {
                if(!(col.colName === "upupdowndownleftrightleftrightAB")){
                    return <Column column={col} key={col.colId}/>
                }
                else{
                    return <ColAddButton />
                }
            })}
        </div>
    )
}