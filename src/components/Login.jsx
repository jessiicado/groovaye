import React from "react";

function Login() {
  const handleLogin = () => {
    window.location.href = "http://127.0.0.1:5000/login";
  };
  return (
    <div className="Join">
      <button className="round-button-join" onClick={handleLogin}>
        Log in
      </button>
    </div>
  );
}

export default Login;
