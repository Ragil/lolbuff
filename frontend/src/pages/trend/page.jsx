import React from "react";
import PusheenLoader from "../../common/pusheen_loader";
import TrendGraph from "../trend_graph/page";
import $ from 'jquery';
import env from 'env';

export default class TrendPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'fetched' : false
    };
  }

  render() {
    let content;

    if (this.state.fetched && !this.state.error) {
      content = <TrendGraph width={600} height={300}
          trend={this.state.data.trend} {... this.props} />
    } else if (this.state.fetched && this.state.error) {
      content = <h1>{this.state.error.error_msg}</h1>
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
    $.ajax(env.api_url + '/api/trends?' + $.param({
      'region' : this.props.region,
      'metric' : this.props.metric,
      'summoner_name' : this.props.summoner_name
    })).success((data, status, jqXHR) => {
      this.setState({
        data : data,
        fetched : true
      });
    }).fail((jqXHR, status, error) => {
      this.setState({
        error : jqXHR.responseJSON,
        fetched : true
      });
    });
  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      fetched : false
    });
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

TrendPage.propTypes = {
  region : React.PropTypes.string.isRequired,
  metric : React.PropTypes.string.isRequired,
  summoner_name : React.PropTypes.string.isRequired
};
TrendPage.defaultProps = {
  metric : 'goldpm'
};
