import axios, { all } from 'axios';
import React, { useEffect } from 'react';
import { useState } from 'react';
import MultiSelect from './Multiselect'

interface FilterProps {
    sendDataToApplicant: (data: any) => void; // Define the function signature
  }

const FilterApplicants: React.FC<FilterProps> = ({ sendDataToApplicant }) => {
    
  const [allSKills, setAllSkills] = useState<string[]>([]); // Initialize as an empty array

      
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/getSkills')
        .then((response) => {
            setAllSkills(response.data);
        
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
    }, []);
    
    function arrayToObjects(inputArray: string[]): { id: string; value: string }[] {
      return inputArray.map((item, index) => ({
          id: (index + 1).toString(),
          value: item,
      }));
  }
  

    const items = arrayToObjects(allSKills)


    const handleDataFromMulti = (data: any) => {
        sendDataToApplicant(data);
    }

    return (
    <div className="multiselect">
        <MultiSelect sendDataToFilter={handleDataFromMulti} items={items} placeholder="Select a Skill" />
    </div>
    );
};

export default FilterApplicants;
