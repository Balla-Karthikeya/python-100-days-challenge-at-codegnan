// Update.jsx
import React from 'react'
import { useParams } from 'react-router-dom'

const Update = () => {
    // get all the data by id in useState
    let [getdata, setgetdata] = useState([{}]);
    let {id}=useParams();
    console.log("id",id)
    console.log(getdata)
    let URL = "http://localhost:3000/student"
    // create a function to get data by id
    let fetchdata= ()=>{
        axios.get(URL)
        .then((res)=>{
            setgetdata(res.data.id)
        })
        .catch(()=>{
            alert("something went wrong")
        })
    }
    return (
    <div>
        <button onClick={fetchdata}>Update</button>
    </div>
  )
}

export default Update


