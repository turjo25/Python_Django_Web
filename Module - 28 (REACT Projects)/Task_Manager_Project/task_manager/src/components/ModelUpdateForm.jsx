function ModelUpdateForms({ closeModal, task, updateTask }) {
  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex justify-center items-center p-4 z-50">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-2xl p-6 border border-gray-200 animate-scaleIn">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">
          Update Task
        </h2>

        <form onSubmit={updateTask} className="flex flex-col gap-3">
          <input defaultValue={task.title}
            name="tasktitle"
            type="text"
            placeholder="Enter task name"
            className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500" required
          />
          <textarea defaultValue={task.description}
            name="taskdesc"
            placeholder="Enter task description"
              className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500" required
            />

        
          <button
            type="submit"
            className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white"
          >
            Update Task
          </button>

          <button
            onClick={() => closeModal()}
            className="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 text-gray-800"
          >
            Cancel
          </button>
        </form>
      </div>
    </div>
  );
}

export default ModelUpdateForms;

/* Optional Tailwind animation */
/* Add in global CSS: 
@keyframes scaleIn { from { transform: scale(.9); opacity: 0;} to { transform: scale(1); opacity: 1;} }
.animate-scaleIn { animation: scaleIn .25s ease-out; }
*/
