import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <h1 className="navbar-title">MoSec</h1>
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/methodology">Vulnerability Analysis</Link>
        <Link to="/cwe">CWE Analysis</Link>
      </div>
    </nav>
  );
}

export default Navbar;
