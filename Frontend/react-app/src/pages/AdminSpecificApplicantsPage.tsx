import React, { useState, useEffect } from "react";
import { Navigate, Outlet, useNavigate, useLocation } from "react-router-dom";
import Header from "../components/Header";
import axios from "axios";
import { Modal, Button } from "react-bootstrap";
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';
import { CardBody, CardHeader, CardSubtitle, CardText, ProgressBar } from 'react-bootstrap';
import { FaRegSadCry } from "react-icons/fa";
import { Row, Col } from "react-bootstrap";

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


const AdminSpecificApplicantsPage = () => {
  
    const accessRights = parseInt(localStorage.getItem("AccessRights") || '0', 10);
    const roleId = parseInt(localStorage.getItem("RoleId") || '0', 10);
    const navigate = useNavigate(); // Get the navigate function

    const [showSkillModal, setSkillShowModal] = useState(false);
    const [data, setData] = useState<Applicant[]>([]); // Initialize as an empty array
    const [roleSkillMatch, setRoleSkillMatch] = useState<RoleSkillMatch[]>([]);
    const [currentItem, setCurrentItem] = useState<Applicant | null>(null);
    const handleDetailCloseModal = () => setSkillShowModal(false);
    const [isArrayEmpty, setIsArrayEmpty] = useState(false);
    const [staffMatchSkill, setStaffMatchSkill] = useState<[]>([]);
    const [staffUnmatchSkill, setStaffUnmatchSkill] = useState<[]>([]);
  
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
        if (Array.isArray(response.data)) {
          setData(response.data);
          console.log(response.data)
          
        } else {
          console.log("Response data is not an array.");
          setIsArrayEmpty(true)
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);


  function onHandleSkills(item: Applicant) {
    setCurrentItem(item);
    setSkillShowModal(true);
    axios.post('http://127.0.0.1:5000/API/v1/getRoleSkillMatch', {
        "staff_id": item.applicant_staff_id,
        "role_id": item.applied_role_id
    })
    .then((response) => {
      setRoleSkillMatch(response.data.skill_match_pct);
      setStaffMatchSkill(response.data.skill_match);
      setStaffUnmatchSkill(response.data.staff_skills_unmatch);

    })
    .catch((error) => {
        console.error('Error fetching data:', error);
    });

}

function onHandleClearFilter() {
  window.location.reload();
}
  return (
    <div>
    <Header accessRights={accessRights}/>
   
    {isArrayEmpty ? (
        <div>
           <button className="view-applicants-button" onClick={() => onHandleClearFilter()}>
             Clear filter
           </button>
           <span className="errormsg">
             <FaRegSadCry />
             No Applicants
             <FaRegSadCry />
           </span>
         </div>
    ) : (
      <Row>
      <Col xl="8">
      {data.map((item) => (
        <Card style={{ margin: "30px" }} key={item.application_id.toString()}>
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
              Name: {item.staff.staff_fname} {item.staff.staff_lname}
            </Card.Text>
            <Card.Text>StaffID: {item.applicant_staff_id}</Card.Text>
            <CardText>
              Current department: {item.applicant_existing_dept}
            </CardText>
            <CardText>
              Current role: {item.applicant_existing_role}
            </CardText>
          </CardBody>
        </Card>
      ))}
      </Col>
  <Col xl={4}>Filter here</Col>
</Row>
    )}
  





 {showSkillModal && (
         <Modal show={showSkillModal} onHide={handleDetailCloseModal}>
           <Modal.Header closeButton>
             <Modal.Title>Skills</Modal.Title>
           </Modal.Header>
           <Modal.Body>
           <p>
                  Role's needed skills: {currentItem!.role_skills.map((RoleSkill)=>(
                      <Badge bg="primary">{RoleSkill.skill_name}</Badge>
                  ))}
                </p>
                <p>
                Applicant's skills:
                {staffMatchSkill.map((skill)=>(
                    <Badge bg="success">{skill}</Badge>
                ))}
                {staffUnmatchSkill.map((skill)=>(
                    <Badge bg="danger">{skill}</Badge>
                ))}
                </p>
              <p>
             Applicant's skills Match Percentage: 
             <ProgressBar now={roleSkillMatch} label={`${roleSkillMatch}%`} />
             </p>
             
           </Modal.Body>
           <Modal.Footer>
             <Button
               style={{ backgroundColor: "#266C73" }}
               onClick={handleDetailCloseModal}
             >
               Close
             </Button>
           </Modal.Footer>
         </Modal>
       )}

 </div>
  );
}

export default AdminSpecificApplicantsPage;