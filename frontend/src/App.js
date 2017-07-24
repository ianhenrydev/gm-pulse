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
    this.state = { classification: [], value: "" };
  }

  componentDidMount() {
      };
  
  handleChange(event) {
    this.setState({value: event.target.value});
  }
  
  handleSubmit(event) {
    event.preventDefault();
        return fetch('https://gm-pulse-supraman.c9users.io:8081/classify/'+ this.state.value)
      .then((response) => response.json())
      .then((responseJson) => {
        console.log(responseJson);
        this.setState({
          classification: responseJson,
        });
      })
      .catch((error) => {
        console.error(error);
      });
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
    <p>Text: {this.state.classification[0]}</p>
    <p>Class: {this.state.classification[1]}</p>
    <p>Positive Confidence: {this.state.classification[2]}</p>
    <p>Negative Confidence: {this.state.classification[3]}</p>
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
