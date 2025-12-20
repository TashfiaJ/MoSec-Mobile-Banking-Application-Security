import { useState } from "react";
import { Button, Card, CardContent, Typography, CircularProgress } from "@mui/material";
import { UploadCloud, Download } from "lucide-react";
import axios from "axios";
import jsPDF from "jspdf";
import "jspdf-autotable";
import "../styles/CWEdashboard.css";

const CWE_Dashboard = () => {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    try {
      const response = await axios.post("http://localhost:8000/api/v1/check-cwe", formData);
      setResults(response.data.results);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
    setLoading(false);
  };

  const handleDownload = () => {
    if (!results) return;

    const doc = new jsPDF();
    doc.setFontSize(16);
    doc.text("CWE Analysis Report", 14, 20);

    // Prepare table data
    const tableData = Object.entries(results).map(([cwe, status]) => {
      const description = getCWE_Description(cwe);
      const [category, desc] = description.split(": ");
      const statusText = status === "yes" ? "Yes" : "No"; // Use Yes/No for the status
      return [cwe, category, desc, statusText];
    });

    // Add table
    doc.autoTable({
      startY: 30,
      head: [["CWE ID", "Category", "Description", "Status"]],
      body: tableData,
    });

    // Save the PDF
    doc.save("cwe_results.pdf");
  };

  return (
    <div className="p-8" style={{
        background: "linear-gradient(135deg, #1e293b, #3b82f6)",
        color: "#ffffff",
      }}>
      <Typography variant="h4" component="h1" gutterBottom>
        CWE Analysis Dashboard
      </Typography>
      <div className="flex gap-4 mb-6">
        <input type="file" onChange={handleFileChange} className="border p-2" />
        <Button
          variant="contained"
          color="primary"
          onClick={handleUpload}
          disabled={!file || loading}
          startIcon={<UploadCloud />}
        >
          Upload
        </Button>
      </div>
      {loading && <CircularProgress />}
      {results && (
        <Card sx={{ padding: 2, mt: 4 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Results
            </Typography>
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-100">
                  <th className="border p-2">CWE ID</th>
                  <th className="border p-2">Category</th>
                  <th className="border p-2">Description</th>
                  <th className="border p-2">Status</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(results).map(([cwe, status]) => {
                  const description = getCWE_Description(cwe);
                  const [category, desc] = description.split(": ");
                  return (
                    <tr key={cwe}>
                      <td className="border p-2 font-bold">{cwe}</td>
                      <td className="border p-2 font-semibold">{category}</td> {/* Category in bold */}
                      <td className="border p-2">{desc}</td>
                      <td
                        className={`border p-2 text-center ${
                          status === "yes" ? "text-green-500" : "text-red-500"
                        }`}
                      >
                        {status === "yes" ? "Yes" : "No"}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
            <Button
              variant="contained"
              color="secondary"
              onClick={handleDownload}
              startIcon={<Download />}
              sx={{ mt: 2 }}
            >
              Download Report
            </Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

const getCWE_Description = (cwe) => {
  const descriptions = {
    "CWE-295": {
      category: "SSL/TLS & Certificate Verification",
      description: "Improper Certificate Validation",
    },
    "CWE-330": {
      category: "Non-standard Cryptography",
      description: "Use of Insufficiently Random Values",
    },
    "CWE-322": {
      category: "Non-standard Cryptography",
      description: "Key Exchange without Entity Authentication",
    },
    "CWE-88": {
      category: "Access Control",
      description: "Argument Injection or Modification",
    },
    "CWE-302": {
      category: "Access Control",
      description: "Authentication Bypass by Assumed-Immutable Data",
    },
    "CWE-521": {
      category: "Access Control",
      description: "Weak Password Requirements",
    },
    "CWE-522": {
      category: "Access Control",
      description: "Insufficiently Protected Credentials",
    },
    "CWE-603": {
      category: "Access Control",
      description: "Use of Client-Side Authentication",
    },
    "CWE-640": {
      category: "Access Control",
      description: "Weak Password Recovery Mechanism for Forgotten Password",
    },
    "CWE-200": {
      category: "Information Leakage",
      description: "Information Exposure",
    },
    "CWE-532": {
      category: "Information Leakage",
      description: "Information Exposure Through Log Files",
    },
    "CWE-312": {
      category: "Information Leakage",
      description: "Cleartext Storage of Sensitive Information",
    },
    "CWE-319": {
      category: "Information Leakage",
      description: "Cleartext Transmission of Sensitive Information",
    },
  };

  const entry = descriptions[cwe];
  if (entry) {
    return `${entry.category}: ${entry.description}`;
  }
  return "Unknown";
};

export default CWE_Dashboard;
