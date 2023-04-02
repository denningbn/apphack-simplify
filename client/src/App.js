import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [data, setData] = useState({});

  const getLogin = async () => {
    console.log("LOGIN")
    fetch("http://127.0.0.1:5000/user")
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });

    setIsLoggedIn(true);
  };

  const getTopTracks = () => {
    fetch("http://127.0.0.1:5000/top-tracks")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        return data;
      });
  };

  const top_tracks = isLoggedIn && getTopTracks()

  return (
    <>
      <div className="header">
        {data && <div>Hi, {data.display_name}</div>}
        <div>Test Title</div>
      </div>
      <div>
        {!isLoggedIn && (
          <button onClick={() => getLogin()}>Log in with Spotify</button>
        )}
      </div>
    </>
  );
}

export default App;
