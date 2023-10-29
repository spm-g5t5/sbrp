import { Form, FormControl, Button, Row, Col } from 'react-bootstrap';
import '../styles/SearchBar.css';
import { useState } from 'react';
import { BsSearch, BsX } from "react-icons/bs";
import React from 'react';

interface SearchBarProps {
  onSearch: (searchText: string) => void;
}

function SearchBar({ onSearch }: SearchBarProps) {
  const [searchText, setSearchText] = useState('');

  const handleSearch = (e: any) => {
    e.preventDefault();
    onSearch(searchText);
  }

  const handleClear = (e:any) => {
    e.preventDefault();
    onSearch("");
    setSearchText("");
  }

  return (
    <Row>
      <Col>
      <Form className='searchbar' onSubmit={handleSearch}>
          <div className="search-input">
            <input
              type="text"
              className="search-input-text"
              placeholder="Search roles..."
              value={searchText}
              onChange={(e) => setSearchText(e.target.value)}
            />
            {searchText && (
              <span className="clear-icon" onClick={handleClear}>
                <BsX />
              </span>
            )}
          </div>
          <button
            className='submit-search-button'
            type="submit"
          >
            <BsSearch />
          </button>
          </Form>
      </Col>
    </Row>
        
  );
}

export default SearchBar;
