import React, {Component} from "react";
import LeaderBoard from "./LeaderBoard";
import ShopPage from "./ShopPage";
import WelcomePage from "./WelcomePage";
import SearchPage from "./SearchPage";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path="/" element={<WelcomePage />}></Route>
                    <Route path="/shop" element={<ShopPage />}></Route>
                    <Route path="/leaderboard" element={<LeaderBoard />}></Route>
                    <Route path="/search" element={<SearchPage />}></Route>
                </Routes>
            </Router>
          );
    }
}