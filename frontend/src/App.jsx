import React from "react";

function App() {
  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Real-time Face Detection</h1>
      <img
        src="http://127.0.0.1:8000/video_feed"
        alt="Face Detection Stream" 
        style={{ width: "640px", height: "480px", border: "2px solid black" }}
      />
    </div>
  );
}

export default App;
