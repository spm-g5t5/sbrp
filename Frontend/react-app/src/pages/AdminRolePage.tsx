import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import axios from "axios";
import Header from "../components/Header";
import SearchBar from "../components/SearchBar";
import RoleSkills from "../components/RoleSkills";
import FilterRole from "../components/FilterRole";
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
import { Navigate, Outlet, useNavigate, Link } from "react-router-dom";
import "../styles/AdminRolePage.css";
import {
  FaPlus,
  FaBuilding,
  FaBriefcase,
  FaPen,
  FaUser,
  FaRegSadCry,
  FaEye,
  FaEyeSlash,
} from "react-icons/fa";

const AdminRolePage = () => {
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
      upd_hiring_manager: {
        staff_fname: string;
        staff_lname: string;
      };
      upd_dt: string;
      // Add other properties as needed
    }[]
  >([]);
  const navigate = useNavigate();
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10
  );
  const [Applications, setApplications] = useState<{ [key: string]: any }>({});
  const [showApplicationModal, setApplicationShowModal] = useState(false);
  const [isArrayEmpty, setIsArrayEmpty] = useState(false);
  const [allFilters, setAllFilters] = useState<{ [key: string]: any }>({});

  const handleDetail = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    localStorage.setItem("RoleId", roleId);
    navigate("/ApplicantDetailsPage");
  };

  const currentDate = new Date();

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/viewRoles")
      .then((response) => {
        if (Array.isArray(response.data)) {
          setData(response.data);
          console.log(response.data);
        } else {
          console.log("Response data is not an array.");
          setIsArrayEmpty(true);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleViewApplications = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    localStorage.setItem("RoleId", roleId);
    navigate("/AdminSpecificApplicants");
  };

  const handleRemoveRole = (item: { role_id: number }) => {
    axios
      .get(`http://127.0.0.1:5000/API/v1/hideRole/${item.role_id}`)
      .then((response) => {
        setApplications(response.data);
        console.log(response.data);
        window.location.reload();
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  const handleUnHideRole = (item: { role_id: number }) => {
    axios
      .get(`http://127.0.0.1:5000/API/v1/unhideRole/${item.role_id}`)
      .then((response) => {
        setApplications(response.data);
        console.log(response.data);
        window.location.reload();
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  const handleUpdateRole = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    localStorage.setItem("RoleId", roleId);
    navigate("/UpdateRoleListingPage");
  };

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
  };

  // to check if object is empty
  function isObjectEmpty(obj: any) {
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        return false; // Object has at least one own property
      }
    }
    return true; // Object is empty (has no own properties)
  }

  const handleDataFromFilter = (data: any) => {
    if (isObjectEmpty(data)) {
      console.log("empty");
    } else {
      setAllFilters((prev) => ({
        ...prev,
        ...data,
      }));
    }
  };

  function onHandleSubmitFilterButton() {
    axios
      .post("http://127.0.0.1:5000/API/v1/searchRole", {
        skills: allFilters["skills"],
        department: allFilters["department"],
        jobtype: allFilters["jobtype"],
      })
      .then((response) => {
        if (Array.isArray(response.data)) {
          setData(response.data);
          console.log(response.data);
        } else {
          console.log("Response data is not an array.");
          setIsArrayEmpty(true);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }

  function onHandleClearFilter() {
    window.location.reload();
  }

  return (
    <div>
      <Header accessRights={accessRights} />

      {isArrayEmpty ? (
        <div>
          <Row>
            <Col xl="8">
              <span className="errormsg">
                <FaRegSadCry />
                No results found
                <FaRegSadCry />
              </span>
            </Col>
            <Col xl="4">
              <Card
                style={{
                  marginTop: "30px",
                  marginBottom: "30px",
                  marginRight: "30px",
                  marginLeft: "15",
                }}
              >
                <div className="filter-card">
                  <CardTitle>Filter For Applicant</CardTitle>
                  <button
                    className="view-applicants-button"
                    onClick={() => onHandleClearFilter()}
                  >
                    Clear filter
                  </button>
                </div>
              </Card>
            </Col>
          </Row>
        </div>
      ) : (
        <Row>
          <Col xs={12} xl={11}>
            <SearchBar onSearch={handleSearch} />
          </Col>

          <Col xs={12} xl={1}>
            <button
              className="add-job-button"
              onClick={() => navigate("/AddJobPage")}
            >
              <span>
                <FaPlus />
              </span>
            </button>
          </Col>

          <Row>
            <Col xl={8}>
              {data.length > 0 ? (
                data.map((item) => (
                  <Card
                    style={{
                      marginTop: "30px",
                      marginBottom: "30px",
                      marginLeft: "30px",
                      marginRight: "15",
                    }}
                    key={item.role_id.toString()}
                    onClick={() => handleDetail(item)}
                    className="clickable-card"
                    data-mdb-ripple-color="light"
                  >
                    <CardBody>
                      <div className="d-flex justify-content-between">
                        <div>
                          <CardTitle>{item.role_name}</CardTitle>
                          {new Date(item.expiry_dt) < currentDate ? (
                            <Badge pill bg="danger" className="badge-margin">
                              Expired
                            </Badge>
                          ) : (
                            <Badge pill bg="success" className="badge-margin">
                              Active
                            </Badge>
                          )}
                          {item.active_status ? (
                            <Badge pill bg="success" className="badge-margin">
                              Visible
                            </Badge>
                          ) : (
                            <Badge pill bg="danger" className="badge-margin">
                              Hidden
                            </Badge>
                          )}
                        </div>
                        <div className="d-flex">
                          <button
                            className="update-job-button"
                            onClick={(e) => {
                              e.stopPropagation(); // Prevent card click
                              handleUpdateRole(item);
                            }}
                          >
                            <span>Update</span>
                          </button>

                          {item.active_status ? (
                            <button
                              className="remove-job-button"
                              onClick={(e) => {
                                e.stopPropagation();
                                handleRemoveRole(item);
                              }}
                            >
                              <span>
                                <FaEyeSlash />
                              </span>
                            </button>
                          ) : (
                            <button
                              className="unhide-job-button"
                              onClick={(e) => {
                                e.stopPropagation();
                                handleUnHideRole(item);
                              }}
                            >
                              <span>
                                <FaEye />
                              </span>
                            </button>
                          )}
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
                        <FaUser /> Last updated by{" "}
                        {item.upd_hiring_manager.staff_fname}{" "}
                        {item.upd_hiring_manager.staff_lname} on{" "}
                        {item.upd_dt.slice(5, 22)}
                      </Card.Text>
                      <button
                        className="view-applicants-button"
                        onClick={(e) => {
                          e.stopPropagation(); // Prevent card click
                          handleViewApplications(item);
                        }}
                      >
                        View Applicants
                      </button>
                    </CardBody>
                  </Card>
                ))
              ) : (
                <div>
                  <span className="errormsg">
                    <FaRegSadCry />
                    No items to display
                    <FaRegSadCry />
                  </span>
                </div>
              )}
            </Col>
            <Col xl={4}>
              <Card
                style={{
                  marginTop: "30px",
                  marginBottom: "30px",
                  marginRight: "30px",
                  marginLeft: "15",
                }}
              >
                <div className="filter-card">
                  <CardTitle>Filter For Roles</CardTitle>
                  <FilterRole
                    sendDataToRoleListing={handleDataFromFilter}
                  ></FilterRole>
                  <button
                    className="filter-button"
                    onClick={onHandleSubmitFilterButton}
                  >
                    {" "}
                    Filter
                  </button>
                </div>
              </Card>
            </Col>
          </Row>
        </Row>
      )}
    </div>
  );
};

export default AdminRolePage;
