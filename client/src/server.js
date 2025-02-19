import axios from 'axios'
// import store from 'store'//用于本地存储token
import settings from './etc/settings.json'

const Url=settings.url

const registerServer=async (data)=>{
    let res=await axios.post(`${Url}/user/register/`,data)
    console.log(res,'register')
    return res.data
}

const loginServer=async (data)=>{
    let res=await axios.post(`${Url}/user/login/`,data)
    console.log(res,'login')
    return res.data
}

const allUserServer=async ()=>{
    let res=await axios.get(`${Url}/user/all_users/`)
    console.log(res,'alluser')
    return res.data
}

const editUserServer=async (data)=>{
    let res=await axios.patch(`${Url}/user/edit_users/`,data)
    console.log(res,'edit')
    return res.data
}

const deleteUserServer=async(params)=>{
    let res=await axios.delete(`${Url}/user/delete_users/`,{params})
    console.log(res,'deleteuser')
    return res.data
}

export {
    registerServer,
    loginServer,
    allUserServer,
    editUserServer,
    deleteUserServer
}
