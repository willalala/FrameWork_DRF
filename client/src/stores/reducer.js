//与useSelector、useDispatch钩子相关联，进行访问和更新store中的状态
import { createSlice } from "@reduxjs/toolkit"

const initialState={
    name:'',
    age:0,
    password:''
}

const personSlice=createSlice({
    name:'person',
    initialState,
    reducers:{
        updateName:(state,action)=>{
            state.name=action.payload
        },
        updateAge:(state,action)=>{
            state.age=action.payload
        }
    }
})
export const {updateName,updateAge} =personSlice.actions

export default personSlice.reducer