import React, { useState, useEffect } from "react";
import { Navigate, Outlet, useNavigate, useLocation } from "react-router-dom";
import Header from "../components/Header";
import axios from "axios";
import RoleSkills from "../components/RoleSkills";
import "../styles/ApplicantDetailsPage.css";
import { Row, Col } from "react-bootstrap";
import { FaRegClock, FaBuilding, FaBriefcase, FaCalendar, FaPen, FaUser} from "react-icons/fa";

const ApplicantDetailsPage = () => {
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10
  );
  const roleId = parseInt(localStorage.getItem("RoleId") || "0", 10);
  const navigate = useNavigate(); // Get the navigate function
  const [data, setData] = useState<
    {
      role_id: number;
      role_name: string;
      department: string;
      job_description: string;
      expiry_dt: Date;
      upd_dt: Date;
      job_type: string;
      original_creation_dt: Date;
      active_status: number;
      orig_role_listing: object;
      hiring_manager: {
        staff_fname:string;
        staff_lname: string;
      };
      // Add other properties as needed
    }[]
  >([]);

  // useEffect(() => {
  //   // Check access rights here
  //   if (accessRights !== 3) {
  //     // Redirect to the login page if access rights are not 3
  //     // This will take the user back to the login page
  //     navigate("/");
  //   }
  // }, [accessRights, navigate]);

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
      <div className="container-view-role">
        {data.length > 0 ? (
          <div>
            <h2 className="create-h2">{data[0].role_name}</h2>

            <div className="form-group">
              <label className="label"><FaBuilding/> Department:</label>
              <span className="view_role">{data[0].department}</span>
            </div>

            <div className="form-group">
              <label className="label"><FaBriefcase/> Job Type:</label>
              <span className="view_role">{data[0].job_type}</span>
            </div>

            <div className="form-group">
              <label className="label"><FaPen/> Apply By:</label>
              <span className="view_role">{data[0].expiry_dt.toString().slice(5, 16)}</span>
            </div>

            <div className="form-group">
              <label className="label"><FaUser/> Posted By:</label>
              <span className="view_role">{data[0].hiring_manager.staff_fname} {data[0].hiring_manager.staff_lname}</span>
            </div>

            <div className="form-group">
              <label className="label"><FaCalendar/> Posted On:</label>
              <span className="view_role">{data[0].original_creation_dt.toString().slice(5, 16)}</span>
            </div>
            <div className="form-group">
              <label className="label"><FaRegClock/> Last Updated On:</label>
              <span className="view_role">{data[0].upd_dt.toString().slice(5, 16)}</span>
            </div>

            <div className="form-group-job-description">
              <Row>
                <Col xl={2}>
                  <label className="label-description">Job Description:</label>
                </Col>
                <Col xl={10}>
                <span className="view-description">
                    {data[0].job_description}
                  </span>
                </Col>
              </Row>
            </div>

            <div className="form-group-skill-card">
              <label className="label-skill">Skills Required:</label>
              <span className="role-skill-card">
                <RoleSkills key={data[0].role_name.toString()} item={data[0]} />
              </span>
            </div>

          </div>
        ) : (
          <p>No data available</p>
        )}
      </div>
    </div>
  );
};

export default ApplicantDetailsPage;
