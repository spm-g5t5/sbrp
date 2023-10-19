import React, { useState, useEffect } from "react";
import { Navigate, Outlet, useNavigate, useLocation } from "react-router-dom";
import Header from "../components/Header";
import axios from "axios";
import RoleSkills from "../components/RoleSkills";


const ApplicantDetailsPage = () => {
  const accessRights = parseInt(localStorage.getItem("AccessRights") || '0', 10);
  const roleId = parseInt(localStorage.getItem("RoleId") || '0', 10);
  const navigate = useNavigate(); // Get the navigate function
  const [data, setData] = useState<
    {
      role_id: number;
      role_name: string;
      department: string;
      job_description: string;
      expiry_dt: Date;
      job_type: string;
      original_creation_dt: Date;
      active_status: number;
      orig_role_listing: object;
      // Add other properties as needed
    }[]
  >([]);


  
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
      .get(`http://127.0.0.1:5000/API/v1/viewRoles/${roleId}`)
      .then((response) => {
        console.log(response.data);
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);


  // return (
  //   <div>
  //     <Header accessRights={accessRights} />
  //     {data.map((item) => (
  //       <div key={item.role_id.toString()}>
  //         <div> {item.role_name} </div>
  //         <div> {item.job_description} </div>
  //         <div> {item.expiry_dt.toString()} </div>
  //         <div> {item.original_creation_dt.toString()} </div>
  //         <RoleSkills key={item.role_name.toString()} item={item} />
  //       </div>
  //     ))}
  //   </div>
  // );

  return (
    <div>
      <Header accessRights={accessRights} />
      <div className="container-add-role">
        <h2 className="create-h2">Role Listing Details</h2>
        {data.length > 0 ? (
          <div>
            <div className="form-group">
              <label className="label">Role Name:</label>
              <span className="inputaddrole">{data[0].role_name}</span>
            </div>
  
            <div className="form-group">
              <label className="label">Department:</label>
              <span className="inputaddrole">{data[0].department}</span>
            </div>
  
            <div className="form-group">
              <label className="label">Job Type:</label>
              <span className="inputaddrole">{data[0].job_type}</span>
            </div>
  
            <div className="form-group">
              <label className="label">Job Description:</label>
              <textarea className="inputaddrole-textarea">{data[0].job_description}</textarea>
            </div>
  
            <div className="form-group">
              <label className="label">Expiry Date:</label>
              <span className="inputaddrole">{data[0].expiry_dt.toString()}</span>
            </div>
  
            <div className="form-group">
              <div className="skill-section">
                <label className="label"> Skills required:</label>
                <RoleSkills key={data[0].role_name.toString()} item={data[0]} />
              </div>
            </div>
          </div>
        ) : (
          <p>No data available</p>
        )}
      </div>
    </div>
  );
  
  
  
  
}

export default ApplicantDetailsPage;