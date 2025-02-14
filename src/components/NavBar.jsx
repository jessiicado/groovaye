import React from "react";
import vinyl from "./vinyl.png";

function NavBar() {
  return (
    <div className="NavBar">
      {/* Clickable Logo */}
      <div className="cursor-pointer" onClick={() => window.location.reload()}>
        <img src={vinyl} alt="Logo" className="w-12 h-auto" />
      </div>

      {/* Header */}
      <div className="Name">Vinylage</div>
    </div>
  );
}

export default NavBar;
