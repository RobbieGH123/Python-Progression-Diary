console.log("Day 2 warm-up:")

// An array of numbers
const numbers = [2, 5, 8, 10, 13];
console.log("Original:", numbers);


// .map is a built in method that creates a new array by applying a function to every item in an array
// num => num * 2: An arrow function that takes each number and doubles it
const doubled = numbers.map(num => num * 2)
console.log("Doubled:", doubled)


// .filter is a built in method that returns a new array with only the elements that pass a test
// num => num % 2 == 0: An arrow function that takes each number and returns it, if it is divisible by 2.
const evens = numbers.filter(num => num % 2 == 0)
console.log("Evens:", evens)
console.log('\n')


// Objects, Nested Data

const users = [
    { name: "Jake", score: 45 },
    { name: "Amy", score: 80 },
    { name: "Rosa", score: 60 },
];

const passed = users.filter(user => user.score >= 60);
console.log("Passed:", passed)

const names = users.map(user => user.name)
console.log("Names:", names)


// .reduce applies a function to each element, returning a single result
// Add each users score to the sum, with its initial value starting 0
// Divide that sum by the amount of users.#
const average = users.reduce((sum, user) => sum + user.score, 0) / users.length;
console.log("Average:", average)

const highestScore = users.reduce((highest, user) => Math.max(highest, user.score), 0)
console.log("Highest score:", highestScore)

// FUNCTIONS:

function greet(name) { 
    console.log(`Hello ${name}!`);
}

// Stores the greet function in the variable
let sayHi = greet;

// Declares a function named 'runFunction' which takes 2 arguments, a function and a value
function runFunction(fn, value) {
  console.log("About to run the function...");
  // Runs the function that was passed in as an argument
  fn(value); 
}

// Running the function (function(greet), value)
runFunction(sayHi, "robbie")
runFunction(greet(), ("Robbie"));



