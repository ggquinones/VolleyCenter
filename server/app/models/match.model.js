const mongoose = require('mongoose');

const MatchSchema = mongoose.Schema({
    team1: String,
    team2:String,
    sets:[],
    gameNumber:Number,
    boxscorelink:String,
    season:String,
    pointsHeader:[],
    team1Points:[],
    team2Points:[]
    //team1HittingDistribution:[[]],
    //team2HittingDistribution:[[]]
}, {
    timestamps: true
});

module.exports = mongoose.model('Match', MatchSchema);
