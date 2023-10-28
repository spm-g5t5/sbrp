import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
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
import { Navigate, Outlet, useNavigate, Link } from "react-router-dom";
import "../styles/AdminRolePage.css";
import {
  FaPlus,
  FaTimes,
  FaBuilding,
  FaBriefcase,
  FaPen,
  FaUser,
  FaRegSadCry,
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
        setData(response.data);
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
  return (
    <div>
      <Header accessRights={accessRights} />
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
      </Row>
      <Row>
        <Col xl={8}>
          {data.length > 0 ? (
            data
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
                        {item.expiry_dt > currentDate ? (
                          <Badge pill bg="danger">
                            Expired
                          </Badge>
                        ) : (
                          <Badge pill bg="success">
                            Active
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
                        <button
                          className="remove-job-button"
                          onClick={(e) => {
                            e.stopPropagation(); // Prevent card click
                            handleRemoveRole(item);
                          }}
                        >
                          <span>
                            <FaTimes />
                          </span>
                        </button>
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
        <Col xl={4}>Put Filter here</Col>
      </Row>

      {/* {showApplicationModal && (
        <Modal
          show={showApplicationModal}
          onHide={() => setApplicationShowModal(false)}
        >
          <Modal.Header closeButton>
            <Modal.Title>Applications</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p>Applicant by staff ID</p>
            {Object.keys(Applications).map((key: string) => (
              <li key={key}>{Applications[key].applicant_staff_id}</li>
            ))}
          </Modal.Body>
          <Modal.Footer>
            <Button
              style={{ backgroundColor: "#266C73" }}
              onClick={() => setApplicationShowModal(false)}
            >
              Close
            </Button>
          </Modal.Footer>
        </Modal>
      )} */}
    </div>
  );
};

export default AdminRolePage;
