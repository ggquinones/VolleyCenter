import React, { Component } from 'react';


export default class TeamPoints extends Component {
    render() {  
    return (
      <tr>
          {this.props.teamPoints.map(item =>{
             return <td>
                  {item}
              </td>
          })}
      </tr>
    )
  }
}