module.exports = (app) => {
    const matches = require('../controllers/match.controller.js');

    app.use(function(req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
      });

    // Create a new Match
    app.post('/matches', matches.create);

    // Retrieve all Matches
    app.get('/matches', matches.findAll);

    // Retrieve a single Match with matchId
    app.get('/matches/:matchId', matches.findOne);

    // Update a Match with matchId
    //app.put('/matches/:matchId', matches.update);

    // Delete a Match with matchId
    app.delete('/matches/:matchId', matches.delete);
}
