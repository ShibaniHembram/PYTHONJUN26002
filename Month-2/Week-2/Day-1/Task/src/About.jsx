import React from 'react'
import { Link } from 'react-router'

function About() {
  return (
    <div>
      <Link to="/detail">Detail</Link>
      <br></br>
      <Link to="/index">Index</Link>
    </div>
  )
}

export default About
