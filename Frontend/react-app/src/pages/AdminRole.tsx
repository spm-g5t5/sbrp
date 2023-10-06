import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Header from '../components/Header';
import SearchBar from '../components/SearchBar';
import ItemContainer from '../components/ItemContainer';
import RoleSkills from '../components/RoleSkills';
import { Button, Container, Modal } from 'react-bootstrap';
import Card from 'react-bootstrap/Card';


const AdminRole = () => {
  const [data, setData] = useState([]);
  const [Applications, setApplications] = useState([]);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/API/v1/viewRoles')
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleViewApplications = (role_id) => {
    setShowModal(true);
    axios.get('http://127.0.0.1:5000/API/v1/viewApplicants/role/'+ role_id)
    .then((response) => {
      setApplications(response.data);
      console.log(response.data);
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
  }
  return (
    <div>
      
      <Header />
      <SearchBar />
      {/* Display the data */}
      <ul>
        {data.map((item) => (
          <Card style={{ margin: '30px' }}>
          <ItemContainer key={item.role_id} item={item} />
          <RoleSkills key={item.role_name} item={item} />
          <Button style={{ backgroundColor: '#266C73' }} onClick={() => handleViewApplications(item.role_id)}>View Applications</Button>
          {showModal && (
            <Modal show={showModal} onHide={() => setShowModal(false)}>
              <Modal.Header closeButton>
                <Modal.Title>Applications</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                <p>Applicant by staff ID</p>
                {Object.keys(Applications).map((key) => (
                  <li key={key}>{Applications[key].applicant_staff_id}</li>
                ))}
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={() => setShowModal(false)}>
                  Close
                </Button>
              </Modal.Footer>
          </Modal>
          )}
          </Card>
        ))}
      </ul>
    </div>
  );
}

export default AdminRole;