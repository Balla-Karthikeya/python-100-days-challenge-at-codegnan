// Create.jsx
import axios from 'axios';
import React, { useState } from 'react'

const Create = () => {
    // 1. create a useState for all to store the data

    const [Name, setName] = useState("");
    const [Email, setEmail] = useState("");
    const [Pno, setPno] = useState("");
    const [Password, setPassword] = useState("");
    const [ConformPassword, setConformPassword] = useState("");

    console.log({ Name, Email, Pno, Password, ConformPassword });

    let URL = "http://localhost:3000/student"

    // 2 create a function for all the useState to set the data

    // 3. create a function to validate the data

    const validate = () => {
        if (!Name || !Email || !Pno || !Password || !ConformPassword) {
            alert("enter all the fields part 1")
            return false;
        }

        // name => min 3 char max 25 [a-zA-Z]
        if (Name.length < 3 || Name.length > 25) {
            alert("enter valid name")
            return false;

        }
        /// email => min 3 char max 25 [a-zA-Z]
        if (Email.length < 3 || Email.length > 25 || !Email.includes("@")) {
            alert("Enter valid email");
            return false;
        }



        // PNO => 10 digit [0-9]
        if (Pno.length < 10 || Pno.length > 10 || !Pno.match(/^[0-9]+$/)) {
            alert("enter valid PNO")
            return false;

        }
        // password => min 8 char max 15 [a-zA-Z0-9] also special char [%^&*#.@$]
        if (Password.length < 8 || Password.length > 15 || !Password.match(/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$/)) {
            alert("enter valid password")
            return false;

        }
        // imp password and conform password should be same
        if (Password !== ConformPassword) {
            alert("password and conform password should be same")
            return false;

        }

        return true;


    }


    // 4. create a function to post the data
    // make shore that u run you are backend server
    const postdata = (e) => {
        // what is PreventDefault 
        e.preventDefault();

        // call validate function before posting the data

        if (!validate()) {
            return;
        }
        // then call axios for posting the data
        axios.post(URL, { Name, Email, Pno, Password })
            .then(() => {
                alert("data posted successfully")
            })
            .catch(() => {
                alert("pls try again something went wrong")
            })

    }



    return (
        <div>

            <form action="" onSubmit={postdata}>
                <div>
                    <label htmlFor=""> Name</label>
                    {/* using onChange we can set the data */}
                    <input type="text" placeholder='name' onChange={(e) => { setName(e.target.value); }} />
                </div>

                <div>
                    <label htmlFor="">Email</label>
                    <input type="email" placeholder='Email' onChange={(e) => { setEmail(e.target.value); }} />
                </div>

                <div>
                    <label htmlFor="">PNO</label>
                    <input type="text" placeholder='Phone number' onChange={(e) => { setPno(e.target.value); }} />
                </div>
                <div>
                    <label htmlFor=""> password </label>
                    <input type="password" placeholder='password' onChange={(e) => { setPassword(e.target.value); }} />
                </div>
                <div>
                    <label htmlFor=""> conform password</label>
                    <input type="password" placeholder='conform password' onChange={(e) => { setConformPassword(e.target.value); }} />
                </div>

                <div>
                    <button type="submit" >Submit</button>
                </div>

            </form>

        </div>
    )
}

export default Create