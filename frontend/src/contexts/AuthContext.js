import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext(null);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [user, setUser] = useState(null);

  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/login', {
        grant_type:'password',
        username:username,
        password:password,
        scope:"",
        'AuthContext.jsclient_id':'string',
        client_secret:'string',
      },{headers: {
          'Content-Type': 'multipart/form-data'
        }});
      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      setToken(access_token);
      await fetchUserProfile();
    } catch (error) {
      throw new Error('Ошибка входа');
    }
  };

  const register = async (email, username, password) => {
    try {
      await axios.post('http://localhost:8000/api/auth/register', {
        email,
        username,
        password
      });
    } catch (error) {
      throw new Error('Ошибка регистрации');
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  const fetchUserProfile = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/user/profile', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setUser(response.data);
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  const value = {
    token,
    user,
    login,
    register,
    logout,
    fetchUserProfile
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}; 