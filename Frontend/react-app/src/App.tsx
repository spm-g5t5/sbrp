import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from './pages/LoginPage';
import AdminHomePage from './pages/AdminHomePage';
import StaffHomePage from './pages/StaffHomePage';
import ManagerHomePage from './pages/ManagerHomePage';
import NoPage from './pages/NoPage'; // Assuming 'NoPage' is a valid component

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
