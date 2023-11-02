import React from 'react';
import Header from '../components/Header';

const StaffApplicationPage = () => {
  const accessRights = parseInt(
    localStorage.getItem("AccessRights") || "0",
    10)

  return (
    <div>
      <Header accessRights={accessRights} />
      
    </div>
  );
}

export default StaffApplicationPage;