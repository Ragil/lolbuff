var webpack = require('webpack');
var webpack_loaders = require('./webpack.loaders');

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

  resolve: {
    extensions: ['', '.js', '.jsx']
  }
}
