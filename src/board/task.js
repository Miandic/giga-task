import React from "react";

export default function Task({task, colId, changeTaskName, changeTaskText, changeTaskWorker}){
    return(
        <div className="task">
            <input className="task-name" type="text" name="taskName" value={task.rawName} onChange={e => changeTaskName(e.target.value, colId, task.rawId)} />
            <input className="task-text" type="text" name="taskText" value={task.rawText} onChange={e => changeTaskText(e.target.value, colId, task.rawId)} />
            <input className="task-worker" type="text" name="taskWorker" value={task.rawWorker} onChange={e => changeTaskWorker(e.target.value, colId, task.rawId)} />
        </div>
    )
}