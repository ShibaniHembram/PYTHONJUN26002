
import { Route, Routes } from 'react-router'
import './App.css'
import Home from './Home'
import Service from './Service'
import Admin from './Admin'
import Notfound from './Notfound'
import Dashboard from './Dashboard'
import Profile from './Profile'

function App() {

  return (
    <>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/service" element={<Service/>}></Route>
        <Route path='*' element={<Notfound/>}></Route>

        <Route path="/admin" element={<Admin/>}>
           <Route index element={<Dashboard/>}></Route>
           <Route path="Profile/:id" element={<Profile/>}></Route>
        </Route>   
      </Routes>
      </>
  )
}

export default App
