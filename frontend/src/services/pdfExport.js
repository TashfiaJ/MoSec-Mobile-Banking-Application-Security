import jsPDF from 'jspdf';

export const exportToPDF = (title, result) => {
  const doc = new jsPDF();
  doc.setFontSize(16);
  doc.text(`Results for: ${title}`, 10, 10);
  doc.setFontSize(12);
  doc.text(result, 10, 20);
  doc.save(`${title.replace(/\s+/g, '_')}_results.pdf`);
};
