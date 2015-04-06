import React from "react/addons";
import { RouteHandler } from "react-router";
let { TestUtils } = React.addons;


import stubRouterContext from "./stub_router_context";
import AppRouter from "../../src/routers/app";


describe("LoggedIn Router", function() {
  let routerComponent;

  beforeEach(function() {
    let StubbedAppRouter = stubRouterContext(AppRouter);
    routerComponent = TestUtils.renderIntoDocument(<StubbedAppRouter />);
  });

  it("should return routes", function() {
    let routes = AppRouter.getRoutes();
    expect(routes).to.exist;
  });

  it("should include <RouterHandler> component", function() {
    let handler = TestUtils.findRenderedComponentWithType(
      routerComponent, RouteHandler);

      expect(handler).to.exist;
  });
});
