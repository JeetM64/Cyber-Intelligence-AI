import React from "react";
import "./UploadZone.css";

export default function UploadZone({ onUpload }) {

  const handleFile = (e) => {
    const file = e.target.files[0];
    if (file) onUpload(file);
  };

  return (
    <div className="upload-container">

      <label className="upload-btn">
        📂 Upload Network Dataset
        <input type="file" onChange={handleFile} hidden />
      </label>

    </div>
  );
}
