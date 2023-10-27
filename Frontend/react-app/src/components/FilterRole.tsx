import axios, { all } from 'axios';
import React, { useEffect } from 'react';
import { useState } from 'react';
import MultiSelect from './Multiselect'
import { Modal } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';

interface FilterProps {
    sendDataToRoleListing: (data: any) => void; // Define the function signature
  }

const FilterRole: React.FC<FilterProps> = ({ sendDataToRoleListing }) => {
    
  const [allSKills, setAllSkills] = useState<string[]>([]);
  const [allJobType, setAllJobType] = useState<string[]>([]);
  const [allDepartment, setAllDepartment] = useState<string[]>([]);

      
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/getJobType')
        .then((response) => {
            setAllJobType(response.data);
        
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
    }, []);
    
    useEffect(() => {
            axios.get('http://127.0.0.1:5000/API/v1/getDepartment')
            .then((response) => {
                setAllDepartment(response.data);
            
              }).catch((error) => {
                console.error('Error fetching data:', error);
              });
        }, []);

    useEffect(() => {
            axios.get('http://127.0.0.1:5000/API/v1/getSkills')
            .then((response) => {
                setAllSkills(response.data);
            
              }).catch((error) => {
                console.error('Error fetching data:', error);
              });
        }, []);
              
    function arrayToObjects(inputArray: string[]): { id: string; value: string }[] {
      return inputArray.map((item, index) => ({
          id: (index + 1).toString(),
          value: item,
      }));
  }
  

    const SkillItems = arrayToObjects(allSKills)
    const DepartmentItem = arrayToObjects(allDepartment)
    const JobTypeItem = arrayToObjects(allJobType)


    // const handleDataFromMulti = (data: any) => {
    //     sendDataToApplicant(data);
    // }

    const allFilters: { [key: string]: any } = {};


    const handleSkillDataFromMulti = (data: any) => {
        const skillArray = data.map((obj:{ id: number; value: string }) => obj.value);
        allFilters["skills"] = skillArray
        sendDataToRoleListing(allFilters);
    }
    const handleDepartmentDataFromMulti = (data: any) => {
        const departmentArray = data.map((obj:{ id: number; value: string }) => obj.value);
        allFilters["department"] = departmentArray
        sendDataToRoleListing(allFilters);
    }
    const handleJobTypeDataFromMulti = (data: any) => {
        const jobTypeArray = data.map((obj:{ id: number; value: string }) => obj.value);
        allFilters["jobtype"] = jobTypeArray
        sendDataToRoleListing(allFilters);
    }

    return (
    <div>
            <MultiSelect sendDataToFilter={handleSkillDataFromMulti} items={SkillItems} zIndex={3} placeholder="Select a Skill" />
            <MultiSelect sendDataToFilter={handleDepartmentDataFromMulti} items={DepartmentItem} zIndex={2} placeholder="Select a department" />
            <MultiSelect sendDataToFilter={handleJobTypeDataFromMulti} items={JobTypeItem} zIndex={1} placeholder="Select a job type" />
       
    </div>
    );
};

export default FilterRole;
