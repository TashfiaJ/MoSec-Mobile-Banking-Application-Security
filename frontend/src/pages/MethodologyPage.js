import React from 'react';
import UploadSection from '../components/UploadSection';

function MethodologyPage() {
  // Define both title and corresponding API endpoint for each methodology point
  const methodologyPoints = [
    { title: 'APK File Extraction', endpoint: '/apk/upload-apk/' },
    { title: 'Custom Static Analysis', endpoint: '/analysis/upload-apk/' },
    { title: 'SSL/TLS Server Testing', endpoint: '/ssl-tls/ssl-test-apk' },
    { title: 'Manual Analysis Automation', endpoint: '/api/v1/upload-apk-analysis/' },
    { title: 'Reverse Engineering', endpoint: '/api/v1/upload-apk-reverse-engineering/' },
    { title: 'Sensitive Data Leakage Detection', endpoint: '/api/v1/sensitive-data-leakage/' },
  ];
  return (
    <div className="methodology-container">
      <div className="content">
        <h1 className="methodology-title">Vulnerability Analysis</h1>
        <p className="methodology-description">
          Discover the crucial steps in safeguarding mobile banking applications through comprehensive vulnerability analysis.
        </p>
        {methodologyPoints.map((point, index) => (
          <UploadSection key={index} title={point.title} endpoint={point.endpoint} />
        ))}
      </div>
    </div>
  );
}

export default MethodologyPage;
