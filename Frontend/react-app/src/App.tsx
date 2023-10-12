import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import LoginPage from './pages/LoginPage';
import AdminHomePage from './pages/AdminHomePage';
import StaffHomePage from './pages/StaffHomePage';
import ManagerHomePage from './pages/ManagerHomePage';
import NoPage from './pages/NoPage'; // Assuming 'NoPage' is a valid component
import LoginPage from  './pages/LoginPage';
import AdminHomePage from  './pages/AdminHomePage';
import AdminRole from  './pages/AdminRole';


const App = () => {
  return (
      <Routes>
        <Route path="/" element={<LoginPage />}/>
        <Route path="AdminHomePage" element={<AdminHomePage />} />
        <Route path="/StaffHomePage" element={<StaffHomePage />} />
        <Route path="/ManagerHomePage" element={<ManagerHomePage />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
  );
}

export default App;
