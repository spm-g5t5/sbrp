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
} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { BsFillXCircleFill } from "react-icons/bs";
import { Navigate, Outlet, useNavigate,Link } from "react-router-dom";

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
    localStorage.setItem('RoleId', roleId);
    navigate('/ApplicantDetailsPage');

  }

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
    localStorage.setItem('RoleId', roleId);
    navigate('/AdminSpecificApplicants');

  }

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
    localStorage.setItem('RoleId', roleId);
    navigate('/UpdateRoleListingPage');

  }

  const handleSearch = (searchText: string) => {
    const searchData = {
      search: searchText,
    };
    axios.post('http://127.0.0.1:5000/API/v1/searchRole', searchData)
    .then(response => {
      setData(response.data);
      
    })
    .catch(error => {
      console.error(error);
    });

  }
  console.log(data)

  return (
    <div>
      <Header accessRights={accessRights} />
      <div className='adminsearchbar'>
      <SearchBar onSearch={handleSearch} />
      <Button onClick={() => navigate("/AddJobPage")} variant="success">
        <span>Add Job</span>
      </Button>
      </div>
      {data
        .filter((item) => item.active_status == 1)
        .map((item) => (
          <Card style={{ margin: "30px" }} key={item.role_id.toString()}>
            <CardHeader className="d-flex justify-content-between">
              <div>
                <CardTitle>{item.role_name}</CardTitle>    
                {item.expiry_dt > currentDate ? (
                  <Badge bg="danger">Expired</Badge>
                ) : (
                  <Badge>Active</Badge>
                )}
              </div>
              <div className="d-flex">
                <Button
                  onClick={() => handleUpdateRole(item)}
                  variant="warning"
                >
                  <span>Update</span>
                </Button>
                <Button onClick={() => handleRemoveRole(item)} variant="danger">
                  <span>Remove</span>
                  <BsFillXCircleFill />
                </Button>
              </div>
            </CardHeader>
            <CardBody>
              Department: {item.department}
            </CardBody>
            <CardFooter>
              <Button
                style={{ backgroundColor: "#266C73" }}
                onClick={() => handleViewApplications(item)}
              >
                View Applications
              </Button>
              <Button
                style={{ backgroundColor: "#266C73" }}
                onClick={() => handleDetail(item)}
              >
                More details
              </Button>
            </CardFooter>
          </Card>
        ))}


      {showApplicationModal && (
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
      )}
    </div>
  );
};

export default AdminRolePage;
