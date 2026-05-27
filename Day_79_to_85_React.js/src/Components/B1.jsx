// B1.jsx
import React from 'react'
import C1 from './C1'
const B1 = (prop) => {
  return (
    <div>
      <h1 style={{color:"Red"}}>This is B1 component</h1>
    <p>{prop.data}</p>
    <C1 bdata={prop.data}/>
    </div>
  )
}

export default B1