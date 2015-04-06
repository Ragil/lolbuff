import React from "react";
import pusheen_url from "../../assets/pusheen.gif";
import "!style!css!less!./pusheen_loader.less";

export default class PusheenLoader extends React.Component {
  render() {
    return (
      <div className="row">
        <div className="col-xs-12 col-sm-12 col-md-12 col-lg-12">
          <img src={pusheen_url} className="pusheen-img" />
          <div className="pusheen-msg">{this.props.msg}</div>
        </div>
      </div>
    );
  }
}
