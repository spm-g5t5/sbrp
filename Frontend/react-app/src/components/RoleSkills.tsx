import React, { useEffect } from 'react';
import { useState } from 'react';
import { Container } from 'react-bootstrap';
import axios from 'axios';
import Badge from 'react-bootstrap/Badge';

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

const RoleSkills: React.FC<MyComponentProps> = ({ item }) => {
    const [skills, setSkills] = useState([]);
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/viewRoles/skill/'+ item.role_name)
      .then((response) => {
        setSkills(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
    },[]);

  return (
    <Container>
        <p>Skills required:</p>
        {Object.keys(skills).map((key) => (
           <Badge bg="success" key={key}>{skills[key].skill_name} </Badge>
        ))}
        
    </Container>
  )
};

export default RoleSkills;