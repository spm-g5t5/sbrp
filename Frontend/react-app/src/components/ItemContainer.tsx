import React from 'react';
import { useState } from 'react';
import { Container } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Badge from 'react-bootstrap/Badge';

interface Item {
  role_name: string;
  department: string;
  job_description: string
  expiry_dt: string;
  job_type: string;
  original_creation_dt: string;
}

interface MyComponentProps {
  item: Item;
}

const ItemContainer: React.FC<MyComponentProps> = ({ item }) => {
  const [showModal, setShowModal] = useState(false);
  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);



  const expiryDate = new Date(item.expiry_dt)
  const expDateStr = expiryDate.toLocaleDateString()
  const currentDate = new Date()

  const [expired, setExpired] = useState(false);
  if (expiryDate < currentDate && !expired) {
      setExpired(true);
  }

  return (
    <Container>
      <h1>{item.role_name}</h1>
      {expired && <Badge>Expired</Badge>}
      <div>
        Department: {item.department}
      </div>
      <Button style={{ backgroundColor: '#266C73' }} onClick={handleShowModal}>More details</Button>

  <Modal show={showModal} onHide={handleCloseModal}>
  <Modal.Header closeButton>
    <Modal.Title>{item.role_name}</Modal.Title>
  </Modal.Header>
  <Modal.Body>
    Application Close Date: <p>{expDateStr}</p>
    Job Description:<p>{item.job_description}</p>
    Job Type: <p>{item.job_type}</p>
    Creation Date and time: <p>{item.original_creation_dt}</p>
  </Modal.Body>
  <Modal.Footer>
    <Button style={{ backgroundColor: '#266C73' }} onClick={handleCloseModal}>
      Close
    </Button>
  </Modal.Footer>
</Modal>
</Container>
  )
};

export default ItemContainer;