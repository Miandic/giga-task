import React from "react";

export default function ColAddButton(onChange){
    return (
        <div className="col-add" onClick={() => onChange(-1)}>
            <i className="fa-solid fa-plus"></i>
        </div>
    )
}