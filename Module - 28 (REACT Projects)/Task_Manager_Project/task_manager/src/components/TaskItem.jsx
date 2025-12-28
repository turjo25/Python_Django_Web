import ModalUpdateForms from "./ModelUpdateForm";
import { useState } from "react";
function TaskItem({ task, deleteTask, toggleTask, openModal }) {
  
  return (
    <div className="flex justify-between items-center w-[400px] p-4 border border-gray-200 rounded-xl shadow-sm bg-white hover:shadow-md transition-shadow duration-300">
      <div className="flex items-center">
        <input
          type="checkbox"
          className="w-5 h-5 mr-4"
          checked={task.isCompleted} onChange={() => toggleTask(task.id)}
        ></input>
        <div>
          <h3 className={`text-lg font-semibold text-gray-800 tracking-tight ${task.isCompleted ? 'line-through' : ''}`}>
            {task.title}
          </h3>

          <p className="text-sm text-gray-500 mt-1 leading-relaxed">
            {task.description}
          </p>
        </div>
      </div>

      <div className="flex gap-2">
      <button
        onClick={()=>openModal(task.id)}
        className="bg-blue-500 text-white px-3 py-1 rounded-md"
      >
        Update
      </button>
      <button
        onClick={() => deleteTask(task.id)}
        className="bg-red-500 text-white px-3 py-1 rounded-md"
      >
        Delete
      </button>
      </div>
      
    </div>
  );
}

export default TaskItem;
