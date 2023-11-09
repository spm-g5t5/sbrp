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

import AdminApplicantsPage from "./pages/AdminApplicantsPage";
import AdminRolePage from  './pages/AdminRolePage'; 
import UpdateRoleListingPage from  './pages/UpdateRoleListingPage'; 
import AddJobPage from  './pages/AddJobPage';
import AdminSpecificApplicantsPage from "./pages/AdminSpecificApplicantsPage";
import ApplicantDetailsPage from "./pages/ApplicantDetailsPage";
import StaffApplicationPage from "./pages/StaffApplicationPage";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/AdminHomePage" element={<AdminHomePage />} />
      <Route path="/ManagerHomePage" element={<ManagerHomePage />} />
      <Route path="/AdminRolePage" element={<AdminRolePage />} />
      <Route path="/StaffRoleListingPage" element={<StaffRoleListingPage />} />
      <Route path="/AdminApplicantsPage" element={<AdminApplicantsPage />} />
      <Route path="/AdminSpecificApplicants" element={<AdminSpecificApplicantsPage />} />
      <Route path="/UpdateRoleListingPage" element={<UpdateRoleListingPage />} />
      <Route path="/ApplicantDetailsPage" element={<ApplicantDetailsPage />} />
      <Route path="/AddJobPage" element={<AddJobPage />} />
      <Route path="/StaffApplicationPage" element={<StaffApplicationPage />} />
      <Route path="*" element={<NoPage />} />
    </Routes>
  );
};

export default App;
