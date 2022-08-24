const path = require('path');
// const express = require('express');
// const router = express.Router();
//webpack打包项目 HtmlWrbpackPlugin生成产出HTML文件 user-agent把浏览器的UserAgent变成一个对象

const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
    entry: './src/index.js',//入口文件
    context: process.cwd(),//上下文目录
    mode: 'development',//开发模式
    output: {
        path: path.resolve(__dirname, 'dist'),//输出目录
        filename: 'monitor.js'//文件名
    },
    
    devServer: {
        static: path.resolve(__dirname,'dist'),//devServer静态文件根目录
        
        //onBeforeSetupMiddleware配置路由 express服务器
        onBeforeSetupMiddleware(devServer){
            devServer.app.get('/success', function(req, res){
                res.json({id : 1}); //200
            });
            devServer.app.post('/error', function(req, res){
                res.sendStatus(500); //500
            });
        }
       
        // onBeforeSetupMiddleware: function (devServer) {
        //     if (!devServer) {
        //       throw new Error('webpack-dev-server is not defined');
        //     }
      
        //     devServer.app.get('/success', function (req, res) {
        //       res.json({ id : 1});
        //     });
        //   },
      
        
    },

    plugins: [
        new HtmlWebpackPlugin({//自动打包出HTML文件
            template: './src/index.html',
            inject: 'head'
        })
    ]
} 