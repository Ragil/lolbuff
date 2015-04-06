import React from "react";
import SearchComponent from "../../common/search_component.jsx";
import TrendPage from "../trend/page";

export default class SearchPage extends React.Component {
  render() {
    return (
      <div id="search-page" className="search-page">
        <div className="row">
          <div className="col-xs-6 col-sm-6 col-md-4 col-lg-4">
            <h4>League Buff</h4>
          </div>
          <div className="col-xs-6 col-sm-6 col-md-8 col-lg-8">
            <SearchComponent value={this.props.routestate.query['q']}/>
          </div>
        </div>

        <div className="row">
          <TrendPage {... this.props} />
        </div>
      </div>
    );
  }
};
