import React from 'react'
import { Link } from 'react-router'

function Home() {
  return (
    <div>
     This is Home page
     <nav>
        <ul>
            <li>
              <Link to="/">Home</Link> 
              <Link to="/about">About</Link>
              <Link to="/login">Login</Link>
            </li>
        </ul>
     </nav>
    </div>
  )
}

export default Home
