import React, { useEffect, useState } from "react";
import axios from "axios";

function Recommend() {
  const [Recommend, setRecommend] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/recommendations")
      .then((response) => {
        setRecommend(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div className="container" id="Swipe">
      {Recommend.map((item, index) => (
        <div key={index} className="album-item">
          <img
            src={item.album_cover}
            alt={item.track_name}
            className="album-image"
          />
          <div className="artist-info">
            <h2 className="artist-title">{item.artist_name}</h2>
            <p className="song-title">{item.track_name}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Recommend;
