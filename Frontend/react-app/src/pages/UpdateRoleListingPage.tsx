import React, { useState, useEffect } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import axios from "axios";
import Header from "../components/Header";

const UpdateRoleListingPage = () => {
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10
  );
  const roleId = parseInt(localStorage.getItem("RoleId") || "0", 10);
  const staffId = localStorage.getItem("StaffId") || "";

  const navigate = useNavigate();

  interface FormData {
    role_name: string;
    job_type: string;
    department: string;
    job_description: string;
    expiry_dt: string;
    role_listing_skills: (string | number)[][];
    hiring_manager_id: any;
    orig_role_listing: {};
    active_status: number;
  }

  const [formData, setFormData] = useState<FormData>({
    role_name: "",
    job_type: "",
    department: "",
    job_description: "",
    expiry_dt: "",
    role_listing_skills: [["", 1]],
    hiring_manager_id: "",
    orig_role_listing: {},
    active_status: 1,
  });

  const [expiry_date, setExpiryDate] = useState("");

  const [expiry_time, setExpiryTime] = useState("");

  useEffect(() => {
    if (accessRights !== 3) {
      navigate("/");
    }
  }, [accessRights, navigate]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000//API/v1/searchAllRoleVer/${roleId}`)
      .then((response) => {
        const data = response.data;
        if (Array.isArray(data) && data.length > 0) {
          // Get the last object in the array
          const lastObject = data[data.length - 1];
          const roleData = lastObject.role;
          const roleSkill = lastObject.role_listing_skills;
          const formattedSkills = roleSkill.map((skill: any) => [
            skill.skill_name,
            skill.skills_proficiency,
          ]);

          // Parse the original expiry date string
          const originalExpiryDate = new Date(roleData.expiry_dt);

          // Format date as "yyyy-MM-dd"
          const year = originalExpiryDate.getFullYear();
          const month = String(originalExpiryDate.getMonth() + 1).padStart(
            2,
            "0"
          );
          const day = String(originalExpiryDate.getDate()).padStart(2, "0");
          const formattedDate = `${year}-${month}-${day}`;

          // Format time as "HH:mm:ss"
          const gmtExpiryDate = new Date(
            Date.UTC(
              originalExpiryDate.getUTCFullYear(),
              originalExpiryDate.getUTCMonth(),
              originalExpiryDate.getUTCDate(),
              originalExpiryDate.getUTCHours(),
              originalExpiryDate.getUTCMinutes()
            )
          );
          const formattedTime = gmtExpiryDate.toISOString().slice(11, 19); // Extract the time part
          setFormData({
            role_name: roleData.role_name,
            department: roleData.department,
            job_type: roleData.job_type,
            job_description: roleData.job_description,
            expiry_dt: roleData.expiry_dt,
            role_listing_skills: formattedSkills,
            hiring_manager_id: staffId,
            orig_role_listing: roleData,
            active_status: 1,
          });

          setExpiryDate(formattedDate);
          setExpiryTime(formattedTime);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [roleId]);

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

  const handleInputChangeDate = (
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value } = event.target;

    setExpiryDate(value); // Update the expiry_date state with the input date
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
            // Update skillName at role_listing_skills[index][0]
            return [value, skill[1]];
          } else if (name === "proficiency") {
            // Update proficiency at role_listing_skills[index][1]
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

  const addSkill = () => {
    setFormData((prevData) => ({
      ...prevData,
      role_listing_skills: [...prevData.role_listing_skills, ["", 1]],
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

    // Combine date and time and format it
    const combinedDateTime = `${expiry_date} ${expiry_time}`;
    const combinedDateTimeAsDate = new Date(combinedDateTime);
    combinedDateTimeAsDate.setSeconds(59); // Set seconds to 59
    combinedDateTimeAsDate.setUTCHours(combinedDateTimeAsDate.getUTCHours()+8);
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
      .post("http://127.0.0.1:5000/API/v1/updateRole", updatedFormData)
      .then((response) => {
        // Handle the response from the server here
        console.log(updatedFormData);
        console.log(response);
      })
      .catch((error) => {
        console.error("Error logging in:", error);
      });
    navigate("/AdminRolePage");
  };

  return (
    <div>
      <Header accessRights={accessRights} />
      <div className="container-add-role">
        <h2 className="create-h2">Update Job Listing</h2>
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
              required
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
              required
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
              required
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
                      value={skill[1]}
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
              Update
            </button>
            <button
              className="submitaddrole"
              type="submit"
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

export default UpdateRoleListingPage;
