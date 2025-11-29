import './App.css'
import { BrowserRouter, Routes, Route, HashRouter, NavLink } from 'react-router-dom'
import Home from './components/home/Home.jsx'
import About from './components/about/About.jsx'
import { Link } from 'react-router-dom'
import Users from './users/Users.jsx'
import SingleUser from './users/SingleUser.jsx'

function App() {

  return (
    // BrowserRouter
    <BrowserRouter>
      <nav>
        {/* <Link to="/">Home</Link>
        <Link to="/about">About</Link> */}
        <NavLink className={({isActive}) => (isActive?'active-link' : 'inactive-link')} to="/">Home</NavLink>
        <NavLink to="/users">Users</NavLink>
        <NavLink to="/about">About</NavLink>
      </nav>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/users' element={<Users />} />
        <Route path='/users/:id' element={<SingleUser />} />
        <Route path='/about' element={<About />} />
      </Routes>
    </BrowserRouter>

    //HashRouter
    // <HashRouter>
    //   <Routes>
    //     <Route path='/' element={<Home />} />
    //     <Route path='/about' element={<About />} />
    //   </Routes>
    // </HashRouter>
  )
}

export default App
