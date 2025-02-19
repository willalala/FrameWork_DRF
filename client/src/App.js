import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState } from 'react';
import Login from './login';

axios.defaults.withCredentials=true

axios.defaults.headers.post['Content-Type']='application/json'
const server='http://127.0.0.1:8000/'

function App() {

  const [name,setName]=useState("")
  const [age,setAge]=useState(0)

  const handleChange=(type,e)=>{
    // console.log(type)
    // console.log(e.target.value)
    if(type==='name')
      setName(e.target.value)
    else
      setAge(e.target.value)
    
  }

  const handleWrite=async ()=>{
    // console.log('write')
    let data={name:name,age:age}
    let res=await axios.post(`${server}/new_person/`,data)
    console.log(res,'write')
  }

  const handleRead=async (type)=>{
    let params
    if(type==='readonly')
      params={name:name}
    else
      params={name:''}
    let res=await axios.get(`${server}/all_person/`,{params})
    console.log(res,'read')
  }

  const handleDelete=async ()=>{
    let params={name:name}
    let res=await axios.delete(`${server}/delete_person/`,{params})
    console.log(res,'delete')
  }

  const handleEdit=async ()=>{
    let data={name:name,age:age}
    let res=await axios.patch(`${server}/edit_person/`,data)
    console.log(res,'edit')
  }

  return (
    <div className="App">
      <p>Willa First APP</p>
      <input onChange={(e)=>handleChange('name',e)} />
      <br />
      <input onChange={(e)=>handleChange('age',e)} />
      <br />
      <button onClick={handleWrite}>write</button>
      <button onClick={()=>handleRead('readonly')}>read</button>
      <button onClick={()=>handleRead('readall')}>readALL</button>
      <button onClick={handleDelete}>delete</button>
      <button onClick={handleEdit}>edit</button>
      <br />
      <Login />
    </div>
  );
}

export default App;
