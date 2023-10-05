import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.png';
import logoWave from '../assets/logo_wave_design.png';
import '../App.css'; // Import a CSS file for component-specific styles
import axios from 'axios';

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
        {/* Display the data */}
        <ul>
          {data.map((data) => (
            <table>
            <tbody>
              <tr>
                <td>Department:</td>
                <td>{data.department}</td>
              </tr>
              <tr>
                <td>Expiry Date:</td>
                <td>{data.expiry_dt}</td>
              </tr>
              <tr>
                <td>Hiring Manager ID:</td>
                <td>{data.hiring_manager_id}</td>
              </tr>
              <tr>
                <td>Job Description:</td>
                <td>{data.job_description}</td>
              </tr>
              <tr>
                <td>Job Type:</td>
                <td>{data.job_type}</td>
              </tr>
              <tr>
                <td>Original Creation Date:</td>
                <td>{data.original_creation_dt}</td>
              </tr>
              <tr>
                <td>Role ID:</td>
                <td>{data.role_id}</td>
              </tr>
              <tr>
                <td>Role Name:</td>
                <td>{data.role_name}</td>
              </tr>
            </tbody>
          </table>
          ))}
        </ul>
      </div>
    );
  }


export default AdminRole;
