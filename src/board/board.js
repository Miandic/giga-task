import React from "react";
import Column from "./column"
import ColAddButton from "./coladdbutton"

export default function Board({board, addRaw}){
    return (
        <div className="board">
            { board.cols.map(col => {
                console.log(col)
                if(!(col.colName === "upupdowndownleftrightleftrightAB")){
                    return <Column column={col} add={addRaw} key={col.colId}/>
                }
                else{
                    return <ColAddButton key={1337}/>
                }
            })}
        </div>
    )
}