import './App.css'
import TaskViewer from './components/TaskViewer.jsx'
function App() {

  return (
    <div className='p-4 max-w-5xl mx-auto'>
      <h1 className='text-5xl font-semibold text-center'>Task Manager App</h1>
      <TaskViewer />
    </div>
  )
}

export default App
