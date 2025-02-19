import React,{useState} from "react";
import { registerServer,loginServer,allUserServer,editUserServer,deleteUserServer } from "../server";
const Login=()=>{
    
    const [username,setN]=useState('')
    const[password,setP]=useState('')
    const [userInfo,setInfo]=useState([])

    const handleChange=(type,e)=>{
        if(type==='name')
            setN(e.target.value)
        else
            setP(e.target.value)
    }

    const handleRegister=async()=>{
        let data={
            username:username,
            password:password
        }
        let res=await registerServer(data)
        console.log(res,'注册')
    }

    const handleLogin=async()=>{
        let data={
            username:username,
            password:password
        }
        let res=await loginServer(data)
        console.log(res,'登录')

    }

    const handleUserInfo=async()=>{
        let res=await allUserServer()
        let data=[]
        Object.keys(res.data).forEach((tp)=>{
            data.push({id:res.data[tp].id,
                username:res.data[tp].username,
                time:res.data[tp].time,
                password:res.data[tp].password})
        })
        setInfo(data)
        console.log(data)
        console.log(res,'查看用户')
    }

    const handleEdit=async()=>{
        let data={
            username:username,
            password:password
        }
        let res=await editUserServer(data)
        console.log(res,'编辑用户')
    }

    const handleDelete=async()=>{
        let params={
            username:username
        }
        let res=await deleteUserServer(params)
        console.log(res,'删除用户')
    }

    return(
        <div>
            <br />
            <div>--------------------------------------</div>
            <p>用户登录注册</p>
            <p>用户名：</p>
            <input onChange={(e)=>handleChange('name',e)} />
            <br />
            <p>密  码：</p>
            <input onChange={(e)=>handleChange('password',e)} />
            <br />
            <br />
            <button onClick={handleRegister}>注册</button>
            <button onClick={handleLogin}>登录</button>
            <button onClick={handleEdit}>编辑</button>
            <button onClick={handleDelete}>删除</button>
            <br />
            <br />
            <button onClick={handleUserInfo}>查看全部用户信息</button>
            <br/>
            <ul>
                {userInfo.map((temp,index)=>(
                    <li key={index}>
                        <div>{temp.username}</div>
                        <div>{temp.time}</div>
                        <div>{temp.id}</div>
                        <div>{temp.password}</div>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Login 