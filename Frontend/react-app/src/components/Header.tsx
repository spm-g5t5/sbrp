import React from 'react';
import logo from '../assets/logo.png';
import '../styles/Header.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Navigate, Outlet, useNavigate } from "react-router-dom";

interface HeaderProps {
  accessRights: number;
}


const Header: React.FC<HeaderProps> = ({ accessRights }) => {
  const navigate = useNavigate();
  return (
    <Navbar expand="lg" className="bgcolor">
      <Container>
        <Navbar.Brand href="#home">
          <img
            src={logo}
            width="40"
            height="60"
            className="d-inline-block align-top"
            alt="Logo"
          />
        </Navbar.Brand>
        <Navbar.Brand className='text-white'>Admin Application Portal</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          {accessRights === 1 ? (
            // Render the original content when accessRights is 1
            <div></div> // You can add your additional content here
          ) : (
            // Render different content when accessRights is not 1
            <Nav className="justify-content-end">
              <Nav.Link onClick={() => navigate("/AdminRole")} className="text-white">Role Listing</Nav.Link>
              <Nav.Link onClick={() => navigate("/AdminApplicantsPage")} className="text-white">Applicants</Nav.Link>
            </Nav>
          )}
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
