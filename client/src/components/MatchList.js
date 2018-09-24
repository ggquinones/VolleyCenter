import React, { Component } from 'react';

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
      <div>
       { this.state.matches.map(match => 
        <div key={match._id}>
          <h1>{match.team1} vs {match.team2}</h1>
          <table>
            <tbody>
            <tr>
            <td>
                {match["pointsHeader"].join(" ")}
              </td>
            </tr>
            <tr>
              <td>
                {match["team1Points"].join(" ")}
              </td>
            </tr>
            <tr>
              <td>
                {match["team2Points"].join(" ")}
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        )
      }
      </div>
    )
  }
}