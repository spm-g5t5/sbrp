import React from 'react';
import { useState } from 'react';
import logo from '../assets/logo.png';
import '../styles/Header.css'


import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

function Header() {

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

        </Navbar.Collapse>
      </Container>
    </Navbar>
    );
}

export default Header;
