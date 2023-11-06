// import React from 'react';

// const StaffRoleListingPage = () => {
//   return (
//     <div>
//       This is the staff role listing page
//     </div>
//   );
// }

// export default StaffRoleListingPage;
//#######################################################

import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "../components/Header";
import SearchBar from "../components/SearchBar";
import RoleSkills from "../components/RoleSkills";
import {
  Button,
  CardHeader,
  Modal,
  Badge,
  CardBody,
  CardFooter,
  CardTitle,
  Container,
} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { BsFillXCircleFill } from "react-icons/bs";
import { Navigate, Outlet, useNavigate } from "react-router-dom";
import {
  FaPlus,
  FaBuilding,
  FaBriefcase,
  FaPen,
  FaUser,
  FaRegSadCry,
  FaEye,
  FaEyeSlash
} from "react-icons/fa";
import 'bootstrap/dist/css/bootstrap.min.css';




const StaffRoleListingPage = () => {
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
  const navigate = useNavigate();
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10
  );
  // const [Applications, setApplications] = useState<{ [key: string]: any }>({});
  // const [showApplicationModal, setApplicationShowModal] = useState(false);
  // const [showDetailModal, setDetailShowModal] = useState(false);

  // const [currentItem, setCurrentItem] = useState<{
  //   role_id: number;
  //   role_name: string;
  //   department: string;
  //   job_description: string;
  //   expiry_dt: Date;
  //   job_type: string;
  //   original_creation_dt: Date;
  //   upd_dt: string;
  //   // Add other properties as needed
  // } | null>(null);

  const handleSearch = (searchText: string) => {
    const searchData = {
      search: searchText,
    };
    axios
      .post("http://127.0.0.1:5000/API/v1/searchRole", searchData)
      .then((response) => {
        setData(response.data);

      })
      .catch((error) => {
        console.error(error);
        console.log(error);
      });
    console.log(searchData)
  };

  const handleDetail = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    localStorage.setItem("RoleId", roleId);
    navigate("/ApplicantDetailsPage");
  };

  // const handleDetailCloseModal = () => setDetailShowModal(false);

  // const handleDetailShowModal = (item: {
  //   role_id: number;
  //   role_name: string;
  //   department: string;
  //   job_description: string;
  //   expiry_dt: Date;
  //   job_type: string;
  //   original_creation_dt: Date;
  // }) => {
  //   item.expiry_dt = new Date(item.expiry_dt);
  //   item.original_creation_dt = new Date(item.original_creation_dt);
  //   setCurrentItem(item);
  //   setDetailShowModal(true);
  // };

  // const currentDate = new Date();



  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/viewRoles")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleViewApplications = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    navigate('/StaffApplicationPage')
  }

  return (
    <div>
      <Header accessRights={accessRights} />
      <SearchBar onSearch={handleSearch} />
      <div className="container">
        <div className="row">
          <div className="col-8">


            {data
              .filter((item) => item.active_status == 1)
              .map((item) => (
                <Card
                  style={{ margin: "30px" }}
                  key={item.role_id.toString()}
                  onClick={() => handleDetail(item)}
                  className="clickable-card"
                  data-mdb-ripple-color="light"
                >
                  <CardBody>
                    <div className="d-flex justify-content-between">
                      <div>
                        <CardTitle>{item.role_name}</CardTitle>
                      </div>
                    </div>
                    <Card.Text>
                      <FaBuilding /> Department: {item.department}
                    </Card.Text>
                    <Card.Text>
                      <FaBriefcase /> Job Type: {item.job_type}
                    </Card.Text>
                    <Card.Text>
                      <FaPen /> Apply By:{" "}
                      {item.expiry_dt.toString().slice(5, 16)}
                    </Card.Text>
                    <Card.Text>
                      <FaUser /> Last updated by on{" "}
                      {/* {item.upd_dt.slice(5, 22)} */}
                    </Card.Text>
                    <button
                      className="view-applicants-button"
                      onClick={(e) => {
                        e.stopPropagation(); // Prevent card click
                        handleViewApplications(item);
                      }}
                    >
                      Apply
                    </button>
                    <RoleSkills item={item} />
                  </CardBody>
                  
 
                </Card>
              ))}

          </div>

          <div className="col-4 sidebar">
            <h2>Filters</h2>

          </div>
        </div>
      </div>
    </div>
  );
};

export default StaffRoleListingPage;
