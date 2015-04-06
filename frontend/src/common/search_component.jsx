import React from "react";
import "bootstrap/js/dropdown";
import "!style!css!less!./search_component.less";

export default class SearchComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      region : props.region
    };
  }

  render() {
    let regions = ['br', 'eune', 'euw', 'kr', 'lan',
        'las', 'na', 'oce', 'ru', 'tr'];
    let options = regions.map((region) => {
      return (
        <li role="presentation" key={region}>
          <a role="menuitem" tabIndex="-1"
              onClick={() => this.selectRegion.apply(this, [region])}>{region}</a>
        </li>
      );
    });

    return (
      <div className="search-bar">
        <div className="dropdown">
          <button className="btn btn-default dropdown-toggle" type="button"
              id="region-menu" data-toggle="dropdown" aria-expanded="true">
              <span className="current-region">{this.state.region}</span>
              <span className="caret"></span>
          </button>
          <ul className="dropdown-menu" role="menu"
              arial-labelledby="region-menu">
            {options}
          </ul>
        </div>

        <div className="input-container">
          <div className="input-group">
            <input type="text" className="form-control"
                placeholder="Summoner name... eg Minicat"
                ref="summonerNameInput"
                defaultValue={this.props.value}
                onKeyPress={(e) => this.onKeyPress.apply(this, [e])}/>

            <span className="input-group-btn">
              <button className="btn btn-default" type="button"
                  onClick={(e) => this.doSearch.apply(this, [e])}>
                <span className="glyphicon glyphicon-search"
                    aria-label="search"></span>
              </button>
            </span>
          </div>
        </div>
      </div>
    )
  }

  selectRegion(region) {
    this.setState({ region : region });
  }

  doSearch() {
    let searchTerm = React.findDOMNode(this.refs.summonerNameInput).value;
    if (searchTerm) {
      this.context.router.transitionTo('/s', undefined, {
        'summoner_name' : searchTerm,
        'metric' : 'games',
        'region' : this.state.region
      });
    }
  }

  onKeyPress(e) {
    if (e.key === 'Enter') {
      this.doSearch();
    }
  }
};

SearchComponent.propTypes = {
  value : React.PropTypes.string
};
SearchComponent.defaultProps = {
  region : 'oce'
};

SearchComponent.contextTypes = {
  router : React.PropTypes.func
};
