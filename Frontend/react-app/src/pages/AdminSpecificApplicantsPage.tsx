import React, { useState, useEffect } from "react";
import { Navigate, Outlet, useNavigate, useLocation } from "react-router-dom";
import Header from "../components/Header";
import axios from "axios";

const AdminSpecificApplicantsPage = () => {
    const accessRights = parseInt(localStorage.getItem("AccessRights") || '0', 10);
    const roleId = parseInt(localStorage.getItem("RoleId") || '0', 10);
    const navigate = useNavigate(); // Get the navigate function

    const [data, setData] = useState()
  
  useEffect(() => {
    // Check access rights here
    if (accessRights !== 3) {
      // Redirect to the login page if access rights are not 3
      // This will take the user back to the login page
      navigate("/");
    }
  }, [accessRights, navigate]);

  useEffect(() => {
  axios
  // to call backend api viewRole/role/${roleId}
      .get(`http://127.0.0.1:5000/API/v1/viewApplicants/role/${roleId}`)
      .then((response) => {
        console.log(response.data);
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);


  return (
    <div>
      {data}
    </div>
  );
}

export default AdminSpecificApplicantsPage;