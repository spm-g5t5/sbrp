import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.png';
import logoWave from '../assets/logo_wave_design.png';
import '../styles/Login.css'; // Import a CSS file for component-specific styles

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
      // Store the email in local storage
      setError('');
          // Check for "admin" or "staff" in the email
      const emailParts = formData.email.split('@');
      if (emailParts.length === 2) {
        const domain = emailParts[1].toLowerCase();
        if (domain.includes('admin')) {
          // Store the identity as "admin"
          localStorage.setItem('identity', 'admin');
          return routeAdmin();
        } else if (domain.includes('staff')) {
          // Store the identity as "staff"
          localStorage.setItem('identity', 'staff');
          return routeStaff();
        } else {
          setError('You are not a registered user');
        };
      }
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
