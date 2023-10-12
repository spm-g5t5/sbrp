import React from 'react';
import { Form, FormControl, Button, Row, Col } from 'react-bootstrap';
import '../styles/SearchBar.css';

function SearchBar() {
  return (
    <Row>
      <Col xs={12} md={6}> {/* Half width on small screens, full width on medium and larger */}
        <Form className='searchbar'>
          <FormControl
            type="text"
            placeholder="Search"
            className="mr-2"
          />
          <Button style={{ backgroundColor: '#266C73' }}>Search</Button>
        </Form>
      </Col>
    </Row>
  );
}

export default SearchBar;