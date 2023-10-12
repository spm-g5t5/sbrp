import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.png';
import logoWave from '../assets/logo_wave_design.png';
import '../App.css'; // Import a CSS file for component-specific styles
import axios from 'axios';


const LoginPage = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [error, setError] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    setError('');
  };

  let navigate = useNavigate(); 
  const routeAdmin = () =>{ 
    let path = `./AdminHomePage`; 
    navigate(path);
  }

  const routeStaff = () =>{ 
    let path = `./StaffHomePage`; 
    navigate(path);
  }
  const routeManager = () =>{ 
    let path = `./AdminHomePage`; 
    navigate(path);
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.email && !formData.password) {
      setFormData({
        email: '',
        password: ''
      });  
      setError('Email and password are required');
    } else if (!formData.email) {
      setFormData({
        email: '',
        password: ''
      });  
      setError('Email is required');
    } else if (!formData.password) {
      setFormData({
        email: '',
        password: ''
      });  
      setError('Password is required');
    } else {
      axios.post('http://127.0.0.1:5000/API/v1/login', null, {
        headers: {
          user: formData.email,
          password: formData.password,
        },
      })
      .then((response) => {
        if (response.data.login_status === 1) {
          // Successful login, store access rights
          let staffId = response.data.staff.staff_id
          let accessRights = response.data.staff.access_rights
          localStorage.setItem('StaffId', staffId);
          localStorage.setItem('AccessRights', accessRights);
          // Direct into the correct webpage
          // If user is admin, route to admin page
          if(accessRights == 3){
            return routeAdmin()
          }
          // If user is manager, route to manager page
          else if (accessRights == 2){
            return routeManager()
          }
          // If user is staff, route to staff page
          else if (accessRights == 1){
            return routeStaff()
          }
          
        } else if (response.data.login_status === 0) {
          setError('Login failed');
        } else if (response.data.login_status === -1){
          setError('Access rights issue. Please contact IT help desk');
        }
        
      })
      .catch((error) => {
        console.error('Error logging in:', error);
        setError('Login failed');
      });
    }
  };

  return (
    <div className="login-container">
    <div className="company-logo-container">
      <div className='company-logo'>
        <img src={logo} alt="Company Logo" />
      </div>
      <div className="company-text">
        All-In-One
      </div>
      <div className="company-logo-design">
        <img src={logoWave} alt="Additional Image" />
      </div>
    </div>
      <div className="login-form">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <label>Email:</label>
            <br /> 
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="styled-input"
            />
          </div>
          <div className="input-container">
            <label>Password:</label>
            <br /> 
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="styled-input"
            />
          </div>
          {error && (
            <div className="alert alert-danger" role="alert">
              {error}
            </div>
          )}

          <button type="submit" className="styled-button">
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
