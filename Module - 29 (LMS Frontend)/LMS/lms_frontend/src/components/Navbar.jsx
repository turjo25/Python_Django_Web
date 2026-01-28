import React from 'react';
import { useAuth } from '../contexts/AuthProvider.jsx';

function Navbar() {
    const { logout, user } = useAuth();
    console.log(user);
    
  return (
    <nav className="w-full flex items-center justify-between p-4 border-b border-gray-200">
      <h1>My LMS</h1>
      <ul className="flex space-x-4">
        <li className="p-2 rounded-md cursor-pointer hover:bg-gray-100 font-semibold"><a href="/">Dashboard</a></li>
        <li className="p-2 rounded-md cursor-pointer hover:bg-gray-100 font-semibold"><a href="/courses">Courses</a></li>
        <li className="p-2 rounded-md cursor-pointer hover:bg-gray-100 font-semibold"><a href="/profile">Profile</a></li>
      </ul>
      <button onClick={logout} className="bg-red-600 text-white p-2 rounded-md cursor-pointer hover:bg-red-700">Logout</button>
    </nav>
  );
}

export default Navbar;