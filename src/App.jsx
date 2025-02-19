import "./App.css";
import NavBar from "./components/NavBar";
import Home from "./Routes/Home.jsx";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </>
  );
}
export default App;
