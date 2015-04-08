import React from "react";
import SearchComponent from "../../common/search_component.jsx";
import TrendPage from "../trend/page";
import "!style!css!less!./page.less";

export default class SearchPage extends React.Component {
  render() {
    return (
      <div id="search-page" className="search-page">
        <div className="navbar navbar-fixed-top navbar-inverse">
          <div className="container">
            <div className="search-page-bar row">
              <div className="col-xs-4 col-sm-4 col-md-3 col-lg-3">
                <a href="/">
                  <h4 className="search-page-title">League Buff</h4>
                </a>
              </div>
              <div className="search-page-input col-xs-8
                  col-sm-8 col-md-9 col-lg-9">
                <SearchComponent
                    value={this.props.routestate.query['summoner_name']}
                    region={this.props.routestate.query['region']} />
              </div>
            </div>
          </div>
        </div>

        <div className="row page-content">
          <TrendPage {... this.props}
              region={this.props.routestate.query['region']}
              metric={this.props.routestate.query['metric']}
              summoner_name={this.props.routestate.query['summoner_name']}/>
        </div>
      </div>
    );
  }
};
