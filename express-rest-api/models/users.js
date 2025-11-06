const mongoose = require('mongoose');                      // Import Mongoose library so that I can interact with MongoDB and create schemas

const userSchema = new mongoose.Schema({                   // A Schema describes the structure for documents within a collection
    name: { type: String, required: true, unique: true }   // Name is the sole field, Must be a string, required and not a duplicate
});

module.exports = mongoose.model('User', userSchema);

// Exportable | Register with mongo DB | Named User and based off the Schema