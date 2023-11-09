import React, { useEffect } from "react";
import { Navigate, Outlet, useNavigate } from "react-router-dom";
import UserCard from "../components/UserCard";
import "../styles/HomePage.css";

const AdminHomePage = () => {
  // You would retrieve access rights from local storage here
  const accessRights = localStorage.getItem("AccessRights");
  const navigate = useNavigate(); // Get the navigate function

  useEffect(() => {
    // Check access rights here
    if (accessRights !== "3") {
      // Redirect to the login page if access rights are not 3
      // This will take the user back to the login page
      navigate("/");
    }
  }, [accessRights, navigate]);

  return (
    <div className="container-center-vertically">
      {accessRights === "3" ? (
        <div className="row">

          <div className="col-xl-3 col-sm-6">
            <UserCard username="ST" />
          </div>
          <div className="col-xl-3 col-sm-6">
            <UserCard username="MA" />
          </div>

        </div>
      ) : (
        <Navigate to="/" />
      )}
      <Outlet />
    </div>
  );
};

export default AdminHomePage;
