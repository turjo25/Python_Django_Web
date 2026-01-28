import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './components/Home.jsx'
import Login from './components/Login.jsx'
import Register from './components/Register.jsx'
import Courses from './components/Courses.jsx'
import AuthProvider from './contexts/AuthProvider.jsx'
import Navbar from './components/Navbar.jsx'
import Admin from './components/Admin.jsx'
import CourseDetails from './components/CourseDetails.jsx'

function App() {

  return (
      <AuthProvider>
        <Navbar/>
        <BrowserRouter>
          <Routes>
            <Route path='/' exact element={<Home />} />
            <Route path='/login' element={<Login />} />
            <Route path='/register' element={<Register />} />
            <Route path='/admin' element={<Admin />} />
            <Route path='/courses' element={<Courses />} />
            <Route path='/courses/:id' element={<CourseDetails />} />
            {/* <Route path='*' element={<div>404 Not Found</div>} /> */}
          </Routes>
        </BrowserRouter>
      </AuthProvider>
  )
}

export default App
