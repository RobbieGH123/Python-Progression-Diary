console.log("Day 1 warmup running!");

const name = "Robbie";  // Const locks the reference to the object not the contents
const age = 23;
const likesCoding = true;
const skills = ["HTML", "CSS", "JS"]; // Array
const profile = { name, age, likesCoding} // Object

console.log(profile);                     

console.log("First skill:", skills[0]);
console.log("Name:", profile.name);

profile.location = "Cornwall";
profile.age = 24;

console.log("Updated profile:", profile);

if (profile.age > 20) {  // Control flow (code that runs based on conditions)
    console.log(`${profile.name} is an adult.`);
} else {
    console.log(`${profile.name} is still a youngster.`);
}

// Starts a for loop that repeats a block of code
// i Starting at 0
// Continue looping as long as i is less than the total number of items in skills
// i++ (Increments i by 1 after each loop iteration)
for (let i = 0; i < skills.length; i++) {
    console.log(`Skill ${i + 1}: ${skills[i]}`);
}

function describeSkill(skill) {
    if (skill == "JS"){
        return "the core of everything!";
    } else {
        return "still useful!";
    }
}

console.log(describeSkill("HTML"));
console.log('\n')
console.log(describeSkill("JS"));
console.log('\n')


// Re-write of the prior function:
// "=>" Says that the constant variable "descirbeSkillArrow" is a function with 1 argument, skill
const describeSkillArrow = (skill) =>
    // Uses a ternary operator which is an if/else shortcut.
    // Ternary Structure: condition ? valueIfTrue : valueIfFalse;
    skill === "JS" ? "the core of everything!" : "still useful!";


console.log(describeSkillArrow("CSS"));
console.log('\n')

// Cleanup function
for (let key in profile) {
    if(profile[key] === undefined) {
        delete profile[key];
    }
}

// Modern function, uses an arrow and takes the argument as an equals = (argument)
const describeProfile = (profile) => {

    // Age check
    profile.age > 20
        ? console.log("Adult")
        : console.log("Youngster");

    // Loop through skills
    for (let key in profile) {
        console.log(`${profile[key]}`);
    }
    // Modern Looping method, loops through every value from the 0th to the nth index
    skills.forEach((skill, index) => {
        console.log(`Skill ${index + 1}: ${skill}`);
    });
};
describeProfile(profile);


// If else, non ternaries
const gradingApp = (score) => {
    if (score > 90) {
      console.log("Excellent work");
    } else if (score > 79 && score < 91) {
      console.log("Good work");
    } else {
        console.log("Needs improvment");
    }
};

gradingApp(85)

// Loop through each number in the array, add it to the total sum, return the sum after the loop is completed
const sumUp = (array) => {
    let sum = 0;
    array.forEach((number) => {
      sum += number;
    });
  return sum
};
console.log(sumUp([1, 2, 3, 4]))

// Establish the array as a constant variable
const numbers = [1, 2, 3, 4];
// Reduce the array 'numbers' to a single value, 
// Accumulator and parameter are passed in as arguments
// Accumulator defaults to 0 value. 
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum);