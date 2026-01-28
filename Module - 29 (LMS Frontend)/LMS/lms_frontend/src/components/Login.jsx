import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthProvider.jsx';

function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    const values = {
      phone: e.target.phone.value,
      password: e.target.password.value,
    };
    try {
        await login(values);
        navigate('/');
    } catch (error) {
        
    }
    

  };
  return (
    <div className='w-full h-[70vh] flex flex-col justify-center items-center'>
      <p className='text-2xl font-bold mb-6'>Login</p>
      <form onSubmit={handleSubmit} className='flex flex-col gap-6 bg-gray-200 rounded-2xl p-12'>
        <input className='border px-4 py-2 rounded-md' name="phone" type="text" placeholder="Phone" />
        <input className='border px-4 py-2 rounded-md' name="password" type="password" placeholder="Password" />
        <input className='bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700' type="submit" value="Login" />
      </form>
      <a href="/register" className='mt-4 text-blue-600 hover:underline'>Don't have an account? Register</a>
    </div>
  );
}

export default Login;
