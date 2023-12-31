import React, { useState, useEffect } from "react";
import axios, { all } from "axios";
import Header from "../components/Header";
import SearchBar from "../components/SearchBar";
import RoleSkills from "../components/RoleSkills";
import {
  Modal,
  Badge,
  CardBody,
  CardFooter,
  CardTitle,
  Container,
} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";
import { Row, Col } from "react-bootstrap";
import { BsFillXCircleFill } from "react-icons/bs";
import FilterRole from "../components/FilterRole";
import ProgressBar from "react-bootstrap/ProgressBar";
import {
  FaBuilding,
  FaBriefcase,
  FaPen,
  FaUser,
  FaRegSadCry,
} from "react-icons/fa";
import "../styles/AdminRolePage.css";

interface Role {
  role_id: number;
  role_name: string;
  department: string;
  job_description: string;
  expiry_dt: Date;
  job_type: string;
  original_creation_dt: Date;
  active_status: number;
  orig_role_listing: object;
  upd_dt: string;
  // Add other properties as needed
}

const StaffRoleListingPage = () => {
  const navigate = useNavigate();
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
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "1",
    10
  );
  const [showDetailModal, setDetailShowModal] = useState(false);
  const [allFilters, setAllFilters] = useState<{ [key: string]: any }>({});
  const [showSkillModal, setSkillShowModal] = useState(false);
  const [roleSkillMatch, setRoleSkillMatch] = useState<number>(0);
  const [staffMatchSkill, setStaffMatchSkill] = useState<[]>([]);
  const [staffUnmatchSkill, setStaffUnmatchSkill] = useState<[]>([]);
  const [roleListingSkill, setRoleListingSkill] = useState<[]>([]);
  const [isArrayEmpty, setIsArrayEmpty] = useState(false);
  const [staffApplication, setStaffApplication] = useState(new Set());

  const userDepartment = localStorage.getItem("DEPT");

  const [currentItem, setCurrentItem] = useState<{
    role_id: number;
    role_name: string;
    department: string;
    job_description: string;
    expiry_dt: Date;
    job_type: string;
    original_creation_dt: Date;
    upd_dt: string;
    // Add other properties as needed
  } | null>(null);

  const handleDetailCloseModal = () => setDetailShowModal(false);
  const handleSkillCloseModal = () => setSkillShowModal(false);

  const handleDetailShowModal = (item: {
    role_id: number;
    role_name: string;
    department: string;
    job_description: string;
    expiry_dt: Date;
    job_type: string;
    original_creation_dt: Date;
    upd_dt: string;
  }) => {
    item.expiry_dt = new Date(item.expiry_dt);
    item.original_creation_dt = new Date(item.original_creation_dt);
    setCurrentItem(item);
    setDetailShowModal(true);
  };
  const currentDate = new Date();
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/viewRoles")
      .then((response) => {
        if (Array.isArray(response.data)) {
          setData(response.data);
        } else {
          console.log("Response data is not an array.");
          setIsArrayEmpty(true);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  useEffect(() => {
    axios
      .post("http://127.0.0.1:5000/API/v1/getStaffApplication", {
        staff_id: staffId,
      })
      .then((response) => {
        setStaffApplication(new Set(response.data));
      });
  }, []);

  const handleDetail = (item: { role_id: number }) => {
    const roleId = item.role_id.toString(); // Convert number to string
    localStorage.setItem("RoleId", roleId);
    navigate("/ApplicantDetailsPage");
  };

  const [errorVisible, setErrorVisible] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const showErrorMessage = (message: any) => {
    setErrorMessage(message);
    setErrorVisible(true);
  };

  const hideErrorMessage = () => {
    setErrorVisible(false);
    setErrorMessage("");
  };
  

  const handleApplication = (item: any) => {
    axios
      .post("http://127.0.0.1:5000/API/v1/createApplication", {
        staff_id: staffId,
        role_id: item.role_id,
      })
      .then((response) => {
        if (Array.isArray(response.data) && response.data.length > 0) {
          console.log(response.data);
        } else if (response.data.error) {
          showErrorMessage(response.data.error);
          // Set your error state or do error handling here
        } else {
          console.error("Response data is empty.");
          // Set your error state or do error handling here
        }
      })
      .then(() => {
        // Chain the second Axios POST request here
        return axios.post("http://127.0.0.1:5000/API/v1/getStaffApplication", {
          staff_id: staffId,
        });
      })
      .then((response) => {
        setStaffApplication(new Set(response.data));
        console.log(response.data);
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

  const staffId = localStorage.getItem("StaffId");
  function onHandleSkills(item: Role) {
    axios
      .get("http://127.0.0.1:5000/API/v1/viewRoles/skill/" + item.role_id)
      .then((response) => {
        setRoleListingSkill(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });

    setSkillShowModal(true);
    axios
      .post("http://127.0.0.1:5000/API/v1/getRoleSkillMatch", {
        staff_id: staffId,
        role_id: item.role_id,
      })

      .then((response) => {
        setRoleSkillMatch(response.data.skill_match_pct);
        setStaffMatchSkill(response.data.skill_match);
        setStaffUnmatchSkill(response.data.staff_skills_unmatch);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }


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

  function onHandleClearFilter() {
    window.location.reload();
  }


  return (
    <div>
      <Header accessRights={accessRights} />

      {isArrayEmpty ? ( // Check if the data array is empty
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
          <Col>
            <SearchBar onSearch={handleSearch} />
          </Col>
          <Row>
            <Col md="8">
              {data.length > 0 ? (
                data.filter(
                  (item) =>
                    item.active_status == 1 &&
                    new Date(item.expiry_dt) > currentDate
                )
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
                        <div className="d-flex">
                          {staffApplication.has(item.role_id) ? (
                            <button className="remove-job-button">
                              Applied
                            </button>
                          ) : (
                            <button
                              className="apply-button"
                              onClick={(e) => {
                                e.stopPropagation();
                                handleApplication(item);
                              }}
                            >
                              Apply
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
                        <FaUser /> Last updated by on {item.upd_dt.slice(5, 22)}
                      </Card.Text>
                      {/* <button
                        className="view-applicants-button"
                        onClick={() => handleDetailShowModal(item)}
                      >
                        More details
                      </button> */}
                      <button
                        className="view-applicants-button"
                        onClick={(e) => {
                          e.stopPropagation();
                          onHandleSkills(item);
                        }}
                      >
                        View Skills
                      </button>
                    </CardBody>
                  </Card>
                ))): (
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

      {showDetailModal && (
        <Modal show={showDetailModal} onHide={handleDetailCloseModal}>
          <Modal.Header closeButton>
            <Modal.Title>{currentItem!.role_name}</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            Application Close Date:{" "}
            <p>{currentItem!.expiry_dt.toLocaleDateString()}</p>
            Job Description:<p>{currentItem!.job_description}</p>
            Job Type: <p>{currentItem!.job_type}</p>
            Creation Date and time:
            <p>{currentItem!.original_creation_dt.toLocaleDateString()}</p>
          </Modal.Body>
          <Modal.Footer>
            <button
              className="view-applicants-button"
              onClick={handleDetailCloseModal}
            >
              Close
            </button>
          </Modal.Footer>
        </Modal>
      )}

      {showSkillModal && (
        <Modal show={showSkillModal} onHide={handleSkillCloseModal}>
          <Modal.Header closeButton>
            <Modal.Title>Applicant's skills</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p>
              Role's needed skills:{" "}
              {roleListingSkill.map((RoleSkill: any) => (
                <Badge bg="primary">{RoleSkill.skill_name}</Badge>
              ))}
            </p>
            <p>
              Your skills:
              {staffMatchSkill.map((skill) => (
                <Badge bg="success">{skill}</Badge>
              ))}
              {staffUnmatchSkill.map((skill) => (
                <Badge bg="danger">{skill}</Badge>
              ))}
            </p>
            <p>
              Applicant's skills Match Percentage:
              <ProgressBar now={roleSkillMatch} label={`${roleSkillMatch}%`} />
            </p>
          </Modal.Body>
          <Modal.Footer>
            <button
              className="view-applicants-button"
              onClick={handleSkillCloseModal}
            >
              Close
            </button>
          </Modal.Footer>
        </Modal>
      )}

      {/* Error message pop-up */}
      {errorVisible && (
        <Modal show={errorVisible} onHide={hideErrorMessage}>
          <Modal.Header closeButton>
            <Modal.Title>Error</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p>{errorMessage}</p>
          </Modal.Body>
        </Modal>
      )}
    </div>
  );
};

export default StaffRoleListingPage;
