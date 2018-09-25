import React, { Component } from 'react';


export default class PointsHeader extends Component {
    render() {  
    return (
      <tr>
          {this.props.pointsHeader.map(item =>{
             return <th>
                  {item}
              </th>
          })}
      </tr>
    )
  }
}