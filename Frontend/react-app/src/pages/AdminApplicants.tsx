import React, { useEffect, useState} from 'react';
import { CardBody, CardHeader, CardSubtitle, CardText, Container } from 'react-bootstrap';
import axios from 'axios';
import Badge from 'react-bootstrap/Badge';
import Header from '../components/Header';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';


const AdminApplicants = () => {
    const [data, setData] = useState<{
        application_id: number;
        applicant_staff_id : number;
        applicant_existing_role: string;
        applicant_existing_dept : string;
        application_status : string;
        date_applied : string;
        applied_role_id : number;
        role : {
            role_name : string;
        };
        staff : {
            staff_fname : string;
            staff_lname : string;
        };
        staff_skill : {
            skill_name : string;
        }[];
        role_skills : {
            skill_name : string;
        }[];
        // Add other properties as needed
      }[]>([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/viewApplicants')
          .then((response) => {
            setData(response.data);
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
      }, []);

  return (
    <div>
       <Header />
       {data.map((item) => (
        <Card style={{ margin: '30px' }} key={item.application_id.toString()}>
            <CardHeader>
                <Card.Title>Application no.{item.application_id}</Card.Title>
                <CardSubtitle>Role: {item.role.role_name}</CardSubtitle>
            </CardHeader>
            <CardBody>
                <Card.Text>Name: {item.staff.staff_fname} {item.staff.staff_lname}</Card.Text>
                <CardText>Current department: {item.applicant_existing_dept}</CardText>
                <CardText>Current role: {item.applicant_existing_role}</CardText>
                <CardText>
                    Role's needed skills: {item.role_skills.map((RoleSkill)=>(
                        <Badge bg="primary">{RoleSkill.skill_name}</Badge>
                    ))}
                </CardText>
                <CardText>Applicant's skills: {item.staff_skill.map((StaffSkill)=>(
                    <Badge bg="success">{StaffSkill.skill_name}</Badge>
                ))}
                </CardText>
            </CardBody>
        
        </Card>
       ))
        
    }
    </div>
  );
};

export default AdminApplicants;
