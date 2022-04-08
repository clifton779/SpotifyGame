import './App.css';
import React, { useState, useEffect } from 'react';
import Player from './Player';

function App() {
  const [music, setMusic] = useState([]);
  const [song, setSong] = useState('');
  const [name, setName] = useState('');
  useEffect(() => {
    fetch('/getSongs')
      .then((response) => response.json())
      .then((data) => function handle() {
        setMusic(data.songs);
        setSong(music[0].url);
        setName(music[0].name);
      });
  });
  return (
    <div className="App">
      <Player url={song} name={name} />
    </div>
  );
}

export default App;
