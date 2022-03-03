import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import LeaderBoard from "./LeaderBoard";
import ShopPage from "./ShopPage";

export default class App extends Component { //App is the default export from this file
  constructor(props) {
    super(props);
  }

  render() {
    return(
    <div>
        <HomePage />
    </div>
    ); 
  }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);