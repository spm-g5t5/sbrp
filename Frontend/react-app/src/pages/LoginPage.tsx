import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import logoWave from '../assets/logo_wave_design.png';
import '../App.css'; // Import a CSS file for component-specific styles

const Login: React.FC = () => {
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

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.email && !formData.password) {
      setError('Email and password are required');
    } else if (!formData.email) {
      setError('Email is required');
    } else if (!formData.password) {
      setError('Password is required');
    } else {
      // Store the email in local storage
      setError('');
      localStorage.setItem('email', formData.email);
      // Navigate to AdminHomePage or display a success message here
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

export default Login;
