import React from "react/addons";
let { TestUtils } = React.addons;

import HomePage from "../../src/pages/home/page";

describe("HomePage Component", function() {
  it("should render with data props", function() {
    let homePageComponent = TestUtils.renderIntoDocument(
      <HomePage />
    );

    let heading = TestUtils.findRenderedDOMComponentWithTag(
      homePageComponent, "h1");
  });
});
