import React, { Component } from "react";
import classnames from "classnames";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import Table from "react-bootstrap/Table";
import { predictClassification } from "./api";
import styles from "./App.module.scss";

class App extends Component {
  state = {
    comment: "you are disgrace",
    hasSubmitted: false,
    result: null,
    error: null
  };

  handleSubmit = e => {
    e.preventDefault();
    predictClassification(this.state.comment)
      .then(result => {
        console.log(result);
        return this.setState({
          result,
          hasSubmitted: true
        });
      })
      .catch(error => {
        console.log(error);
        return this.setState({
          error
        });
      });
  };

  handleCommentChange = e => {
    this.setState({ comment: e.target.value });
  };

  render() {
    const { comment, result, hasSubmitted } = this.state;
    return (
      <div
        className={classnames(styles.App, {
          [styles.positive]: hasSubmitted && result && !result.toxic,
          [styles.negative]: hasSubmitted && result && result.toxic
        })}
      >
        <div className={styles.wrapper}>
          <div className={styles.form}>
            <Form onSubmit={this.handleSubmit}>
              <Form.Group controlId="comment">
                <Form.Label>Comment message</Form.Label>
                <Form.Control
                  value={comment}
                  placeholder="Enter a comment message"
                  onChange={this.handleCommentChange}
                />
              </Form.Group>
              <Button variant="primary" type="submit">
                Estimate
              </Button>
            </Form>
          </div>
          {result && (
            <div className={styles["table-wrapper"]}>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Toxic</th>
                    <th>Hate</th>
                    <th>Threat</th>
                    <th>Insult</th>
                    <th>Obscene</th>
                    <th>Severe toxic</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{result.toxic ? "Yes" : "No"}</td>
                    <td>{result.identity_hate ? "Yes" : "No"}</td>
                    <td>{result.threat ? "Yes" : "No"}</td>
                    <td>{result.insult ? "Yes" : "No"}</td>
                    <td>{result.obscene ? "Yes" : "No"}</td>
                    <td>{result.severe_toxic ? "Yes" : "No"}</td>
                  </tr>
                </tbody>
              </Table>
            </div>
          )}
        </div>
      </div>
    );
  }
}

export default App;
