import { createContext, useContext, useEffect, useState } from 'react'
import { registerUser, loginUser, getCurrentUser } from '../services/authService';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

const AuthProvider = ({ children }) => {

  const [user, setUser] = useState(null);
  const [isAuthLoading, setIsAuthLoading] = useState(true);

    const register = async (userData) => {
        console.log("Register Function", userData);
        const res = await registerUser(userData);
        console.log(res);
    }

    const login = async (credentials) => {
        console.log("Login Function");
        const res = await loginUser(credentials);
        localStorage.setItem('token', res.token);
        localStorage.setItem('refresh', res.refresh);
        console.log(res);
    }

    const logout = () => {
        console.log("Logout Function");
        localStorage.removeItem('token');
        localStorage.removeItem('refresh');
        window.location.href = '/login';
        console.log("cleared");
    }

    const getUser = async () => {
        console.log("Get Current User Function");
        try {
            const res = await getCurrentUser();
            if(res?.user){
                setUser(res.user)
            } else {
                setUser(null)
                // if(window.location.pathname !== '/login'){
                //     window.location.href = '/login';
                // }
            }
        } catch (error) {
            console.log(error);
        }
        setIsAuthLoading(false);
    }

    useEffect(() => {
        // async function fetchUser() {
        //     await getUser();
        // }
        getUser();
    }, [user]);

    return (
        
        <AuthContext.Provider value={{ register, login, logout, getUser, user, isAuthLoading }}>
            {children}
        </AuthContext.Provider>
    )
};

export default AuthProvider;