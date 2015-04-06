import React from "react";
import SearchComponent from "../../common/search_component.jsx";
import TrendPage from "../trend/page";

export default class SearchPage extends React.Component {
  render() {
    return (
      <div id="search-page" className="search-page">
        <div className="row">
          <div className="col-xs-4 col-sm-4 col-md-3 col-lg-3">
            <h4>League Buff</h4>
          </div>
          <div className="col-xs-8 col-sm-8 col-md-9 col-lg-9">
            <SearchComponent value={this.props.routestate.query['summoner_name']}
                region={this.props.routestate.query['region']} />
          </div>
        </div>

        <div className="row">
          <TrendPage {... this.props}
              region={this.props.routestate.query['region']}
              metric={this.props.routestate.query['metric']}
              summoner_name={this.props.routestate.query['summoner_name']}/>
        </div>
      </div>
    );
  }
};
