import React from 'react';
import { Form, FormControl, Button, Row, Col } from 'react-bootstrap';
import '../styles/SearchBar.css';

function SearchBar() {
  return (
    <Row className='searchbar'>
      <Col xs={12} md={6}> {/* Half width on small screens, full width on medium and larger */}
        <Form className="form-inline">
          <FormControl
            type="text"
            placeholder="Search"
            className="mr-2"
          />
          <Button variant="outline-success">Search</Button>
        </Form>
      </Col>
    </Row>
  );
}

export default SearchBar;