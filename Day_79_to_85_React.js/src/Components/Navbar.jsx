// Navbar.jsx
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div>
      <Link to={"/create"}>Create</Link>
      <Link to={"/read"}>Read</Link>
      <Link to={"/update"}>Update</Link>
      <Link to={"/delete"}>Delete</Link>

    </div>
  );
};

export default Navbar;
