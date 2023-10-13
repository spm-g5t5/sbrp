import React from "react";
import { BrowserRouter, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import LoginPage from  './pages/LoginPage';
import AdminHomePage from  './pages/AdminHomePage';
import AdminRole from  './pages/AdminRole';
import { BrowserRouter as Router } from 'react-router-dom';
import AdminApplicants from "./pages/AdminApplicants";


function App() {
  return (
    <div>
      <Router>
          {/* <LoginPage /> */}
          <AdminApplicants/>
      </Router>

    </div>
  );
}

export default App;
