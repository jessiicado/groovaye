import NavBar from "./components/NavBar";
import Home from "./Routes/Home.jsx";
import Swipe from "./Routes/Swipe.jsx";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Swipe" element={<Swipe />} />
          {/* <Route path="/callback" element={Callback />} */}
        </Routes>
      </div>
    </>
  );
}
export default App;
