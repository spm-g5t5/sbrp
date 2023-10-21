import axios, { all } from 'axios';
import React, { useEffect } from 'react';
import { useState } from 'react';
import MultiSelect from './Multiselect'

interface FilterProps {
    
}

const Filter: React.FC<FilterProps> = (props) => {
    
    const [allSKills, setAllSkills] = useState<object[]>([]); // Initialize as an empty array

      
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/API/v1/getSkills')
        .then((response) => {
            setAllSkills(response.data);
        
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
    }, []);
    
    function arrayToObjects(inputArray: string[]): { id: number; value: string }[] {
        return inputArray.map((item, index) => ({
          id: index + 1, // You can start id from 1 or 0, depending on your preference
          value: item,
        }));
      }

    const items = arrayToObjects(allSKills)

    return (
    <div className="multiselect">
        <h5>Filter by skill</h5>
        <MultiSelect items={items} placeholder="Select a Skill" />
    </div>
    );
};

export default Filter;
