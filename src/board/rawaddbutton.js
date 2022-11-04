import React from "react";

export default function RawAddButton({colId, onChange}) {
    return (
        <div className="raw-add" onClick={() => onChange(colId)}>
            <i className="fa-solid fa-plus"></i>
        </div>
    )
}