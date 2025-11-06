import logo from './logo.svg';
import './App.css';
import { getAllByText } from '@testing-library/dom';

import React, {useState, useEffect} from "react";

import CounterApp from './CounterApp';

function App() {
  return (
    <div>
      <Greeting name="Robbie" />
      <TimeDisplay />
      <CounterApp />
    </div>
  );
}

function Greeting({ name }) {
  return <h1>Hello, {name} 👋</h1>;
}


function TimeDisplay(){       
  {/*State: Holds current time as a string*/}{/*Currently STATIC*/}
  const [time, setTime] = useState(new Date().toLocaleTimeString());  {/*new Date creates a Data Variable. toLocaleTimeString sets to local time. */}

 {/*useEffect runs AFTER component appears on screen*/}
 {/*useEffect(aFunctionIprovide, anArrayIProvide) Knowing this helps to follow the brackets*/}
 useEffect(() => {

  {/*SetInterval: runs a function repeatedly every X milliseconds*/}
  {/*SerInterval(functionToRun, whenToRunIt)*/}
  const timer = setInterval(() => {
    {/*Every 1000ms update the time state */}
    setTime(new Date().toLocaleTimeString())
  }, 1000);

  {/*Cleanup runs AFTER a component disappears*/}
  {/*Stops the timer to prevent memory leaks*/}
  return () => clearInterval(timer);

  {/*[] Is part of useEffect, blank means run once]*/}
  }, []);


    return <p>The current time is: {time}</p>;
}


    



export default App;
