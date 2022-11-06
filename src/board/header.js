import React from "react";

export default function Header({board, onChange}) {
    return (
        <div className='header'>
            <div className='header-logo'>
                <img src="ggt-logo.png" alt="#" />
                <span>GigaTask</span>
            </div>
            <input type="text" name="board-name" value={board.name} onChange = {e => onChange(e.target.value)} />
        </div>
    )
}