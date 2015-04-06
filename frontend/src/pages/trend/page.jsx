import React from "react";
import PusheenLoader from "../../common/pusheen_loader";
import TrendGraph from "../trend_graph/page";

export default class TrendPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'fetched' : false
    };
  }

  render() {
    let content;

    if (this.state.fetched || true) {
      content = <TrendGraph width={600} height={300} />
    } else {
      content = <PusheenLoader msg="Generating data for the first time ..." />;
    }

    return (
      <div id="trend-page">
        {content}
      </div>
    );
  }

  fetchData() {
  }

  componentDidMount() {
    this.fetchData();
  }

  componentDidUpdate(prevProps, prevState) {
    if (!this.state.fetched) {
      this.fetchData();
      return;
    }
  }
}
