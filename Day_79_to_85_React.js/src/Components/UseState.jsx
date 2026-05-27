// UseState.jsx
import React, { useState } from 'react'

const UseState = () => {
  let [name, SetName]=useState("John");
  let [age, SetAge]=useState("");
  let [gender, SetGender]=useState("");

    return (
    <div>
      <form action="">Name: </form>
        <h1>{name}</h1>
        <label htmlFor="SetName">Name: </label>
        <input type="text" onChange={(x)=>{SetName(x.target.value)}}/>
    
      <form action="">Age: </form>
        <h1>{age}</h1>
        <label htmlFor="SetAge">Age: </label>
        <input type="text" onChange={(x)=>{SetAge(x.target.value)}}/>
      
      <form action="">Gender: </form>
        <h1>{gender}</h1>
        <label htmlFor="Setgender">Gender: </label>
        <input type="text" onChange={(x)=>{SetGender(x.target.value)}}/>
        
    </div>
  )
}

export default UseState