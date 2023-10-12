import React from 'react';
import { useState } from 'react';
import { Container } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Badge from 'react-bootstrap/Badge';
import { BsFillXCircleFill } from 'react-icons/bs'

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

  const expiryDate = new Date(item.expiry_dt)
  const expDateStr = expiryDate.toLocaleDateString()
  const currentDate = new Date()

  const [expired, setExpired] = useState(false);
  if (expiryDate < currentDate && !expired) {
      setExpired(true);
  }

  const handleRemoveRole = () => {

  }

  return (
    <Container>
      <h1>{item.role_name}</h1>
      {expired && <Badge>Expired</Badge>}
      <div>
        Department: {item.department}
      </div>
      <Button onClick={handleRemoveRole} variant="danger" style={{ display: 'flex', alignItems: 'center' }}>
        <span>Remove</span>
        <BsFillXCircleFill style={{ marginRight: 'auto' }} />
      </Button>


  
</Container>
  )
};

export default ItemContainer;