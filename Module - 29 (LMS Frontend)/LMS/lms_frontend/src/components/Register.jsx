import React from 'react'
import { useAuth } from '../contexts/AuthProvider.jsx'

function Register() {
    const { register } = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const values = {
            username: e.target.userName.value,
            first_name: e.target.firstName.value,
            last_name: e.target.lastName.value,
            phone: e.target.phone.value,
            password: e.target.password.value,
        }
        await register(values)
    }

  return (
    <div className='w-full h-[80vh] flex flex-col justify-center items-center'>
        <p className='text-2xl font-bold mb-6'>Register</p>
        <form onSubmit={handleSubmit} className='flex flex-col gap-6 bg-gray-200 rounded-2xl p-12'>
            <input className='border px-4 py-2 rounded-md' name='firstName' type="text" placeholder='First Name' />
            <input className='border px-4 py-2 rounded-md' name='lastName' type="text" placeholder='Last Name' />
            <input className='border px-4 py-2 rounded-md' name="userName" type="text" placeholder='Username' />
            <input className='border px-4 py-2 rounded-md' name="phone" type="text" placeholder='Phone' />
            <input className='border px-4 py-2 rounded-md' name="password" type="password" placeholder='Password' />
            <input className='bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700' type="submit" value="Register" />
        </form>
        <a href="/login" className='mt-4 text-blue-600 hover:underline'>Already have an account? Login</a>
    </div>
  )
}

export default Register