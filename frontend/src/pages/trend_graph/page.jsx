import React from "react";
import MG from "metrics-graphics/index";
import "!style!css!metrics-graphics/dist/metricsgraphics.css";
import "!style!css!less!./page.less";
import moment from "moment/moment";
import $ from "jquery/dist/jquery";

export default class TrendGraph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hidden : {}
    };
  }

  render() {
    let avg_label = (this.props.metric === 'games') ? 'total' : 'avg';

    return (
      <div id="trend-graph">
        <div className="trend-graph-svg-container"
            style={{
              width : (this.props.width + 20) + 'px',
              height : (this.props.height) + 'px'
            }}>
          <div className="trend-graph-legend">
            <span className="mg-line1-legend-color">-- daily </span>
            <span className="mg-line2-legend-color"
                onClick={() => this.hideData.apply(this,[1])}>-- {avg_label} </span>
          </div>
          <div className="trend-graph-rollover-text"></div>
        </div>
      </div>
    );
  }

  hideData(index) {
    let hidden = $.extend({}, this.state.hidden);
    hidden[index] = !hidden[index];
    this.setState({ hidden : hidden });
  }

  drawGraph() {
    let data = [this.props.trend.data_day, this.props.trend.data_day_cumulative];
    console.log(this.state.hidden);
    data = data.filter((d, i) => !this.state.hidden[i]);
    data = data.map((group) => {
      return group.map((d) => {
        return {value : d[1], date : d[0]};
      });
    });
    for (let i = 0; i < data.length; i++) {
      //data[i] = MG.convert.date(data[i], 'date');
    }

    MG.data_graphic({
      title : this.props.trend.name,
      data : data,
      missing_is_hidden : false,
      width : this.props.width,
      height : this.props.height,
      target : '.trend-graph-svg-container',
      x_accessor : 'date',
      y_accessor : 'value',
      xax_format : ((d) => moment(d.date).format('YYYY-MM-DD')),

      // custom rollover text
      show_rollover_text : false,
      mouseover : ((d, i) => {
        let text = moment(d.date).format('ll');
        text = text + ' ' + this.props.trend.name + ' ' + d.value;
        $('.trend-graph-rollover-text').html(text);
      }),
      mouseout : () => $('.trend-graph-rollover-text').html(''),

      full_height : true,
      full_width : true,
      animate_on_load : true,
      area : false,
      chart_type : 'line',
      interpolate_tension : 1
    });
  }

  componentDidMount() {
    this.drawGraph();
  }

  componentDidUpdate() {
    this.drawGraph();
  }
}

TrendGraph.propTypes = {
  width : React.PropTypes.number.isRequired,
  height : React.PropTypes.number.isRequired,
  metric : React.PropTypes.string.isRequired,
  trend : React.PropTypes.object.isRequired
};
