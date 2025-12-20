import React from 'react';
import '../styles/Homepage.css';

function HomePage() {
  return (
    <div className="homepage-container">
      <div className="content">
        {/* Replace the static GIF with the embedded iframe */}
        <div className="gif-container">
          <iframe
            src="https://giphy.com/embed/RDZo7znAdn2u7sAcWH"
            width="480"
            height="269"
            style={{ border: 'none', borderRadius: '8px' }}
            frameBorder="0"
            allowFullScreen
            title="Cybersecurity GIF"
          ></iframe>
        </div>
        <h1 className="homepage-title">Welcome to MoSec</h1>
        <p className="homepage-description">
          A powerful security tool designed for analyzing and safeguarding mobile banking applications.
        </p>
        <button
          className="get-started-button"
          onClick={() => window.location.href = '/methodology'}
        >
          Get Started
        </button>
      </div>
    </div>
  );
}

export default HomePage;
