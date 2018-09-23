const Match = require('../models/match.model.js');

// Create and Save a new Note
exports.create = (req, res) => {
    // Validate request
    //console.log(req.body)
    if(!req.body.team1) {
        return res.status(400).send({
            message: "Team1 cannot be empty"
        });
    }

    if(!req.body.team2) {
        return res.status(400).send({
            message: "Team2 cannot be empty"
        });
    }

    // Create a Match
    const match = new Match({
        team1: req.body.team1 || "NA", 
        team2: req.body.team1 || "NA", 
        sets: req.body.sets || [], 
        pointDistribution: req.body.pointDistribution || [[]], 
        team1HittingDistribution: req.body.team1HittingDistribution || [[]],
        team2HittingDistribution: req.body.team2HittingDistribution || [[]], 
    });

    // Save Note in the database
    match.save()
    .then(data => {
        res.send(data);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while creating the Match."
        });
    });
};

// Retrieve and return all notes from the database.
exports.findAll = (req, res) => {
    Match.find()
    .then(matches => {
        res.send(matches);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while retrieving matches."
        });
    });
};

// Find a single match with a matchId
exports.findOne = (req, res) => {
    Match.findById(req.params.matchId)
    .then(match => {
        if(!match) {
            return res.status(404).send({
                message: "Match not found with id " + req.params.matchId
            });            
        }
        res.send(match);
    }).catch(err => {
        if(err.kind === 'ObjectId') {
            return res.status(404).send({
                message: "Match not found with id " + req.params.matchId
            });                
        }
        return res.status(500).send({
            message: "Error retrieving match with id " + req.params.matchId
        });
    });
};

// Delete a note with the specified matchId in the request
exports.delete = (req, res) => {
    Match.findByIdAndRemove(req.params.matchId)
    .then(match => {
        if(!match) {
            return res.status(404).send({
                message: "Match not found with id " + req.params.matchId
            });
        }
        res.send({message: "Note deleted successfully!"});
    }).catch(err => {
        if(err.kind === 'ObjectId' || err.name === 'NotFound') {
            return res.status(404).send({
                message: "Match not found with id " + req.params.matchId
            });                
        }
        return res.status(500).send({
            message: "Could not delete match with id " + req.params.matchId
        });
    });
};
