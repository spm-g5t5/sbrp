import { Fragment, useState } from "react";



function ListGroup() {
  const items = ["New York", "San Francisco", "Tokyo", "London", "Paris"];

  const handleClick = (event: React.MouseEvent) => console.log(event)
  let [selectedIndex, setSelectedIndex] = useState(-1)
  

//   const getMessage = () => {
//     return items.length === 0 ? <p>No item found</p> : null
//   }

  return (
    <Fragment>
      <h1>List</h1>
      {/* {getMessage()} */items.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li 
            className = { selectedIndex === index? 'list-group-item active' : 'list-group-item'}
            key={item} 
            onClick={() =>{setSelectedIndex(index);}}
            >{item}</li>
        ))}
      </ul>
    </Fragment>
  );
}

export default ListGroup;
