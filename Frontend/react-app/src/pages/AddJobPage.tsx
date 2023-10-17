import React, { useState, useEffect } from "react";
import "../styles/AddJobPage.css";
import Header from "../components/Header";
import axios from "axios";
import { Navigate, Outlet, useNavigate } from "react-router-dom";

interface FormData {
  role_name: string;
  job_type: string;
  department: string;
  job_description: string;
  expiry_dt: string;
  role_skills: Array<{ skillName: string; proficiency: number }>;
  hiring_manager_id: string;
}

const accessRights = parseInt(localStorage.getItem("AccessRights") || '0', 10);
const staffId = localStorage.getItem("StaffId") || '';

const AddJobPage: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    role_name: "",
    job_type: "",
    department: "",
    job_description: "",
    expiry_dt: "",
    role_skills: [{ skillName: "", proficiency: 1 }],
    hiring_manager_id: staffId,
  });

  const proficiencyLevels = {
    1: "Basic",
    2: "Intermediate",
    3: "Advanced",
  };

  const navigate = useNavigate(); // Get the navigate function

  useEffect(() => {
    // Check access rights here
    if (accessRights !== 3) {
      // Redirect to the login page if access rights are not 3
      // This will take the user back to the login page
      navigate("/");
    }
  }, [accessRights, navigate]);

  const handleInputChange = (
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value } = event.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSkillChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>,
    index: number
  ) => {
    const { name, value } = event.target;

    setFormData((prevData) => {
      const updatedSkills = prevData.role_skills.map((skill, i) => {
        if (i === index) {
          return {
            ...skill,
            [name]: name === "proficiency" ? parseInt(value) : value,
          };
        }
        return skill;
      });

      return {
        ...prevData,
        role_skills: updatedSkills,
      };
    });
  };

  const addSkill = () => {
    setFormData((prevData) => ({
      ...prevData,
      role_skills: [...prevData.role_skills, { skillName: "", proficiency: 1 }],
    }));
  };

  const [skills, setSkills] = useState<string[]>([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/getSkills")
      .then((response) => {
        const skills = response.data;
        setSkills(skills);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    
    // Extract the current `expiry_dt` from the formData
    const existingExpiry_dt = new Date(formData.expiry_dt);
    
    // Set the hours, minutes, and seconds to 23:59:59
    existingExpiry_dt.setHours(23, 59, 59);
  
    // Format the `existingExpiry_dt` to the desired format: %a, %d %b %Y %H:%M:%S %Z
    const formattedExpiry_dt = existingExpiry_dt.toUTCString();
  
    // Create a copy of the formData and update the expiry_dt
    const updatedFormData = {
      ...formData,
      expiry_dt: formattedExpiry_dt,
    };
  
    setFormData(updatedFormData);
    
    console.log(updatedFormData);
    // You can send the form data to your server here.
  
  
    // Now, formData.expiryDate will be "2023-10-26 23:59:59"
    axios.post('http://127.0.0.1:5000/API/v1/createRole', updatedFormData)
      .then((response) => {
        // Handle the response from the server here
        console.log(updatedFormData);
        console.log(response);
      })
      .catch((error) => {
        console.error('Error logging in:', error);
      });
      navigate("/AdminRole");
  };


  // const handleSubmit = (event: React.FormEvent) => {
  //   event.preventDefault();
    
  //   console.log(formData);
  //   // You can send the form data to your server here.
  
  
  //   // Now, formData.expiryDate will be "2023-10-26 23:59:59"
  //   axios.post('http://127.0.0.1:5000/API/v1/createRole', formData)
  //     .then((response) => {
  //       // Handle the response from the server here
  //       console.log(formData);
  //       console.log(response);
  //     })
  //     .catch((error) => {
  //       console.error('Error logging in:', error);
  //     });
  // };

  return (
    <div>
      <Header accessRights={accessRights} />
      <div className="container-add-role">
        <h2 className="create-h2">Create New Job Listing</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="label">Role Name:</label>
            <input
              className="inputaddrole"
              type="text"
              name="role_name"
              value={formData.role_name}
              placeholder="Enter Role Name"
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="form-group">
            <label className="label">Department:</label>
            <input
              className="inputaddrole"
              type="text"
              name="department"
              value={formData.department}
              placeholder="Enter Job Department"
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="form-group">
            <label className="label">Job Type:</label>
            <select
              className="inputaddrole"
              name="job_type"
              value={formData.job_type}
              onChange={handleInputChange}
            >
              <option value="Full-time">Full-time</option>
              <option value="Part-time">Part-time</option>
            </select>
          </div>

          <div className="form-group">
            <label className="label">Job Description:</label>
            <textarea
              className="inputaddrole-textarea"
              name="job_description"
              value={formData.job_description}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="form-group">
            <label className="label">Expiry Date:</label>
            <input
              className="inputaddrole"
              type="date"
              name="expiry_dt"
              value={formData.expiry_dt}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <div className="skill-section">
              {formData.role_skills.map((skill, index) => (
                <div key={index} className="skill-card">
                  <div className="skill-row">
                    <label className="label-skill">Skills:</label>
                    <select
                      className="inputaddrole"
                      name="skillName"
                      value={skill.skillName}
                      onChange={(event) => handleSkillChange(event, index)}
                    >
                      <option value="">Select Skill</option>
                      {skills.map((skillItem) => (
                        <option key={skillItem} value={skillItem}>
                          {skillItem}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div className="skill-row">
                    <label className="label-skill">Proficiency:</label>
                    <select
                      className="inputaddrole"
                      name="proficiency"
                      value={skill.proficiency}
                      onChange={(event) => handleSkillChange(event, index)}
                    >
                      <option value={1}>Basic</option>
                      <option value={2}>Intermediate</option>
                      <option value={3}>Advanced</option>
                    </select>
                  </div>
                </div>
              ))}
            </div>
            <button className="submitaddskill" type="button" onClick={addSkill}>
              Add Skill
            </button>
          </div>

          <div className="submit-container">
            <button className="submitaddrole" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddJobPage;
