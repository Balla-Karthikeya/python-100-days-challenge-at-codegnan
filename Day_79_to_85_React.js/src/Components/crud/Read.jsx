// Read.jsx
import React, { useState } from "react";
import axios from "axios";
// import Create from './crud/Create'
// import home from './pages/home'
// import Read from './crud/Read'

const Read = () => {
  let [data, setData] = useState([]);
  let URL = "http://localhost:3000/student";
  const getdata = async () => {
    axios
      .get(URL)
      .then(() => {
        setData(res.data);
      })
      .catch(() => {
        alert("something went wrong");
      });
  };
  return (
    <div>
      {data.map((item)=>{
        return( 
          <div key={item.id}>
            <h2>{item.name}</h2>
            <p>{item.email}</p>
            <p>{item.pno}</p>
            <i>{item.password}</i>
            <Link to={`/Update/${+item.id}`}><button>Update</button></Link>
            <Link to={"/delete"}><button>Delete</button></Link>

          
          </div>
        )
      })}
      <button onClick={getdata}>get data</button>
    </div>
  );
};

export default Read;
