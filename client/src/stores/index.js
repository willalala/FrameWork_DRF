//创建redux store
//安装redux的命令使用了npm install @reduxjs/toolkit react-redux

import { configureStore } from "@reduxjs/toolkit"
import personReducer from './reducer'

export const store=configureStore({
    reducer:{
        person:personReducer
        //可按需增加
    }
})