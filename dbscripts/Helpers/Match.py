import re
import json

class Match(object):
    def __init__(self, team1,team2,sets,pointDist,team1HittingDist,team2HittingDist):
        self.team1 = team1
        self.team2 = team2
        self.sets = sets
        self.pointDist = pointDist
        self.team1HittingDist = team1HittingDist
        self.team2HittingDist = team2HittingDist
        
	

