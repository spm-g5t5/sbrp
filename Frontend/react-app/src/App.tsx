import React from "react";
import ReactDOM from "react-dom";
import {
  BrowserRouter,
  createBrowserRouter,
  Route,
  Routes,
  RouterProvider,
} from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import AdminHomePage from "./pages/AdminHomePage";
import ManagerHomePage from "./pages/ManagerHomePage";
import NoPage from "./pages/NoPage"; // Assuming 'NoPage' is a valid component

import AdminApplicants from "./pages/AdminApplicants";
import AdminRole from  './pages/AdminRole';        

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="AdminHomePage" element={<AdminHomePage />} />
      <Route path="/ManagerHomePage" element={<ManagerHomePage />} />
      <Route path="/AdminRole" element={<AdminRole />} />
      <Route path="/AdminApplicants" element={<AdminApplicants />} />
      <Route path="*" element={<NoPage />} />
    </Routes>
  );
};

export default App;
