import React from "react";
import { useState, useEffect } from "react";
// import { Link } from "react-router-dom";

function Home() {
  const homeList = ["artist", "song", "band", "track", "album"]; //create word array
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prevIndex) => (prevIndex + 1) % homeList.length);
    }, 1000); // Change word every second

    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

  return (
    <div className="homepage">
      <h1 className="Header">Groovyr.</h1>
      <p style={{ fontWeight: "500" }}>
        Find your new favorite <span id="HomeWord">{homeList[index]}</span> with
        a swipe.
      </p>

      <button className="getStarted">Get Started</button>
    </div>
  );
}

export default Home;
