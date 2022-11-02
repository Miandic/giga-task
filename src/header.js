import React, { useState } from "react";


export default function Header() {
    const [boardName, setBoardName] = useState("Fix dynamic");

    return(
        <div className='header'>
            <div className='header-logo'>
                <img src="https://i.ebayimg.com/images/g/PFkAAOSwHjxeyKol/s-l1600.jpg" alt="#"/ >
                <span>GigaTask</span>
            </div>
            <input type="text" name="board-name" value={boardName} onChange={e => setBoardName(e.target.value)}></input> 
        </div>
    )
}