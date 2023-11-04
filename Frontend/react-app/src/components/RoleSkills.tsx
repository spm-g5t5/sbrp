import React, { useEffect } from "react";
import { useState } from "react";
import { Container } from "react-bootstrap";
import axios from "axios";
import Badge from "react-bootstrap/Badge";
import Header from "../components/Header";
import { FaRegCheckCircle } from "react-icons/fa";
import { Row, Col } from "react-bootstrap";

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
    axios
      .get("http://127.0.0.1:5000/API/v1/viewRoles/skill/" + item.role_id)
      .then((response) => {
        setSkills(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const badgeStyle = {
    margin: "5px", // Adjust the margin value as needed
    padding: "10px",
    color: '#266C73'
  };

  return (
    <div>
      <Row style={{ justifyContent: 'flex-start' }}>
        {Object.keys(skills).map((key: string) => (
          <Col xl={3}>
          <div key={key} style={badgeStyle}>
          <FaRegCheckCircle /> {skills[key].skill_name}
          </div>
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default RoleSkills;
