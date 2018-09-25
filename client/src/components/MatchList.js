import React, { Component } from 'react';
import PointsHeader from '../components/PointsHeader';
import TeamPoints from '../components/TeamPoints';
import axios from 'axios';

export default class MatchesList extends Component {
  state = {
    matches: []
  }

  componentDidMount() {
    axios.get("http://localhost:4000/matches")
      .then(res => {
         
        const matches = res.data;
        this.setState({matches});
        
      })
  }

  render() {
   
  
    return (
      <div >
       { this.state.matches.map(match => 
        <div key={match._id} className="" >
          <h2>{match.team1} vs {match.team2}</h2>
          <table  className="table-striped table-dark text-center" style={{margin:'auto',width:'50%'}}>
            
            <tbody>
            
            <PointsHeader pointsHeader={match["pointsHeader"]} />
            <TeamPoints teamPoints={match["team1Points"]} />
            <TeamPoints teamPoints={match["team2Points"]} />
            
            </tbody>
          </table>
        </div>
        )
      }
      </div>
    )
  }
}