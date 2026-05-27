// App.jsx
// import React from 'react'
// import A from './Components/A'
// import A1 from './Components/A1'
// import B from './Components/B'
// import C from './Components/C'
// import D from './Components/D'
// import E from './Components/E'
// import F from './Components/F'
// import G from './Components/G'
// import Reg from "./Components/Reg"
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Create from "./Components/crud/Create";
import Read from "./Components/crud/Read";
import Navbar from "./Components/Navbar";

const App = () => {
  return (
    <div>
      {/* <A />
      <B />
      <C />
      <D />
      <E />
      <F />
      <G /> */}
      {/* <h1>HelloReact</h1> */}
      {/* <A1/> */}
      {/* <UseState/> */}
      {/* <Reg /> */}
      {/* <Navbar/>
      <Create/>
      <Read/>
      <home/> */}
      <BrowserRouter> 
      <Navbar>
        <Routes>
          <Route path="/create" element={<CreateCard />} />
          <Route path="/read" element={<ReadCard />} />
          <Route path="/update/:id" element={<EditCard/>} />
        </Routes>
      </Navbar>
      </BrowserRouter>
    </div>
  );
};

export default App;
