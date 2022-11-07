import React from "react";
import { addColumn } from "../store/boardSlice";
import { useDispatch } from 'react-redux'

export default function ColAddButton(){

    const dispatch = useDispatch();

    return (
        <div className="col-add" onClick={() => dispatch(addColumn())}>
            <i className="fa-solid fa-plus"></i>
        </div>
    )
}