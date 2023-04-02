import React from "react";
import "../App.css";

export const ItemList = ({ data, getTopTracks }) => {
  // console.log(data)
  // console.log(getTopTracks);

  return (
    <div className="list-container">
      <div className="list-header">Top Tracks</div>
      <div className="list-options">
        <p>Time period:</p>
        <button
          className="btn btn-dark"
          onClick={() => getTopTracks("short_term")}
        >
          Last 4 weeks
        </button>
        <button className="btn btn-dark" onClick={() => getTopTracks("medium_term")}>
          Last 6 months
        </button>
        <button className="btn btn-dark" onClick={() => getTopTracks("long_term")}>All time</button>
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
