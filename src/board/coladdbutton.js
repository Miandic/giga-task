import React from "react";

export default function ColAddButton({addColumn}){
    return (
        <div className="col-add" onClick={() => addColumn()}>
            <i className="fa-solid fa-plus"></i>
        </div>
    )
}