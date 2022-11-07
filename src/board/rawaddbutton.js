import React from "react";
import { addRaw } from "../store/boardSlice";
import { useDispatch } from 'react-redux'

export default function RawAddButton({colId}) {

    const dispatch = useDispatch();

    return (
        <div className="raw-add" onClick={() => dispatch(addRaw({
            colId: colId
        }))}>
            <i className="fa-solid fa-plus"></i>
        </div>
    )
}