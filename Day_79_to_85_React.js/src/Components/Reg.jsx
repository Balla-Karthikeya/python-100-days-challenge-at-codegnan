import React, { useState } from 'react'

import "./reg.css"
import axios from 'axios'

const Reg = () => {
  let [name,setName]=useState("")
  let [email,setEmail]=useState("")
  let [age,setAge]=useState("")
  let [dob,setDob]=useState("")
  let [gender,setGender]=useState("")
  let [password,setPassword]=useState("")
  let [confirmPassword,setConfirmPassword]=useState("")


  let URL="http://localhost:3000/student"


  // let student ={name,email,age,dob,gender,password,confirmPassword}

  let postdata=() =>{
    axios.post(URL,{name,email,age,dob,gender,password,confirmPassword})
  } 

  // Validation 
  
  
  return (
    <div>
      <form >
        <div>
          <label>Name: </label>
          <input type="text" onChange={(e)=>setName(e.target.value)} required minLength={3} maxLength={25}/>
        </div>

        <div>
          <label>Email: </label>
          <input type="email" onChange={(e)=>setEmail(e.target.value)}required/>
        </div>

        <div>
          <label>Age: </label>
          <input type="number" onChange={(e)=>setAge(e.target.value)}required/>
        </div>

        <div>
          <label>Date of Birth: </label>
          <input type="date" onChange={(e)=>setDob(e.target.value)}required/>
        </div>

        <div>
          <label>Gender: </label>

          <input type="radio" name="gender" id="male" onChange={(e)=>setGender(e.target.value)} />
          <label htmlFor="male">Male</label>

          <input type="radio" name="gender" id="female" onChange={(e)=>setGender(e.target.value)} />
          <label htmlFor="female">Female</label>
        </div>

        <div>
          <label>Password: </label>
          <input type="password" onChange={(e)=>setPassword(e.target.value)}required/>
        </div>

        <div>
          <label>Confirm Password: </label>
          <input type="password" onChange={(e)=>setConfirmPassword(e.target.value)}required/>
        </div>

        <div>
          <button type="submit" onClick={postdata}>Submit</button>
        </div>

      </form>
    </div>
  )
}

export default Reg