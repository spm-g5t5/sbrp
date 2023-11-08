import React, { useEffect, useState } from "react";
import { CardBody, CardText, CardTitle, Col, Row } from "react-bootstrap";
import axios from "axios";
import Badge from "react-bootstrap/Badge";
import Header from "../components/Header";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import ProgressBar from "react-bootstrap/ProgressBar";
import FilterApplicants from "../components/FilterApplicants";
import {
  FaBuilding,
  FaBriefcase,
  FaPen,
  FaUser,
  FaIdBadge,
  FaRegSadCry,
  FaEye,
  FaEyeSlash,
} from "react-icons/fa";

interface Applicant {
  application_id: number;
  applicant_staff_id: number;
  applicant_existing_role: string;
  applicant_existing_dept: string;
  application_status: string;
  date_applied: string;
  applied_role_id: number;
  role: {
    role_name: string;
  };
  staff: {
    staff_fname: string;
    staff_lname: string;
  };
  staff_skill: {
    skill_name: string;
  }[];
  role_skills: {
    skill_name: string;
  }[];
  // Add other properties as needed
}

interface RoleSkillMatch {
  staff_id: number;
  role_id: number;
  skill_match_pct: number;
  // Add other properties as needed
}

const AdminApplicantsPage = () => {
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10
  );
  const [showSkillModal, setSkillShowModal] = useState(false);
  const [data, setData] = useState<Applicant[]>([]);
  const [roleSkillMatch, setRoleSkillMatch] = useState<RoleSkillMatch[]>([]);
  const [currentItem, setCurrentItem] = useState<Applicant | null>(null);
  const [isArrayEmpty, setIsArrayEmpty] = useState(false);
  const [filteredSkill, setFilteredSkill] = useState<[]>([]);
  const [staffMatchSkill, setStaffMatchSkill] = useState<[]>([]);
  const [staffUnmatchSkill, setStaffUnmatchSkill] = useState<[]>([]);

  const handleDetailCloseModal = () => setSkillShowModal(false);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/viewApplicants")
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

  function onHandleSkills(item: Applicant) {
    setCurrentItem(item);
    setSkillShowModal(true);
    axios
      .post("http://127.0.0.1:5000/API/v1/getRoleSkillMatch", {
        staff_id: item.applicant_staff_id,
        role_id: item.applied_role_id,
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

  const handleDataFromFilter = (data: any) => {
    const skillArray = data.map(
      (obj: { id: number; value: string }) => obj.value
    );
    setFilteredSkill(skillArray);
  };

  function onHandleSubmitFilterButton() {
    console.log(filteredSkill);
    axios
      .post("http://127.0.0.1:5000/API/v1/viewApplicants", {
        skills: filteredSkill,
      })
      .then((response) => {
        if (Array.isArray(response.data) && response.data.length > 0) {
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
          <Col xl="8">
            {data.map((item) => (
              <Card
                style={{ margin: "30px" }}
                key={item.application_id.toString()}
              >
                <CardBody>
                  <div className="d-flex justify-content-between">
                    <div>
                      <Card.Title>Role: {item.role.role_name}</Card.Title>
                    </div>
                    <div className="d-flex">
                      <button
                        className="view-applicants-button"
                        onClick={() => onHandleSkills(item)}
                      >
                        View Skills
                      </button>
                    </div>
                  </div>
                  <Card.Text>
                    <FaUser /> Name: {item.staff.staff_fname}{" "}
                    {item.staff.staff_lname}
                  </Card.Text>
                  <Card.Text>
                    <FaIdBadge /> StaffID: {item.applicant_staff_id}
                  </Card.Text>
                  <CardText>
                    <FaBuilding /> Current department:{" "}
                    {item.applicant_existing_dept}
                  </CardText>
                  <CardText>
                    <FaBriefcase /> Current role: {item.applicant_existing_role}
                  </CardText>
                </CardBody>
              </Card>
            ))}
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
                <FilterApplicants
                  sendDataToApplicant={handleDataFromFilter}
                ></FilterApplicants>
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
      )}

      {showSkillModal && (
        <Modal show={showSkillModal} onHide={handleDetailCloseModal}>
          <Modal.Header closeButton>
            <Modal.Title>Applicant's skills</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p>
              Role's needed skills:{" "}
              {currentItem!.role_skills.map((RoleSkill) => (
                <Badge pill bg="primary" className="badge-margin">
                  {RoleSkill.skill_name}
                </Badge>
              ))}
            </p>
            <p>
              Applicant's skills:
              {staffMatchSkill.map((skill) => (
                <Badge pill bg="success" className="badge-margin">
                  {skill}{" "}
                </Badge>
              ))}
              {staffUnmatchSkill.map((skill) => (
                <Badge pill bg="warning" className="badge-margin">
                  {skill}
                </Badge>
              ))}
            </p>
            <p>
              Applicant's skills Match Percentage:
              <ProgressBar
                now={roleSkillMatch}
                label={`${roleSkillMatch}%`}
                className="custom-progress-bar"
              />
            </p>
          </Modal.Body>
        </Modal>
      )}
    </div>
  );
};

export default AdminApplicantsPage;
