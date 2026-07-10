import React, { useState } from 'react'
import { Link } from 'react-router';

function Detail() {
    const [name, setName] = useState("");
    const [addres, setAddress] = useState("");
    const [phone, setPhone] = useState("");

    function handleSubmit(){
        console.log(name,addres,phone);
    }
  return (
    <div>
      <input type="text" placeholder='Enter your name' onChange={(e)=>setName(e.target.value)}/> <br />
      <input type="text" placeholder='Enter your addres' onChange={(e)=>setAddres(e.target.value)}/><br />
      <input type="number" placeholder='Enter the phone number' onChange={(e)=>setPhone(e.target.value)} /><br/>
      <button onClick={handleSubmit}>Detail</button>
    </div>
  )
}

export default Detail
