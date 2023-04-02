import React from "react";
import { useState } from "react";
import "../App.css";

export const ItemList = ({ data, getTopTracks }) => {
  const [activeButton, setActiveButton] = useState(2);
  // console.log(data)
  // console.log(getTopTracks);

  return (
    <div className="list-container">
      <div className="list-header">Top Tracks</div>
      <div className="list-options">
        <p>Time period:</p>
        <button
          className={activeButton === 1 ? "btn btn-success" : "btn btn-dark"}
          onClick={() => {
            getTopTracks("short_term");
            setActiveButton(1);
          }}
        >
          Last 4 weeks
        </button>
        <button
          className={activeButton === 2 ? "btn btn-success" : "btn btn-dark"}
          onClick={() => {
            getTopTracks("medium_term");
            setActiveButton(2);
          }}
        >
          Last 6 months
        </button>
        <button
          className={activeButton === 3 ? "btn btn-success" : "btn btn-dark"}
          onClick={() => {
            getTopTracks("long_term");
            setActiveButton(3);
          }}
        >
          All time
        </button>
      </div>
      <div className="list-wrapper">
        <ol>
          {data.map((item) => {
            return (
              <li>
                <div className="list-item">
                  <p>{item.artist_name}</p>
                  <p>-</p>
                  <p>{item.name}</p>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
};
