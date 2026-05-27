import React from 'react'
import B1 from './B1.jsx'
const A1 = () => {
  let name="My name is John";
  return (
    <div>
        <h1>This is A1 component</h1>
        <B1 data={name}/>
    </div>
  )
}

export default A1