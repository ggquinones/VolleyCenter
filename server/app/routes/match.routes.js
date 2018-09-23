module.exports = (app) => {
    const matches = require('../controllers/match.controller.js');

    // Create a new Note
    app.post('/matches', matches.create);

    // Retrieve all Notes
    app.get('/matches', matches.findAll);

    // Retrieve a single Note with noteId
    app.get('/matches/:matchId', matches.findOne);

    // Update a Note with noteId
    //app.put('/matches/:matchId', matches.update);

    // Delete a Note with noteId
    app.delete('/matches/:matchId', matches.delete);
}
