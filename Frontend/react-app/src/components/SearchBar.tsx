import { Form, FormControl, Button, Row, Col } from 'react-bootstrap';
import '../styles/SearchBar.css';
import { useState } from 'react';
import { BsSearch, BsX } from "react-icons/bs";

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
      <Col xs={12} md={6}>
        <Form className='searchbar' onSubmit={handleSearch}>
          <div className="search-input">
            <FormControl
              type="text"
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
          <Button
            style={{ backgroundColor: '#266C73' }}
            type="submit"
          >
            <BsSearch />
          </Button>
        </Form>
      </Col>
    </Row>
  );
}

export default SearchBar;
