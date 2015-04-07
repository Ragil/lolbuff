var webpack = require('webpack');
var webpack_loaders = require('./webpack.loaders');
var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');

/**
 * This is the Webpack configuration file for production.
 */
module.exports = {
  entry: "./src/main",

  output: {
    path: __dirname + "/build/",
    filename: "app.js"
  },

  module: {
    loaders: webpack_loaders
  },

  plugins : [
    new HtmlWebpackPlugin({
      filename : 'index.html',
      template : './index.html',
      hash : new Date().valueOf()
    })
  ],

  resolve: {
    root : path.resolve(__dirname, '.'),
    alias : {
      'env' : 'src/common/env_prod.js'
    },
    extensions: ['', '.js', '.jsx']
  }
}
