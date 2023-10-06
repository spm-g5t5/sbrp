import React from 'react';
import { useState } from 'react';
import { Container } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Modal from 'react-bootstrap/Modal';


interface Item {
  role_name: string;
  department: string;
  job_description: string
  expiry_dt: string;
  job_type: string;
}

interface MyComponentProps {
  item: Item;
}

const ItemContainer: React.FC<MyComponentProps> = ({ item }) => {
  const [showModal, setShowModal] = useState(false);
  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);
  const currentDate = new Date(item.expiry_dt)
  const dateStr = currentDate.toLocaleDateString()

  return (
    <Container>
    <Card style={{ width: '18rem' }}>
    <Card.Body>
      <Card.Title>{item.role_name}</Card.Title>
      <Card.Text>
        Department: {item.department}
      </Card.Text>
      <Button style={{ backgroundColor: '#266C73' }} onClick={handleShowModal}>More details</Button>
    </Card.Body>
  </Card>
  <Modal show={showModal} onHide={handleCloseModal}>
  <Modal.Header closeButton>
    <Modal.Title>{item.role_name}</Modal.Title>
  </Modal.Header>
  <Modal.Body>
    Application Close Date: <p>{dateStr}</p>
    Job Description:<p>{item.job_description}</p>
    Job Type: <p>{item.job_type}</p>
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