import React, { useEffect } from "react";
import { Navigate, Outlet, useNavigate } from "react-router-dom";
import UserCard from "../components/UserCard";
import "../styles/HomePage.css";

const StaffHomePage = () => {
  // You would retrieve access rights from local storage here
  const accessRights = localStorage.getItem("AccessRights");
  const navigate = useNavigate(); // Get the navigate function

  useEffect(() => {
    // Check access rights here
    if (accessRights !== "1") {
      // Redirect to the login page if access rights are not 3
      // This will take the user back to the login page
      navigate("/");
    }
  }, [accessRights, navigate]);

  return (
    <div className="container center-vertically">
      {accessRights === "1" ? (
        <div className="row">
          <div className="col-sm-4"></div>
          <div className="col-sm-4">
            <UserCard username="ST" />
          </div>
          <div className="col-sm-4"></div>
        </div>
      ) : (
        <Navigate to="/" />
      )}
      <Outlet />
    </div>
  );
};

export default StaffHomePage;
