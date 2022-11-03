import React from "react";

export default function Task({task}, onChange){
    return(
        <div className="task">
            <input className="task-name" type="text" name="taskName" value={task.rawName} onChange={() => onChange()} />
            <input className="task-text" type="text" name="taskText" value={task.rawText} onChange={() => onChange()} />
            <input className="task-worker" type="text" name="taskWorker" value={task.rawWorker} onChange={() => onChange()} />
        </div>
    )
}