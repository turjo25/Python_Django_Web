import { useState } from 'react';
import ModelForms from './ModelForms.jsx';
import TaskItem from './TaskItem.jsx';
import { loadTasksFromLocalStorage, saveTasksToLocalStorage } 
from '../utils/tasks.js';
import ModalUpdateForms from "./ModelUpdateForm";
function TaskViewer() {
    const [tasks, setTasks] = useState(loadTasksFromLocalStorage());

    const [isModelOpen, setIsModalOpen] = useState(false);

    const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);

    const[taskTobeUpdated, setTaskToBeUpdated] = useState(null);

    function closeModal() {
        setIsModalOpen(false);
    }

    function toggleTask(id){
      const updatedTasks = tasks.map((task) => {
          if (task.id === id) {
              return { ...task, isCompleted: !task.isCompleted };
          }
          return task;
      });
      setTasks(updatedTasks);
      saveTasksToLocalStorage(updatedTasks);
    }

    function deleteTask(id) {
        const updatedTasks = tasks.filter((task) => task.id !== id);
        setTasks(updatedTasks);
        saveTasksToLocalStorage(updatedTasks);
    }

    function addTask(event) {
        event.preventDefault();
        const tasktitle = event.target.tasktitle.value;
        const taskdesc = event.target.taskdesc.value;
        const taskid = tasks.length + 1;
        const task = {
            id: taskid,
            title: tasktitle,
            description: taskdesc,
            isCompleted: false,
        }
        setTasks([...tasks, task]);
        saveTasksToLocalStorage([...tasks, task]);
        closeModal();
    }

    function openModal(id) {
      const task = tasks.find((t) => t.id === id);
      setTaskToBeUpdated(task);
      setIsUpdateModalOpen(true);
    }

    function updateTask(event) {
      event.preventDefault();
      const updatedTitle = event.target.tasktitle.value;
      const updatedDesc = event.target.taskdesc.value;
      const updatedTasks = tasks.map((task) => {
          if (task.id === taskTobeUpdated.id) {
              return { ...task, title: updatedTitle, description: updatedDesc };
          } return task;
      });
      setTasks(updatedTasks);
      saveTasksToLocalStorage(updatedTasks);
      setIsUpdateModalOpen(false);
  }
  return (
    <div className="flex flex-col items-center justify-center w-full mt-12">
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 w-fit border-2 rounded-2xl bg-blue-200 hover:bg-blue-400 cursor-pointer">
        Add Task
      </button>
      <div className='my-6 space-y-3'>
        {tasks.map((task, index) => (
            <TaskItem key={index} task={task} deleteTask={deleteTask} toggleTask={toggleTask} openModal={openModal}/>
        ))}
      </div>
        {isModelOpen && (
            <ModelForms
            closeModal={closeModal}
            addTask={addTask}
            />
        )}
        {isUpdateModalOpen ? <ModalUpdateForms  task={taskTobeUpdated}
        closeModal={() => setIsUpdateModalOpen(false)} updateTask={updateTask}/> : <></>}
    </div>
  );
}

export default TaskViewer;
