import React, { useState, useEffect } from "react";
import "../styles/AddJobPage.css";
import Header from "../components/Header";
import axios from "axios";
import { Navigate, Outlet, useNavigate } from "react-router-dom";
import { BsX } from "react-icons/bs";

interface FormData {
  role_name: string;
  job_type: string;
  department: string;
  job_description: string;
  expiry_dt: string;
  role_listing_skills: Array<[string, number]>;
  hiring_manager_id: string;
}

const accessRights = parseInt(localStorage.getItem("AccessRights") || "0", 10);
const staffId = localStorage.getItem("StaffId") || "";

const AddJobPage: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    role_name: "",
    job_type: "",
    department: "",
    job_description: "",
    expiry_dt: "",
    role_listing_skills: [["", 1]],
    hiring_manager_id: staffId,
  });

  const [errorDate, setErrorDate] = useState("");
  const [error, setError] = useState("");

  const [expiry_date, setExpiryDate] = useState("");

  const [expiry_time, setExpiryTime] = useState("");

  const proficiencyLevels = {
    1: "Basic",
    2: "Intermediate",
    3: "Advanced",
  };

  const navigate = useNavigate(); // Get the navigate function
  //Check and navigate to the right page
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
    setError("");
  };

  const handleInputChangeDate = (
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value } = event.target;
    const isDateInPast = (inputDate: Date): boolean => {
      const currentDate = new Date();
      return inputDate <= currentDate;
    };

    const inputDate = new Date(value);
    if (isDateInPast(inputDate)) {
      setErrorDate("Please choose a present date for your expiry date.");
      setExpiryDate(value);
    } else {
      setExpiryDate(value);
      setErrorDate("");
    }
  };

  const handleInputChangeTime = (
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value } = event.target;

    setExpiryTime(value); // Update the expiry_time state with the input time
  };

  const handleSkillChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>,
    index: number
  ) => {
    const { name, value } = event.target;

    setFormData((prevData) => {
      const updatedSkills = prevData.role_listing_skills.map((skill, i) => {
        if (i === index) {
          if (name === "skillName") {
            // Check if the selected skill is not already in the selectedSkills array
            if (!selectedSkills.includes(value)) {
              setSelectedSkills([...selectedSkills, value]);
            }
            return [value, skill[1]];
          } else if (name === "proficiency") {
            return [skill[0], parseInt(value, 10)];
          }
        }
        return skill;
      });

      return {
        ...prevData,
        role_listing_skills: updatedSkills,
      };
    });
  };

  const handleRemoveSkill = (index: number) => {
    setFormData((prevData) => {
      const updatedSkills = prevData.role_listing_skills.filter(
        (_, i) => i !== index
      );

      return {
        ...prevData,
        role_listing_skills: updatedSkills,
      };
    });

    setSelectedSkills((prevSelectedSkills) => {
      const skillToRemove = prevSelectedSkills[index];
      const updatedSelectedSkills = prevSelectedSkills.filter(
        (_, i) => i !== index
      );

      return updatedSelectedSkills;
    });
  };

  const addSkill = () => {
    setFormData((prevData) => ({
      ...prevData,
      role_listing_skills: [...prevData.role_listing_skills, ["", 1]],
    }));
  };

  const [skills, setSkills] = useState<string[]>([]);
  const [selectedSkills, setSelectedSkills] = useState<string[]>([]);

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

    const errors = [];
    if (formData.role_name === "" || formData.role_name.trim().length === 0) {
      errors.push("Role Name");
    }

    if (formData.department === "" || formData.department.trim().length === 0) {
      errors.push("Job Department");
    }

    if (formData.job_type === "") {
      errors.push("Job Type");
    }

    if (
      formData.job_description === "" ||
      formData.job_description.trim().length === 0
    ) {
      errors.push("Job Description");
    }

    if (expiry_date === "") {
      errors.push("Job Expiry Date");
    }

    if (expiry_time === "") {
      errors.push("Job Expiry Time");
    }

    // Check for empty skills
    const hasEmptySkills = formData.role_listing_skills.some(
      (skill) => skill[0] === "" || skill[0] === "Select Skill"
    );
    if (hasEmptySkills) {
      errors.push("Skills");
    }
    if (errors.length > 0) {
      const errorMessage = `Please fill in the following fields: ${errors.join(
        ", "
      )}.`;
      setError(errorMessage);
    } else if (errorDate.length > 0) {
      setError("");
    } else {
      setError("");
      // Combine date and time and format it
      const combinedDateTime = `${expiry_date} ${expiry_time}`;
      const combinedDateTimeAsDate = new Date(combinedDateTime);
      combinedDateTimeAsDate.setSeconds(59); // Set seconds to 59
      combinedDateTimeAsDate.setUTCHours(
        combinedDateTimeAsDate.getUTCHours() + 8
      );
      const formattedExpiry_dt = combinedDateTimeAsDate.toUTCString();

      const updatedFormData = {
        ...formData,
        expiry_dt: formattedExpiry_dt,
      };

      setFormData((prevData) => ({
        ...prevData,
        expiry_dt: formattedExpiry_dt,
      }));

      console.log(updatedFormData);
      axios
        .post("http://127.0.0.1:5000/API/v1/createRole", updatedFormData)
        .then((response) => {
          // Handle the response from the server here
          console.log(response);
        })
        .catch((error) => {
          console.error("Error logging in:", error);
        });
      navigate("/AdminRolePage");
    }
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
              <option value="" disabled>
                Select Job Type
              </option>
              <option value="FT">FT</option>
              <option value="PT">PT</option>
            </select>
          </div>

          <div className="form-group">
            <label className="label">Job Description:</label>
            <textarea
              className="inputaddrole-textarea"
              name="job_description"
              value={formData.job_description}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <label className="label">Expiry Date:</label>
            <input
              className="inputaddrole"
              type="date"
              name="expiry_date"
              value={expiry_date}
              onChange={handleInputChangeDate}
            />
          </div>

          <div className="form-group">
            <label className="label">Expiry Time:</label>
            <input
              className="inputaddrole"
              type="time"
              name="expiry_time"
              value={expiry_time}
              onChange={handleInputChangeTime}
            />
          </div>

          <div className="form-group">
            <div className="skill-section">
              {formData.role_listing_skills.map((skill, index) => (
                <div key={index} className="skill-card">
                  <div className="skill-row">
                    <label className="label-skill">Skills:</label>
                    <select
                      className="inputaddrole"
                      name="skillName"
                      value={skill[0]}
                      onChange={(event) => handleSkillChange(event, index)}
                    >
                      <option value="" disabled>
                        Select Skill
                      </option>
                      {skills.map((skillItem) => (
                        <option
                          key={skillItem}
                          value={skillItem}
                          disabled={selectedSkills.includes(skillItem)}
                        >
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
                      value={skill[1]}
                      onChange={(event) => handleSkillChange(event, index)}
                    >
                      <option value={1}>Basic</option>
                      <option value={2}>Intermediate</option>
                      <option value={3}>Advanced</option>
                    </select>
                  </div>
                  <button
                    className="remove-skill-button"
                    onClick={() => handleRemoveSkill(index)}
                    type="button"
                  >
                    <BsX /> 
                  </button>
                </div>
              ))}
            </div>
            <button className="submitaddskill" type="button" onClick={addSkill}>
              Add Skill
            </button>
          </div>
          {(error || errorDate) && (
            <div className="alert-input" role="alert">
              <span dangerouslySetInnerHTML={{ __html: errorDate }} />
              <br />
              {error}
            </div>
          )}

          <div className="submit-container">
            <button className="submitaddrole" type="submit">
              Submit
            </button>
            <button
              className="submitaddrole"
              type="button"
              onClick={() => navigate("/AdminRolePage")}
              style={{ backgroundColor: "#F32013", color: "white" }}
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddJobPage;
