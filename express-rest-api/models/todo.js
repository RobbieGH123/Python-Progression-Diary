const mongoose = require ('mongoose');  


    // 'text' field must be a string and is required
const taskSchema = new mongoose.Schema({
    text: { type: String, required: true},

    // 'completed' field must be a Boolean and is default False
    completed: { type: Boolean, default: false},
});


// Export a module named 'Task' based on taskSchema
module.exports = mongoose.model('Task', taskSchema);




