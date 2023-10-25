import React, { useEffect } from 'react';
import { useState } from 'react';
import { Container } from 'react-bootstrap';
import axios from 'axios';
import Badge from 'react-bootstrap/Badge';
import Header from '../components/Header';

interface Item {
  role_id: number;
  role_name: string;
  department: string;
  job_description: string;
  expiry_dt: Date;
  job_type: string;
}

interface MyComponentProps {
  item: Item;
}

const RoleSkills: React.FC<MyComponentProps> = ({ item }) => {
  const [skills, setSkills] = useState<{ [key: string]: any }>({});

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/API/v1/viewRoles/skill/' + item.role_id)
      .then((response) => {
        setSkills(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      {Object.keys(skills).map((key: string) => (
        <Badge bg="success" key={key}>
          {skills[key].skill_name}
        </Badge>
      ))}
    </div>
  );
};

export default RoleSkills;
