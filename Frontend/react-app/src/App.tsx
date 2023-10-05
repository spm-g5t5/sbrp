import React from "react";
import { BrowserRouter, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import LoginPage from  './pages/LoginPage';
import AdminHomePage from  './pages/AdminHomePage';
import AdminRole from  './pages/AdminRole';
import { BrowserRouter as Router } from 'react-router-dom';


function App() {
  return (
    <div>
    <Router>
        {/* <LoginPage /> */}
        <AdminRole />
    </Router>,

    </div>
  );
}

export default App;
