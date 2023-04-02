import React from "react";
import "./App.css";
import { useState } from "react";
import { ItemList } from "./components/ItemList";

export const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userData, setUserData] = useState(null);
  const [topTracksData, setTopTrackData] = useState([]);
  const [isDisabled, setIsDisabled] = useState(false);

  const getLogin = async () => {
    // console.log("LOGIN")
    fetch("http://127.0.0.1:5000/user")
      .then((response) => response.json())
      .then((data) => {
        setUserData(data);
        // console.log(data);
      });

    setIsLoggedIn(true);
    getTopTracks("medium_term");
  };

  const getTopTracks = (timeframe) => {
    fetch(`http://127.0.0.1:5000/top-tracks/${timeframe}`)
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        setTopTrackData(data);
      });
  };

  const makePlaylist = () => {
    fetch(`http://127.0.0.1:5000/make-playlist`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setIsDisabled(true);
      });
  };

  return (
    <>
      <div className="header">
        <div>{userData ? `Hi, ${userData.display_name}` : ""}</div>
        <div>Simplify</div>
      </div>
      {!isLoggedIn && (
        <div className="button-container">
          <button onClick={() => getLogin()}>Log in with Spotify</button>
        </div>
      )}
      {isLoggedIn && (
        <>
          <ItemList data={topTracksData} getTopTracks={getTopTracks}></ItemList>
          <div className="rec-box">
            <button
              onClick={() => makePlaylist()}
              className="btn btn-primary btn-lg"
              disabled={isDisabled}
            >
              {isDisabled ? "Playlist Created!" : "Make Recommendation Playlist"}
            </button>
          </div>
        </>
      )}
    </>
  );
};

export default App;
