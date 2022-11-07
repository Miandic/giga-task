import React from "react";
import { changeTaskText, changeTaskName, changeTaskWorker, deleteTask } from "../store/boardSlice"
import { setDragTarget } from "../store/dndSlice";
import { useDispatch } from 'react-redux'

export default function Task({task, colId}){

    const dispatch = useDispatch();


    return(
        <div className="task" draggable onDragStart={e => dispatch(setDragTarget({
            dragTarget: {
                colId: colId,
                rawId: task.rawId
            }
            }))}
            onDragEnd={e => dispatch(setDragTarget({
                dragTarget: null
            }))}
        >
            <input className="task-name" type="text" name="taskName" value={task.rawName} onChange={e => dispatch(changeTaskName({
                name: e.target.value,
                colId: colId,
                rawId: task.rawId
            }))} />
            <input className="task-text" type="text" name="taskText" value={task.rawText} onChange={e => dispatch(changeTaskText({
                text: e.target.value,
                colId: colId,
                rawId: task.rawId
            }))} />
            <input className="task-worker" type="text" name="taskWorker" value={task.rawWorker} onChange={e =>dispatch(changeTaskWorker({
                worker: e.target.value,
                colId: colId,
                rawId: task.rawId
            }))} />
            <i className="fa-solid fa-trash-can" onClick={() => dispatch(deleteTask({
                colId: colId,
                rawId: task.rawId
            }))}></i>
        </div>
    )
}