import React, { useState, useEffect } from "react";
import "../styles/AddJobPage.css";
import Header from "../components/Header";
import axios from "axios";

interface FormData {
  role_name: string;
  job_type: string;
  department: string;
  description: string;
  expiryDate: string;
  role_skills: Array<{ skillName: string; proficiency: number }>;
}

const accessRights = parseInt(localStorage.getItem("AccessRights") || "0", 10);

const AddJobPage: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    role_name: "",
    job_type: "",
    department: "",
    description: "",
    expiryDate: "",
    role_skills: [{ skillName: "", proficiency: 1 }],
  });

  const proficiencyLevels = {
    1: "Basic",
    2: "Intermediate",
    3: "Advanced",
  };

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
    event: React.ChangeEvent<HTMLInputElement>,
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

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/API/v1/getSkills")
      .then((response) => {
        const skills = response.data;
        setFormData((prevData) => ({
          ...prevData,
          role_skills: skills.map((skillName) => ({
            skillName,
            proficiency: 1,
          })),
        }));
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    console.log(formData);
    // You can send the form data to your server here.
  };

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
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="form-group">
            <label className="label">Expiry Date:</label>
            <input
              className="inputaddrole"
              type="date"
              name="expiryDate"
              value={formData.expiryDate}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <label className="label">Skills:</label>
            {formData.role_skills.map((skill, index) => (
              <div key={index} className="skill-card">
                <select
                  name="skillName"
                  value={skill.skillName}
                  onChange={(event) => handleSkillChange(event, index)}
                >
                  <option value={1}>Basic</option>
                  <option value={2}>Intermediate</option>
                  <option value={3}>Advanced</option>
                </select>
                <select
                  name="proficiency"
                  value={skill.proficiency}
                  onChange={(event) => handleSkillChange(event, index)}
                >
                  <option value={1}>Basic</option>
                  <option value={2}>Intermediate</option>
                  <option value={3}>Advanced</option>
                </select>
              </div>
            ))}
            <button type="button" onClick={addSkill}>
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
