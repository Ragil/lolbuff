import React from "react";
import PusheenLoader from "../../common/pusheen_loader";
import TrendGraph from "../trend_graph/page";
import $ from 'jquery';
import env from 'env';
import moment from 'moment/moment';

export default class TrendPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'fetched' : false,
      'fetching' : false,
      'ts_startFetch' : undefined,
      'ts_lastFetchUpdate' : undefined
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
      let timeSinceLoad = this.state.ts_lastFetchUpdate - this.state.ts_startFetch;
      let pusheenCount = parseInt(timeSinceLoad / 5000, 10);
      let msg = "Generating data for the first time ...";
      if (pusheenCount === 1) {
        msg = "This is what's currently happening in the background ...";
      } else if (pusheenCount === 2) {
        msg = "We've doubled the power! Almost done ...";
      } else if (pusheenCount === 3) {
        msg = "You have lots of games. All of our staff are working on it!";
      } else if (pusheenCount > 3) {
        msg = "This is hard ... we need ZzzZzzZzzZzz";
      }

      content = <PusheenLoader pusheenCount={pusheenCount} msg={msg} />;
    }

    return (
      <div id="trend-page">
        {content}
      </div>
    );
  }

  updateFetchTimer() {
    window.setTimeout((() => {
      if (this.state.fetching) {
        this.setState({
          ts_lastFetchUpdate : moment().valueOf()
        });
        this.updateFetchTimer();
      }
    }).bind(this), 1000);
  }

  fetchData() {
    if (this.state.fetched || this.state.fetching) {
      return;
    }

    this.setState({
      fetching : true,
      ts_startFetch : moment().valueOf(),
      ts_lastFetchUpdate : moment().valueOf()
    });

    $.ajax(env.api_url + '/api/trends?' + $.param({
      'region' : this.props.region,
      'metric' : this.props.metric,
      'summoner_name' : this.props.summoner_name
    })).success((data, status, jqXHR) => {
      this.setState({ data : data });
    }).fail((jqXHR, status, error) => {
      this.setState({ error : jqXHR.responseJSON });
    }).done(() => {
      this.setState({
        fetched : true,
        fetching : false,
        ts_startFetch : undefined,
        ts_lastFetchUpdate : undefined
      });
    });

    this.updateFetchTimer();
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
    this.fetchData();
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
