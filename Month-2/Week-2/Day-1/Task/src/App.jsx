import { useState } from 'react'
import './App.css'
import { Route,Routes } from 'react-router'
import Home from './Home'
import About from './About'
import Detail from './Detail'
import Index from './Index'


function App() {

  return (
    <>
     <Routes>
      <Route path='/' element={<Home/>}></Route>
      <Route path="/about" element={<About/>}>
      <Route path="detail" element={<Detail/>}></Route>
      <Route path="index" element={<Index/>}></Route>
      </Route>
     </Routes>
    </>
  )
}

export default App
