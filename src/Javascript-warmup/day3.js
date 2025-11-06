console.log("Day 3 warm-up:")

// This document is to show that when Javascript hits timer code, the timer begins, but continues to execute code that isn't indented within

console.log("Start");  // Runs immediately

// Run the setTimeout function (No arguments passed in), after 1000ms (1 second), thus printing Timeout finished! after 1 second. 
setTimeout(() => {
  console.log("Timeout finished!");
}, 1000);

console.log("End"); // Runs immediately, therefore console goes Start -> End -> Timeout finished


function doTask(taskName, delayMs, callback) {  // Create a Function that takes 3 arguments

  console.log(`Starting task: ${taskName}`);   // Upon function call, print this

  setTimeout(() => {                           // Then, open a timer, which runs the below code after its finished

  console.log(`Finished Task: ${taskName}`);   
  callback();                                  // Runs the function provided in the call
  }, 
  delayMs                                      // But, before executing the code above, it has to wait this long
  );
}                                              // Close function block

// Calling this function
// The callback is an arrow function, printing "Callback executed!" to the console

doTask("Task 1", 1000, () => {
  console.log("Callback executed!");
}); // Closes callback and closes arguments into doTask