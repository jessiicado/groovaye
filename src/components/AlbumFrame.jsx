import React from "react";

function AlbumFrame() {
  return (
    <div className="Album Frame">
      <img src={albumImage} alt="album-cover" className="album-cover" />
      <h3>Artist Name</h3>
      <p>Artist title</p>
    </div>
  );
}

export default AlbumFrame;
