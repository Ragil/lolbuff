import React from "react";
import SearchComponent from "../../common/search_component";
import "!style!css!less!./page.less";
//import img_league_dominion_url from "../../../assets/league_dominion.jpg"

export default class HomePage extends React.Component {
  render() {
    return (
      <div id="home-page" className="home-page">
        <div className="row">
          <div className="col-xs-1 col-sm-2 col-md-3 col-lg-3"></div>
          <div className="col-xs-10 col-sm-8 col-md-6 col-lg-6">
            <h1 className="header">League Buff</h1>
          </div>
          <div className="col-xs-1 col-sm-2 col-md-3 col-lg-4"></div>
        </div>
        <div className="row">
          <div className="col-lg-12">
            <SearchComponent/>
          </div>
        </div>
      </div>
    );
  }
};
