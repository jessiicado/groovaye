import React from "react";
import vinyl from "./vinyl.png";
import { Link } from "react-router-dom";

function NavBar() {
  const handleLogin = () => {
    window.location.href = "http://localhost:5000/login";
  };

  return (
    <div className="NavBar">
      {/* Clickable Logo */}
      <div className="cursor-pointer" onClick={() => window.location.reload()}>
        <img
          src={vinyl}
          alt="Logo"
          className="vinyl-img"
          style={{
            width: "140px",
            height: "120px",
            position: "absolute",
            top: "0px",
            right: "0px",
          }}
        />
      </div>

      {/* Header */}

      <div className="Nav">
        <Link to="/" className="Home">
          Home
        </Link>

        <Link to="/swipe" className="Swipe">
          Swipe
        </Link>
      </div>
      <div className="Join">
        <button onClick={handleLogin} className="round-button-join">
          Log in
        </button>
      </div>
    </div>
  );
}

export default NavBar;
