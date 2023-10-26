import React, { useEffect, useState, useContext} from 'react';
import { CardBody, CardHeader, CardSubtitle, CardText, Col, Container, Row } from 'react-bootstrap';
import axios from 'axios';
import Badge from 'react-bootstrap/Badge';
import Header from '../components/Header';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Filter from '../components/Filter';

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
    const accessRights = parseInt(localStorage.getItem("AccessRights") || '0', 10);
    const [showSkillModal, setSkillShowModal] = useState(false);
    const [data, setData] = useState<Applicant[]>([]);
    const [roleSkillMatch, setRoleSkillMatch] = useState<RoleSkillMatch[]>([]);
    const [currentItem, setCurrentItem] = useState<Applicant | null>(null);
    const [isArrayEmpty, setIsArrayEmpty] = useState(false);
    const [filteredSkill, setFilteredSkill] = useState<[]>([]); // Initialize as an empty array
    
    const handleDetailCloseModal = () => setSkillShowModal(false);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/viewApplicants')
          .then((response) => {
            if (Array.isArray(response.data)) {
              setData(response.data);
              
            } else {
              console.log("Response data is not an array.");
              setIsArrayEmpty(true)
            }

          })
          .catch((error) => {
            console.error('Error fetching data:', error);
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

        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    
    }

    const handleDataFromFilter = (data: any) => {
      const skillArray = data.map((obj:{ id: number; value: string }) => obj.value);
      setFilteredSkill(skillArray);
    
    }

    function onHandleSubmitFilterButton() {
      console.log(filteredSkill);
      axios.post('http://127.0.0.1:5000/API/v1/viewApplicants',{
        "skills": filteredSkill
      })
      .then((response) => {
        if (Array.isArray(response.data)) {
          setData(response.data);
          console.log(response.data);
          
        } else {
          console.log("Response data is not an array.");
          setIsArrayEmpty(true)
        }
      })
      .catch((error) => {
          console.error('Error fetching data:', error);
      });
    }

  return (
    <div>
       <Header accessRights={accessRights}/>
       <Row>
        <Col md='8'>
        {isArrayEmpty ? (
  <p>No applicants</p>
) : (
  data.map((item) => (
      <Card style={{ margin: '30px' }} key={item.application_id.toString()}>
        <CardHeader>
          <Card.Title>Application no.{item.application_id}</Card.Title>
          <CardSubtitle>Role: {item.role.role_name}</CardSubtitle>
        </CardHeader>
        <CardBody>
          <Card.Text>Name: {item.staff.staff_fname} {item.staff.staff_lname}</Card.Text>
          <CardText>Current department: {item.applicant_existing_dept}</CardText>
          <CardText>Current role: {item.applicant_existing_role}</CardText>
          <Button onClick={() => onHandleSkills(item)} variant="primary">View Skills</Button>
        </CardBody>
      </Card>
    
  ))
)}
        </Col>
        <Col md='4'>
          <Button onClick={onHandleSubmitFilterButton} style={{ margin: '30px' }} variant="primary">Filter</Button>
          <Filter sendDataToApplicant={handleDataFromFilter}></Filter>
        </Col>
       </Row>
       


    {showSkillModal && (
            <Modal show={showSkillModal} onHide={handleDetailCloseModal}>
              <Modal.Header closeButton>
                <Modal.Title>Applicant's skills</Modal.Title>
              </Modal.Header>
              <Modal.Body>

                <p>
                    Role's needed skills: {currentItem!.role_skills.map((RoleSkill)=>(
                        <Badge bg="primary">{RoleSkill.skill_name}</Badge>
                    ))}
                </p>
                <p>
                Applicant's skills: {currentItem!.staff_skill.map((StaffSkill)=>(
                    <Badge bg="success">{StaffSkill.skill_name}</Badge>
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
};

export default AdminApplicantsPage;
