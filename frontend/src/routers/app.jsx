import React from "react";
import Router from "react-router";
let { Route, DefaultRoute, RouteHandler } = Router;

import HomePage from "../pages/home/page";
import SearchPage from "../pages/search/page";
import "!style!css!less!bootstrap/less/bootstrap.less";
import env from "env";

export default class AppRouter extends React.Component {
  render() {
    return (
      <div id="container" className="container">
        <div id="main">
          <RouteHandler {...this.props} />
        </div>
      </div>
    );
  }
}

AppRouter.getRoutes = function() {
  return (
    <Route name="app" path="/" handler={AppRouter}>
      <DefaultRoute handler={HomePage} />
      <Route name="search" path="/s" handler={SearchPage} />
    </Route>
  );
}
