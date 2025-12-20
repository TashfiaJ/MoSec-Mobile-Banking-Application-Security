import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import MethodologyPage from './pages/MethodologyPage';
import CWE_Dashboard from './components/CWEdashboard';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/methodology" element={<MethodologyPage />} />
        <Route path="/cwe" element={<CWE_Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
