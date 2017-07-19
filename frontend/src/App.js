import React, {
  Component
}
from 'react';
import { FormGroup, ControlLabel, FormControl, HelpBlock, Button } from 'react-bootstrap/lib/';
import './App.css';

class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.state = { value: '' };
  }

  componentDidMount() {
      };
  
  handleChange(event) {
    this.setState({value: event.target.value});
  }
  
  handleSubmit(event) {
    console.log(this.state.value);
    var teams = [
      ["Chicago Blackhawks", "hawks", "blackhawks", "chicago"],
      ["Carolina Hurricanes", "carolina", "hurricanes", "canes"],
      ];
    var words = this.state.value.split(" ");
    for (var i = 0; i < words.length; i++) {
      var word = words[i];
      for (var j = 0; j < teams.length; j++) {
        var team = teams[j];
        for (var k = 0; k < team.length; k++) {
          if (word.toLowerCase() === team[k].toLowerCase()) {
            console.log("Found: " + team[0])
          }
        }
      }
    }
    event.preventDefault();
  }

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <FieldGroup
      id="formControlsText"
      type="text"
      label="Text"
      placeholder="Enter text"
      value={this.state.value} onChange={this.handleChange} 
    />
    <Button type="submit">
      Submit
    </Button>
        </form>
      </div>
    );
  }
}

function FieldGroup({
  id,
  label,
  help,
  ...props
}) {
  return (
    <FormGroup controlId={id}>
      <ControlLabel>{label}</ControlLabel>
      <FormControl {...props} />
      {help && <HelpBlock>{help}</HelpBlock>}
    </FormGroup>
  );
}

export default App;
