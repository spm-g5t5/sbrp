import React, { useEffect, useState} from 'react';
import { CardBody, CardHeader, CardSubtitle, CardText, Container, Col, ListGroup, Row, Badge, Card, Button, Modal } from 'react-bootstrap';
import axios from 'axios';
import Header from '../components/Header';


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

const AdminApplicantPage = () => {
    const [showSkillModal, setSkillShowModal] = useState(false);
    const [data, setData] = useState<Applicant[]>([]);
    const [roleSkillMatch, setRoleSkillMatch] = useState()
    const [currentItem, setCurrentItem] = useState<Applicant | null>(null);
    
    const handleDetailCloseModal = () => setSkillShowModal(false);

    const filterMenuOptions = {
      Size: ["XS", "S", "M", "L", "XL"],
      Color: ["Red", "Green", "Blue", "Black", "White"],
  };

  const [selectedFilterOption, setSelFilterOption] = useState(
      Object.keys(filterMenuOptions)[0]
  );

  // Maintain separate state arrays for Size and Color options
  const [sizeOptions, setSizeOptions] = useState<string[]>([]);
  const [colorOptions, setColorOptions] = useState<string[]>([]);

  const handleCheckboxSelect = (option) => {
    if (selectedFilterOption === "Color") {
        setColorOptions((prevOptions) => {
            if (prevOptions.includes(option)) {
                return prevOptions.filter((item) => item !== option);
            } else {
                return [...prevOptions, option];
            }
        });
    } else if (selectedFilterOption === "Size") {
        setSizeOptions((prevOptions) => {
            if (prevOptions.includes(option)) {
                return prevOptions.filter((item) => item !== option);
            } else {
                return [...prevOptions, option];
            }
        });
    }
};

const handleFilterOptionChange = (newFilterOption) => {
    // Clear the selected checkbox states when the filter option changes
    setSizeOptions([]);
    setColorOptions([]);
    setSelFilterOption(newFilterOption);
};

useEffect(() => {
    console.log(`Selected Size Options: ${sizeOptions}`);
    console.log(`Selected Color Options: ${colorOptions}`);
    // You can perform additional actions here
}, [sizeOptions, colorOptions]);

    
    

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/viewApplicants')
          .then((response) => {
            setData(response.data);

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
            console.log(response.data.skill_match_pct);
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
        });
    
    }

  return (
    <div>
       <Header />
        <Row>
        <Col md={8}>
        {data.map((item) => (
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
      
          }
          </Col>
          <Col md={4}>
          <Container>
    <Row style={{ minWidth: "30vw" }}>
        <Col>
            <ListGroup variant="flush">
                {Object.keys(filterMenuOptions).map((fKey, id) => (
                    <ListGroup.Item
                        key={id}
                        action
                        active={selectedFilterOption === fKey}
                        onClick={() => handleFilterOptionChange(fKey)}
                        style={{ backgroundColor: "#266C73" }}
                    >
                        {fKey}
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Col>
        <Col>
            <ListGroup>
                {filterMenuOptions[selectedFilterOption].map((option, id) => (
                    <Row key={id}>
                        <Col xs="2">
                            <input
                                type="checkbox"
                                checked={
                                    selectedFilterOption === "Size"
                                        ? selectedSizeOptions.includes(option)
                                        : selectedColorOptions.includes(option)
                                }
                                onChange={() => handleCheckboxSelect(option)}
                            />
                        </Col>
                        <Col>
                            <p>{option}</p>
                        </Col>
                    </Row>
                ))}
            </ListGroup>
        </Col>
    </Row>
</Container>

          </Col>
        </Row>
    {showSkillModal && (
    <Modal>
        {roleSkillMatch}
    </Modal>
    )}

    {showSkillModal && (
            <Modal show={showSkillModal} onHide={handleDetailCloseModal}>
              <Modal.Header closeButton>
                <Modal.Title></Modal.Title>
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
                Applicant's skills Match Percentage: {roleSkillMatch}%
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

export default AdminApplicantPage;
