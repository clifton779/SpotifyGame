import React from 'react';

function Timer(props, ref) {
  const [time, setTime] = React.useState(30000);
  const [timerOn, setTimerOn] = React.useState(true);
  const interval = React.useRef(10); // initalized with 10 to meet condtional in use state
  const isNeg = (num) => {
    // returns 0 if time is negative
    if (num < 0) {
      return 0;
    }
    return num - 10;
  };

  // update time
  React.useEffect(() => {
    //  restart time after submit button is clicked
    if (!timerOn) {
      setTimerOn(true);
    }

    if (time <= 0) {
      clearInterval(interval.current);
    } else if (interval.current >= 0 && timerOn) {
      interval.current = setInterval(() => {
        setTime((previousTime) => isNeg(previousTime)); // decrement by 10 ms
      }, 10); // updates every 10 ms
    } else {
      clearInterval(interval.current);
    }
  }, [timerOn]);

  // ensures timer is stoped at 0
  if (time <= 0) {
    clearInterval(interval.current);
  }
  // send data to parent componet (App)
  React.useImperativeHandle(ref, () => ({
    getTime: time,
    setTime: () => setTime(30000),
    stopTime: () => setTimerOn(false),
    startTime: () => setTimerOn(true),
  }));

  return (
    <div className="App">
      <div>
        <span>
          {/* minutes */}
          {(`0${Math.floor(time / 60000) % 60}`).slice(-2)}
          :
        </span>
        {' '}
        <span>
          {/* seconds */}
          {(`0${Math.floor(time / 1000) % 60}`).slice(-2)}
          :
        </span>
        {' '}
        {/* miliseconds */}
        <span>{(`0${(time / 10) % 100}`).slice(-2)}</span>
        {' '}
      </div>
    </div>
  );
}

export default React.forwardRef(Timer);
