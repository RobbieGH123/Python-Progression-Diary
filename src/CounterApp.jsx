// CounterApp.jsx

// Import React and Hooks, CSS styling and Re-usable Button Component
import React, { useState, useEffect } from "react";
import "./CounterApp.css";
import Button from "./Button";

// Main Function which contains a child (Incrementer)
function CounterApp() { 
  return (
    <div className="counter-app">
      <h1 className="main-header">Counter App</h1>
      {/* Render the Incrementer Component */}
      <Incrementer />
    </div>
  );
}


// Deals with Setting, Initalizing, User Input and Button Interactions
function Incrementer() {
    // Current Value
    const [value, setValue] = useState(0); 
    // How much to Increment Value by
    const [step, setStep] = useState(1)
    // How many times have the buttons been clicked
    const [click, setClick] = useState(0)
    

    // These Next 2 functions increment value by step and tracks the click
 function buttonClick(){
    setValue(value + step);
    setClick(click + 1);
 }
 function buttonClickNeg(){
   setValue(value - step);
   setClick(click + 1);
 }
   //  Resets the states to their Initial Values.
 function buttonClickReset(){
  setValue(1);
  setStep(1);
  setClick(click + 1);
 }
   // Automatically Increments Value every 1 second, taking their latest states
 useEffect(() => {
  const ValTimer = setInterval(() => {
    // Grabs the freshest Value by saying "I want the previous value, with step added"
  setValue(prev => prev + step)
 },1000);

  // Cleanup: clears interval when component unmounts or step changes
  return () => clearInterval(ValTimer);
 }, [step]);

 return (
    <div className="incrementer">   
      <p className="counter-value">Current Value: {value}</p>
      <p className="click-value">Total Clicks: {click}</p>
      {/* Seeking User Input: */}
      <input 
        // User Input will be a number
        type="number"
        // The initial value comes from the step, which is 1.
        value={step}
        // If any changes occurs, sets step, in number format, giving it the specified value.
        onChange={(e) => setStep(Number(e.target.value))} />
      <Button className ="button-add" handleClick={buttonClick}
        label="Add" />
      <Button className = "button-subtract" handleClick={buttonClickNeg}
        label="Subtract" />
      <Button className = "button-reset" handleClick={buttonClickReset}
       label="Reset" />
    </div>
  );
 };


export default CounterApp;
