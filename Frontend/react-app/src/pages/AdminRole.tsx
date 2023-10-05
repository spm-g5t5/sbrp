import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Header from '../components/Header';
import SearchBar from '../components/SearchBar';
import ItemContainer from '../components/ItemContainer';


const AdminRole = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/API/v1/viewRoles')
      .then((response) => {
        setData(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      
      <Header />
      <SearchBar />
      {/* Display the data */}
      <ul>
        {data.map((item) => (
          <ItemContainer key={item.role_id} item={item} />
        ))}
      </ul>
    </div>
  );
}

export default AdminRole;

