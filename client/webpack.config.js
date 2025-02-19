const path=require('path')
const HtmlWebpackPlugin=require('html-webpack-plugin')
const {CleanWebpackPlugin}=require('clean-webpack-plugin')

module.exports={
    entry:'./src/index.js',
    output:{
        filename:'bundle.js',
        path:path.resolve(__dirname,'dist'),
        publicPath:'./'//设置为相对路径
    },
    module:{
        rules:[
            {
                test:/\.css$/,
                use:[
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test:/\.(png|svg|jpg|gif)$/,
                use:[
                    'file-loader'
                ]
            },
            {
                test:/\.(js|jsx)$/,//支持编译js和jsx语法
                exclude:/node_modules/,
                loader:"babel-loader"
            }
        ]
    },
    plugins:[
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            title:'first project',
            template:'public/index.html'
        })
    ],
    resolve:{//在打包时，.js文件以及.jsx文件都能作为有效路径被识别
        extensions:['.js','.jsx']
    },
    // devServer:{
    //     proxy:{
    //         '/user':{
    //             target:'http://localhost:8000',
    //             changeOrigin:true,
    //             secure:false
    //         }
    //     }
    // }
}