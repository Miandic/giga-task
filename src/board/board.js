import React from "react";
import Column from "./column"
import ColAddButton from "./coladdbutton"
import { useSelector, useDispatch } from 'react-redux'

export default function Board(){
    const { board } = useSelector(state => state.board);
    return (
        <div className="board">
            { board.cols.map(col => {
                if(!(col.colName === "upupdowndownleftrightleftrightAB")){
                    return <Column column={col} key={col.colId} />
                }
                else{
                    return <ColAddButton key={1337}/>
                }
            })}
        </div>
    )
}