import React from "react";
import MG from "metrics-graphics/index";
import "!style!css!less!./page.less";
import moment from "moment/moment";
import $ from "jquery/dist/jquery";

export default class TrendGraph extends React.Component {
  render() {
    return (
      <div id="trend-graph">
        <div className="trend-graph-svg-container"
            style={{
              width : (this.props.width + 20) + 'px',
              height : (this.props.height) + 'px'
            }}>
          <div className="trend-graph-rollover-text"></div>
        </div>
      </div>
    );
  }

  drawGraph() {
    let data = [];
    for (let i = 0; i < 100; i ++) {
      let t = 1428310348000 - i * 86400000;
      data.push({ value : i, time : t });
    }
    console.log(data);

    MG.data_graphic({
      data: data,
      width : this.props.width,
      height : this.props.height,
      target : '.trend-graph-svg-container',
      x_accessor: 'time',
      xax_format : (t) => moment(t).format('ll'),
      y_accessor: 'value',

      // custom rollover text
      show_rollover_text : false,
      mouseover : ((d, i) => {
        $('.trend-graph-rollover-text').html(d.value);
      }),
      mouseout : () => $('.trend-graph-rollover-text').html(''),

      animate_on_load : true,
      area : false,
      chart_type : 'line'
    });
  }

  componentDidMount() {
    this.drawGraph();
  }

  componentDidUpdate() {
    this.drawGraph();
  }
}
