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
} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { BsFillXCircleFill } from 'react-icons/bs'

const AdminRole = () => {
  const [data, setData] = useState<
    {
      role_id: number;
      role_name: string;
      department: string;
      job_description: string;
      expiry_dt: Date;
      job_type: string;
      original_creation_dt: Date;
      // Add other properties as needed
    }[]
  >([]);

  const [Applications, setApplications] = useState<{ [key: string]: any }>({});
  const [showApplicationModal, setApplicationShowModal] = useState(false);
  const [showDetailModal, setDetailShowModal] = useState(false);

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
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleViewApplications = (role_id: number) => {
    setApplicationShowModal(true);
    axios
      .get(`http://127.0.0.1:5000/API/v1/viewApplicants/role/${role_id}`)
      .then((response) => {
        setApplications(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  const handleRemoveRole = () => {
    
  }

  return (
    <div>
      <Header />
      <SearchBar />
      {data.map((item) => (
        <Card style={{ margin: "30px" }} key={item.role_id.toString()}>
          <CardHeader className="d-flex justify-content-between">
            <div>
            <h1>{item.role_name}</h1>
              {item.expiry_dt > currentDate ? (
                <Badge bg="danger">Expired</Badge>
              ) : (
                <Badge>Active</Badge>
              )}
            </div>
            <Button
              onClick={handleRemoveRole}
              variant="danger"
              style={{ display: "flex", alignItems: "center" }}
            >
              <span>Remove</span>
              <BsFillXCircleFill />
            </Button>
          </CardHeader>
          <CardBody>
            Department: {item.department}
            <RoleSkills key={item.role_name.toString()} item={item} />
          </CardBody>
          <CardFooter>
            <Button
              style={{ backgroundColor: "#266C73" }}
              onClick={() => handleViewApplications(item.role_id)}
            >
              View Applications
            </Button>
            <Button
              style={{ backgroundColor: "#266C73" }}
              onClick={() => handleDetailShowModal(item)}
            >
              More details
            </Button>
          </CardFooter>

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
                <Button
                  style={{ backgroundColor: "#266C73" }}
                  onClick={handleDetailCloseModal}
                >
                  Close
                </Button>
              </Modal.Footer>
            </Modal>
          )}

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
        </Card>
      ))}
    </div>
  );
};

export default AdminRole;
