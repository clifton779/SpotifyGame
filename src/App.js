import './App.css';
import React, { useState, useEffect, useRef } from 'react';
import Player from './Player';
import Timer from './Timer';

function App() {
  const [time, setTime] = useState(null);
  const [music, setMusic] = useState([]);
  const [song, setSong] = useState('default');
  const [name, setName] = useState('default');
  const [guessing, setGuessing] = useState('');
  const inputRef = useRef();
  const timeRef = useRef(); // to get data from Timer componet
  const [score, setScore] = useState(0);
  const [next, setNext] = useState(1);

  useEffect(() => {
    fetch('/getsongs')
      .then((response) => response.json())
      .then((data) => {
        setMusic(data.songs);
        setSong(data.songs[0].url);
        setName(data.songs[0].name);
      });
  }, []);

  // This function will increment the song and when it reaches 5 it will reset to 0
  const nextSong = () => {
    if (next === 4) {
      setNext(0);
      setSong(music[next].url);
      setName(music[next].name);
    } else {
      setNext(next + 1);
      setSong(music[next].url);
      setName(music[next].name);
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

  return (
    <div className="App">
      <h3 className="ScoreDisplay">{score}</h3>
      <h3 ClassName="Time">{time}</h3>
      <Player url={song} />
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
