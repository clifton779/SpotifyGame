import './App.css';
import React, { useState, useEffect, useRef } from 'react';
import Player from './Player';

function App() {
  const [music, setMusic] = useState([]);
  const [song, setSong] = useState('');
  const [name, setName] = useState('');
  const [guessing, setGuessing] = useState('');
  const inputRef = useRef();
  const [score, setScore] = useState(0);
  const [next, setNext] = useState(0);
  console.log(next);
  // This function will increment the song and when it reaches 5 it will reset to 0
  const nextSong = () => {
    if (next === 5) {
      setNext(0);
      setSong(music[next]);
    } else {
      setNext(next + 1);
      setSong(music[next]);
    }
  };
  // This prompts the user if their guess is right, sets the score, and goes to the next song.
  const handleClick = () => {
    const val = inputRef.current.value;
    if (val === name) {
      setGuessing('Correct!');
      setScore(score + 1);
    } else {
      setGuessing('Wrong Song.');
      setScore(() => {
        if (score === 0) {
          return 0;
        }
        return score - 1;
      });
      nextSong();
    }
    inputRef.current.value = '';
  };

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
      <h3 className="ScoreDisplay">{score}</h3>
      <Player url={song} name={name} />
      <div className="GuessBox">
        <p>{guessing}</p>
        <input className="GuessInput" type="text" ref={inputRef} data-testid="input-field" />
        <br />
        <br />
        <button className="GuessButton" type="button" onClick={handleClick}>Submit</button>
      </div>
    </div>

  );
}

export default App;
