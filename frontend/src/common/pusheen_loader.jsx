import React from "react";
import pusheen_url from "./../../assets/pusheen.gif";
import pusheen_sleeping_url from "../../assets/pusheen_sleeping.png";
import "!style!css!less!./pusheen_loader.less";
import ReactSpinner from "./spin";

export default class PusheenLoader extends React.Component {
  render() {

    let spinner;
    if (this.props.pusheenCount) {
      let pusheen = [];
      let sleeping = this.props.pusheenCount > 3 ?
          Math.floor(Math.random() * 3) : -1;

      for (let i = 0; i < Math.min(3, this.props.pusheenCount); i++) {
        let url = sleeping === i ? pusheen_sleeping_url : pusheen_url;
        pusheen.push(<img src={url} className="pusheen-img" key={i} />);
      }

      spinner = (
        <div className="pusheen-container" style={{
            width : this.props.pusheenCount * 262
          }} >
          {pusheen}
        </div>
      );
    } else {
      spinner = <ReactSpinner config={{
        width : 5,
        radius : 10,
        top : '50%',
        left : '50%'
      }}/>
    }

    return (
      <div className="row pusheen-loader">
          {spinner}
        <div className="col-xs-12 col-sm-12 col-md-12 col-lg-12">
          <div className="pusheen-msg">{this.props.msg}</div>
        </div>
      </div>
    );
  }
}

PusheenLoader.propTypes = {
  pusheenCount : React.PropTypes.number.isRequired
};

PusheenLoader.defaultProps = {
  pusheenCount : 1
};
