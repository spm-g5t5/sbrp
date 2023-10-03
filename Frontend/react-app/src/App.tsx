import React from "react";
import "./App.css";
import { BrowserRouter, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import LoginPage from  './pages/LoginPage';
import AdminHomePage from  './pages/AdminHomePage';
import { BrowserRouter as Router } from 'react-router-dom';


function App() {
  return (
    <div className="App">
    <Router>
        <LoginPage />
    </Router>,
    </div>
  );
}

export default App;
