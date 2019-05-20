import React from 'react';
import PropTypes from 'prop-types';
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup'
import ToggleButton from 'react-bootstrap/ToggleButton'
import { Navbar } from 'react-bootstrap'
import { Nav } from 'react-bootstrap'
import { Tab } from 'react-bootstrap'
import { Tabs } from 'react-bootstrap'



class Index extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      correct_answer: "",
      options: [{"Name": ""}, {"Name": ""}, {"Name": ""}, {"Name": ""}],
      url: "",
      value: null,
      key: "Kanto",
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.handleRegionChange = this.handleRegionChange.bind(this);
  }

  componentDidMount() {
    let answer = Math.floor(Math.random() * 4)
    console.log(answer);
    let url = this.props.url + "?region=" + this.state.key
    fetch(url, { credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.setState({
            correct_answer: data[answer],
            options: data,
            url: data[answer].silhouette,
          });
        })
        .catch(error => console.log(error)); // eslint-disable-line no-console
    

  }

  handleChange(value, event) {
    console.log(value);
    var name = this.state.correct_answer.Name;
    let color = this.state.correct_answer.color_url;
    value.forEach((item) => {
      if (item == name) {
        this.setState({url: color});
      }
    });

    this.setState({ value: value, });
  }

  handleNext() {
    this.componentDidMount()
  }

  handleRegionChange(key) {
    console.log(key);
    this.setState({ key }, function() {
      this.componentDidMount();
    });

  }


  render() {
    var divStyle = {
      height: '450px',
      margin: '75px 0px 0px 50px'
    };
    console.log(this.state.options);
    return (
      <div>
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand href="#">Who's That Pokemon</Navbar.Brand>
          <Tabs
        id="controlled-tab-example"
        activeKey={this.state.key}
        onSelect={this.handleRegionChange}
      >
        <Tab eventKey="Kanto" title="Kanto">
        </Tab>
        <Tab eventKey="Johto" title="Johto">
        </Tab>
        <Tab eventKey="Hoenn" title="Hoenn">
        </Tab>
      </Tabs>
        </Navbar>
        <img src={this.state.url} style={divStyle}/>

        <ToggleButtonGroup
        type="checkbox"
        value={this.state.value}
        onChange={this.handleChange}
      >
        <ToggleButton value={this.state.options[0].Name}>{this.state.options[0].Name}</ToggleButton>
        <ToggleButton value={this.state.options[1].Name}>{this.state.options[1].Name}</ToggleButton>
        <ToggleButton value={this.state.options[2].Name}>{this.state.options[2].Name}</ToggleButton>
        <ToggleButton value={this.state.options[3].Name}>{this.state.options[3].Name}</ToggleButton>
        <button className="next" onClick={this.handleNext}>Next</button>
      </ToggleButtonGroup>
      </div>
    );
  }
}

export default Index;
