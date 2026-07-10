import { useState } from 'react'
import './App.css'
import { useEffect } from 'react';

function App() {
  const [usersData,setusersData]=useState([])
  

  async function getUsersData(){
    try {
      let response = await fetch("https://jsonplaceholder.typicode.com/posts");
      let data=await response.json()
      console.log(data);
      
    } catch (error) {
      console.log(error)
    }
  }
  useEffect(()=>{
    getUsersData()
  },[])
  
  return (
    <>
      Hlo
    </>
  )
}

export default App
