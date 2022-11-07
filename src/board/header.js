import React from "react";
import { useSelector, useDispatch } from 'react-redux'
import { changeBoardName } from "../store/boardSlice";

export default function Header() {
    const { board } = useSelector(state => state.board);
    const dispatch = useDispatch()

    return (
        <div className='header'>
            <div className='header-logo'>
                <img src="ggt-logo.png" alt="#" />
                <span>GigaTask</span>
            </div>
            <input type="text" name="board-name" value={board.name} onChange = {e => dispatch(changeBoardName({name: e.target.value}))} />
        </div>
    )
}