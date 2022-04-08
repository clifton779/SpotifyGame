import './App.css';
import React, { useState, useEffect, useRef } from 'react';
import Player from './Player';
import Timer from './Timer';

function App() {
  const [time, setTime] = useState(null);
  const [music, setMusic] = useState([]);
  const [song, setSong] = useState('');
  const [name, setName] = useState('');
  const [guessing, setGuessing] = useState('');
  const inputRef = useRef();
  const timeRef = useRef(); // to get data from Timer componet
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
    setTime(timeRef.current.getTime / 1000); // gets time in seconds
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

  // reset timer after submit
  const handleReset = () => {
    timeRef.current.setTime();
    timeRef.current.stopTime();
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
      <h3 lassName="time">{time}</h3>
      <Player url={song} name={name} />
      <Timer ref={timeRef} />
      <div className="GuessBox">
        <p>{guessing}</p>
        <input className="GuessInput" type="text" ref={inputRef} data-testid="input-field" />
        <br />
        <br />
        <button className="GuessButton" type="button" onClick={() => { handleClick(); handleReset(); }}>Submit</button>
      </div>
    </div>
  );
}

export default App;
