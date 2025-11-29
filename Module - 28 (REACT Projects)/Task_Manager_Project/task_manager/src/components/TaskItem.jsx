function TaskItem({ task }) {
  return (
    <div className="w-[400px] p-4 border border-gray-200 rounded-xl shadow-sm bg-white hover:shadow-md transition-shadow duration-300">
  <h3 className="text-lg font-semibold text-gray-800 tracking-tight">
    {task.title}
  </h3>

  <p className="text-sm text-gray-500 mt-1 leading-relaxed">
    {task.description}
  </p>
</div>

  );
}

export default TaskItem;
