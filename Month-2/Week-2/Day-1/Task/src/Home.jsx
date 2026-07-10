import React from 'react'
import { Link } from 'react-router'

function Home() {
  return (
    <div>
      <h1>Home </h1><br/>
      <Link to="/about">About</Link>
    </div>
  )
}

export default Home
