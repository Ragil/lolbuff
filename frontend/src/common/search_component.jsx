import React from "react";

export default class SearchComponent extends React.Component {
  render() {
    return (
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
    )
  }

  doSearch() {
    let searchTerm = React.findDOMNode(this.refs.summonerNameInput).value;
    if (searchTerm) {
      this.context.router.transitionTo('/s', undefined, {'q' : searchTerm});
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

SearchComponent.contextTypes = {
  router : React.PropTypes.func
};
