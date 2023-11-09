import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import the useNavigate hook
import '../styles/UserCard.css';

// Define a prop type for the UserCard component
interface UserCardProps {
  username: string;
}

const UserCard: React.FC<UserCardProps> = ({ username }) => {
  const navigate = useNavigate(); // Get the navigate function

  const handleUserCardClick = () => {
    if (username === 'ST') {
      navigate('/StaffRoleListingPage')
    } else if (username === 'MA') {
      // Navigate to another page if needed
      navigate('/AdminRolePage');
    }

  };

  return (
    <div className="user-card" onClick={handleUserCardClick}>
      <div className="user-avatar">
        <div className="avatar-circle">
          <h1 className="username-text">{username}</h1>
        </div>
      </div>
    </div>
  );
};

export default UserCard;
