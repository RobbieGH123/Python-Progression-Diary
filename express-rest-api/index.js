const mongoose = require('mongoose');                                    // Imports the Mongoose library - used to connect to MongoDB
require('dotenv').config();                                 // Loads environment variables from .env, parses key value pairs into process.env

const express = require('express');                                      // Store the express module
const app = express();                                                   // Create an express application instance
const PORT = 3000;                                                       // Define the port number the server will listen on

app.use(express.json());                                                 // Take any raw JSON data sent in an HTTP request and convert into a usable JS object
 
app.get('/', (req, res) => {                                             // Define a GET route at the root url (http://localhost:3000/)
  res.send('Server is running!');                                          // In plain text, respond "Server is running!"
});

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI)                                  // Now pull the MONGO_URI key's value from process.env and connect to it
  .then(() => console.log('✅ Connected to MongoDB'))                     // If successful 
  .catch(err => console.error('❌ MongoDB connection error:', err));      // If not 
//


app.listen(PORT, () => console.log(`Server running on port ${PORT}`));   // Start the server, listen fr requests, once running, log message  


const users = [                                                          // Define an array of users
  { id: 1, name: 'Alice' },                                                
  { id: 2, name: 'Bob' },
];

// ----Mongo DB Array----

const User = require('./models/users');  // Import Mongoose Model for the User collection

//──────────────────────────────────────────────────────────────────────── Express.js GET Route ────────────────────────────────────────────────────────────────────────

app.get('/users', (req, res) => {                                        // When someone requests user data:
  res.json(users);                                                         // Takes the array, converts into JSON format, and responds with it
});
app.get('/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) {
    return res.status(404).send('User not found');
  }
  res.json(user);
});

//──────────────────────────────────────────────────────────────────────── MongoDB GET Route ────────────────────────────────────────────────────────────────────────

app.get('/db-users', async (req, res) => {                    // GET Route to fetch all users from MongoDB
  try {
    const users = await User.find();                          // Await all of the User documents are received from the user collection
    res.json(users);                                            // Send the array of users as a JSON response
  } catch (err) {                                               // In an error occurs during the DB query
    res.status(500).json({ error: err.message });             // Set HTTP error code, and respond "error" with a message
  }
});

//──────────────────────────────────────────────────────────────────────── Express.js POST Route ────────────────────────────────────────────────────────────────────────

app.post('/users', (req, res) => {                                       // Define a post route at users

    // Checks if name is missing
    if (!req.body.name) return res.status(400).send('Name is required');
    
    // Checks if name is a duplicate
    else if (users.some(u => u.name === req.body.name)) return res.status(500).send('Cannot create duplicates')
        
    const newUser = {                                                      // Creates a new user object to be added to the array
        id: users.length + 1,                                                // Assigns an ID to said user, that is equal to the last id+1
        name: req.body.name,                                                 // Set the name to the name sent in the body of the request
    };                                                                     // End of the new user aspect of the Call-back function
    users.push(newUser);                                                   // Append the new user to the users array
    res.status(201).json(newUser);                                    // HTTP status code 201 (created) + send the newUser to client in JSON format
});
// This is easiest to test via tools such as Hopsscotch or Postman, but can also be done via VScode

//──────────────────────────────────────────────────────────────────────── Mongo DB Post Route ────────────────────────────────────────────────────────────────────────

app.post('/db-users', async (req, res) => {                              // POST route to update Mongo DB collection
                                                                           // Marked as async co we can use await for database functions
  try {                                      
    if (!req.body.name) return res.status(400).send('Name is required'); // If the request body does not contain a name
                                                                           // Return a bad request response and a message 
    const newUser = new User({ name: req.body.name });       // Create newUser document instance using the mongoose model, initialise with name
    await newUser.save();                                    // Save it and don't move on until the save is complete

    res.status(201).json(newUser);                           // Respond with a successful POST status code and return the saved user as JSON
  } catch (err) {                                              // If any error occurs
    res.status(500).json({ error: err.message });                // Return "error": "Whatever the error message is"
  }
});

//──────────────────────────────────────────────────────────────────────── Mongo DB Update Route ───────────────────────────────────────────────────────────────────────

app.put('/db-users/:id', async (req, res) => {                   // Define a put route, ':id' part will be dynamic (: tells us)
  try {
    const { id } = req.params;                                   // Assigns id a value 
    const { name } = req.body;                                   // Extract the name field from the request body

    if (!name) return res.status(400).send('Name is required');  // If no name...

    const updatedUser = await User.findByIdAndUpdate(            // Search the User model which points to the User collection by document id

      id,                                                        // id to search for 
      { name },                                                  // The update operation: set name to new value
      { new: true }                                              // Option: return the updated document instead of the old one
    );

    if (!updatedUser) return res.status(404).send('User not found'); // If no document matched the id
    res.json(updatedUser);                                       // If successful, respond with the updatedUser in JSON 
  } catch (err) {                                                // Catch-all and error message print
    res.status(500).json({ error: err.message });
  }
});

//──────────────────────────────────────────────────────────────────────── Mongo DB Delete Route ──────────────────────────────────────────────────────────────────────

app.delete('/db-users/:id', async (req, res) => {                // Define a delete route, again we know id is dynamic

  try {                                                      
    const { id } = req.params;                                   // Assign id value (id) parameter)
    const deletedUser = await User.findByIdAndDelete(id);        // Again, search the model -> collection by document id

    if (!deletedUser) return res.status(404).send('User not found');  // If no document matched the id
    res.json({ message: 'User deleted successfully' });               // <- Else
  } catch (err) {                                                     // Error Catchall
    res.status(500).json({ error: err.message });
  }
});


//
//────────────────────────────────────────────────────────────────────────────To-Do App Routes────────────────────────────────────────────────────────────────────────

//────────────────────────────────────
// Import task model Schema
//────────────────────────────────────
const Task = require('./models/todo'); 

//────────────────────────────────────
// GET all tasks:
//────────────────────────────────────
app.get('/db-tasks', async (req,res) => {
  try {
    // Fetch all tasks from the database
    const tasks = await Task.find();
    // Return tasks in JSON format
    res.json(tasks);
  } catch (err) {
    // Handle database errors
    res.status(500).json({ error: err.message});
  }
});

//────────────────────────────────────
// POST a new task: 
//────────────────────────────────────

app.post('/db-tasks', async (req, res) => {

  try {
    if (!req.body.text) return res.status(400).send('Task input is required');
    
    // Create a new Task instance with the provided text
    const newTask = new Task({ text: req.body.text });

    // Wait for the new task to be saved to the DB
    await newTask.save();

    res.status(201).json(newTask);
  } catch (err) {
  res.status(500).json({ error: err.message});
  };
});

//────────────────────────────────────
// UPDATE task by ID:
//────────────────────────────────────

app.put('/db-tasks/:id', async (req, res) => {

  try {

    // Find task by ID and update with request body
    // This is quicker than previous where I assigned :id and req.body to variables
    const updatedTask = await Task.findByIdAndUpdate(req.paramas.id, req.body, { new: True} );

    if (!updatedTask) return res.status(404).send('Task not found');

    res.json(updatedTask);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

//────────────────────────────────────
// DELETE task by ID:
//────────────────────────────────────

app.delete('/db-tasks/:id', async (req, res) => {

  try {

    // Find task by ID and update with request body
    // This is quicker than previous where I assigned :id and req.body to variables
    const deletedTask = await Task.findByIdAndDelete(req.paramas.id, req.body, { new: True} );

    if (!deletedTask) return res.status(404).send('Task not found');

    res.json({ message: "Task deleted"});
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});





