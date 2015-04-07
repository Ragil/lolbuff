import React from "react";

export default class MetricSelector extends React.Component {
  render() {
    let metrics = {
      'goldpm' : 'GPM',
      'kda' : 'KDA',
      'winrate' : 'Win %',
      'games' : 'Games Played'
    };
    let buttons = Object.keys(metrics).map((key) => {
      let name = metrics[key];
      let btnClass = "btn " +
          (this.props.selectedMetric === key ? "btn-primary" : "btn-default");
      console.log(this.props.selectedMetric + ' ' + key + ' ' + btnClass);
      return (
        <button type="button" className={btnClass}
            onClick={() => this.selectMetric.apply(this, [key])}>{name}</button>
      );
    });

    return (
      <div className="metric-selector">
        <div className="btn-group" role="group">
          {buttons}
        </div>
      </div>
    );
  }

  selectMetric(metric) {
    this.context.router.transitionTo('/s', undefined, {
      'summoner_name' : this.props.summonerName,
      'metric' : metric,
      'region' : this.props.region
    });
  }
}

MetricSelector.propTypes = {
  selectedMetric : React.PropTypes.string.isRequired,
  summonerName : React.PropTypes.string.isRequired,
  region : React.PropTypes.string.isRequired
};
MetricSelector.defaultProps = {
  selectedMetric : 'goldpm'
};
MetricSelector.contextTypes = {
  router : React.PropTypes.func
};
