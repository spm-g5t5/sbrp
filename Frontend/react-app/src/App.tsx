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
import StaffRoleListingPage from "./pages/StaffRoleListingPage";
import AdminApplicants from "./pages/AdminApplicants";
import AdminRole from  './pages/AdminRole'; 
import UpdateRoleListingPage from  './pages/UpdateRoleListingPage'; 
import AddJobPage from  './pages/AddJobPage';
import ApplicantPage from "./pages/ApplicantPage"; 

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="AdminHomePage" element={<AdminHomePage />} />
      <Route path="/ManagerHomePage" element={<ManagerHomePage />} />
      <Route path="/AdminRole" element={<AdminRole />} />
      <Route path="/StaffRoleListingPage" element={<StaffRoleListingPage />} />
      <Route path="/AdminApplicants" element={<AdminApplicants />} />
      <Route path="/UpdateRoleListingPage" element={<UpdateRoleListingPage />} />
      <Route path="/AddJobPage" element={<AddJobPage />} />
      <Route path="/ApplicantPage" element={<ApplicantPage />} />
      <Route path="*" element={<NoPage />} />
    </Routes>
  );
};

export default App;
