import React, { useState } from "react";

function App() {
  const [detections, setDetections] = useState([]);

  const fetchDetections = async () => {
    const response = await fetch("http://127.0.0.1:8000/detect");
    const data = await response.json();
    setDetections(data.detections);
  };

  return (
    <div className="App">
      <h1>Real-Time Object Detection</h1>
      <button onClick={fetchDetections}>Detect Objects</button>
      {detections.length > 0 && (
        <ul>
          {detections.map((det, index) => (
            <li key={index}>
              Bounding Box: ({det.x1}, {det.y1}) - ({det.x2}, {det.y2})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
