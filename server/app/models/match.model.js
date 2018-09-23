const mongoose = require('mongoose');

const MatchSchema = mongoose.Schema({
    team1: String,
    team2:String,
    sets:[],
    pointDistribution:[[]],
    team1HittingDistribution:[[]],
    team2HittingDistribution:[[]],
}, {
    timestamps: true
});

module.exports = mongoose.model('Match', MatchSchema);
