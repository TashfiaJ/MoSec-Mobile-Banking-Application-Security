import React, { useState } from 'react';
import axios from 'axios';
import '../styles/UploadSection.css';

function UploadSection({ title, endpoint }) {
  const [result, setResult] = useState('');
  const [file, setFile] = useState(null);
  const [pdfUrl, setPdfUrl] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile && (selectedFile.name.endsWith('.apk') || selectedFile.name.endsWith('.apkm'))) {
      setFile(selectedFile);
    } else {
      alert("Please upload a valid APK or APKM file.");
    }
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`http://localhost:8000${endpoint}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob', // This ensures we handle the binary PDF response
      });

      // Create a temporary URL for the PDF blob
      const pdfBlob = response.data;
      const pdfUrl = URL.createObjectURL(pdfBlob);
      setPdfUrl(pdfUrl);
      
      setResult(`${title} processed successfully.`);
    } catch (error) {
      console.error("Error during file upload:", error);
      setResult('Error processing the file.');
    }
  };

  return (
    <div className="upload-section">
      <h3>{title}</h3>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file}>
        Upload APK File
      </button>
      {result && <p>{result}</p>}
      
      {pdfUrl && (
        <div>
          <p>PDF generated successfully!</p>
          <iframe
            src={pdfUrl}
            width="100%"
            height="600px"
            title="APK Analysis Report"
          ></iframe>
          <a href={pdfUrl} download>
            Download PDF
          </a>
        </div>
      )}
    </div>
  );
}

export default UploadSection;
