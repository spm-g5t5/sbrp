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
  CardTitle
} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";
import {Row, Col} from "react-bootstrap";
import Filter from "../components/FilterRole";
import ProgressBar from "react-bootstrap/ProgressBar";
import { FaRegSadCry } from "react-icons/fa";


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
  // Add other properties as needed
}

const StaffRoleListingPage = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<Role[]>([]);
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
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

  const [currentItem, setCurrentItem] = useState<{
    role_id: number;
    role_name: string;
    department: string;
    job_description: string;
    expiry_dt: Date;
    job_type: string;
    original_creation_dt: Date;
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



  const handleApplication = () => {
    navigate('/StaffApplicationPage')
  }

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
    if (isObjectEmpty(data)){
      console.log("empty")
    }else{
      setAllFilters((prev) => ({
        ...prev,
        ...data,
      }));
    }

  }

  function onHandleSubmitFilterButton() {
    axios.post('http://127.0.0.1:5000/API/v1/searchRole',{
      "skills": allFilters["skills"],
      "department": allFilters["department"],
      "jobtype":  allFilters["jobtype"]
    })
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
        console.error('Error fetching data:', error);
    });
  }

  const staffId = localStorage.getItem('StaffId');
  function onHandleSkills(item: Role) {

    axios.get('http://127.0.0.1:5000/API/v1/viewRoles/skill/'+item.role_id)
    .then((response) => {
      setRoleListingSkill(response.data);
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });

    setSkillShowModal(true);
    axios.post('http://127.0.0.1:5000/API/v1/getRoleSkillMatch', {
        "staff_id": staffId,
        "role_id": item.role_id
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
      <Header accessRights={accessRights} />
      <SearchBar />
      {isArrayEmpty ? ( // Check if the data array is empty
      <div>
        <button className="view-applicants-button" onClick={() =>onHandleClearFilter()}>Clear filter</button>
      <span className="errormsg">
        <FaRegSadCry />
        No Applicants
        <FaRegSadCry />
      </span>
    </div> // Display "No applicants" if the array is empty
    ) : (
      <Row>
      <Col md='8'>
        
        {data
          .filter((item) => item.active_status == 1 && new Date(item.expiry_dt) > currentDate)
          .map((item) => (
            <Card style={{ margin: "30px" }} key={item.role_id.toString()}>
             
              <CardBody>
              <CardTitle>{item.role_name}</CardTitle>
                Department: {item.department}
                <RoleSkills key={item.role_name.toString()} item={item} />
              </CardBody>
              <CardFooter>
                <button
                  className="view-applicants-button"
                  onClick={() => handleDetailShowModal(item)}
                >
                  More details
                </button>
                <button
                  className="view-applicants-button"
                  onClick={() => handleApplication()}
                >
                  Apply
                </button>
                <button
                  className="view-applicants-button"
                  onClick={() => onHandleSkills(item)}
                >
                  View Skills
                </button>
              </CardFooter>
            </Card>
          ))}
          </Col>  
          <Col md='4'>
          <button className="view-applicants-button"  onClick={onHandleSubmitFilterButton}> Filter</button>
          <Filter sendDataToRoleListing={handleDataFromFilter}></Filter>
          </Col>
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
                  Role's needed skills: {roleListingSkill.map((RoleSkill)=>(
                      <Badge bg="primary">{RoleSkill.skill_name}</Badge>
                  ))}
              </p>
              <p>
                Your skills: 
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
              <button
                className="view-applicants-button"
                onClick={handleSkillCloseModal}
              >
                Close
              </button>
            </Modal.Footer>
          </Modal>
          
      )}
      </div>
 
  );
};

export default StaffRoleListingPage;
