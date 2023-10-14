import React from 'react';
import '../styles/UserCard.css';

// Define a prop type for the UserCard component
interface UserCardProps {
  username: string;
}

const UserCard: React.FC<UserCardProps> = ({ username }) => {
    return (
      <div className="user-card">
        <div className="user-avatar">
          <div className="avatar-circle">
            <h1 className="username-text">{username}</h1>
          </div>
        </div>
      </div>
    );
  };
  

export default UserCard;
