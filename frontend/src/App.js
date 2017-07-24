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
