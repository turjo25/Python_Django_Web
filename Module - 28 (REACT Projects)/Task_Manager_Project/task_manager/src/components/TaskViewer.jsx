import { useState } from 'react';
import ModelForms from './ModelForms.jsx';
import TaskItem from './TaskItem.jsx';
function TaskViewer() {
    const [tasks, setTasks] = useState([]);

    const [isModelOpen, setIsModalOpen] = useState(false);

    function closeModal() {
        setIsModalOpen(false);
    }

    function addTask(event) {
        event.preventDefault();
        const tasktitle = event.target.tasktitle.value;
        const taskdesc = event.target.taskdesc.value;
        const taskid = tasks.length + 1;
        const task = {
            id: taskid,
            title: tasktitle,
            description: taskdesc
        }
        setTasks([...tasks, task]);
        closeModal();
    }

  return (
    <div className="flex flex-col items-center justify-center w-full mt-12">
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 w-fit border-2 rounded-2xl bg-blue-200 hover:bg-blue-400 cursor-pointer">
        Add Task
      </button>
      <div className='my-6 space-y-3'>
        {tasks.map((task, index) => (
            <TaskItem key={index} task={task} />
        ))}
      </div>
        {isModelOpen && (
            <ModelForms
            closeModal={closeModal}
            addTask={addTask}
            />
        )}
    </div>
  );
}

export default TaskViewer;
