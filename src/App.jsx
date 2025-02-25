import NavBar from "./components/NavBar";
import Home from "./Routes/Home.jsx";
import Swipe from "./Routes/Swipe.jsx";
import { Routes, Route } from "react-router-dom";
import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  return (
    <div className="App">
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/swipe" element={<Swipe />} />
      </Routes>
    </div>
  );
}
export default App;
