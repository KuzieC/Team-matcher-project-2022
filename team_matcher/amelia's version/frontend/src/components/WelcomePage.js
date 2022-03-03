import React, {Component} from "react";
import {Button, Grid, Typography, TextField, FormControl, FormHelperText, Radio, RadioGroup, FormControlLabel } from '@material-ui/core';
import {Link} from "react-router-dom";
import Select from 'react-select';

const sports = [
    {value: 'Football', label: 'Football'},
    {value: 'Tennis', label: 'Tennis'},
    {value: 'Dance', label: 'Dance'},
    {value: 'Running', label: 'Running'}
]

export default class WelcomePage extends Component{
    constructor(props){
        super(props);
        this.state = { //default state
            postcode: "",
            sport: "",
            mode: "",
            result: "",
        };

        //binding methods to class so we can access 'this' keyword
        this.handleTeamButtonPressed = this.handleTeamButtonPressed.bind(this);
        this.handleMemberButtonPressed = this.handleMemberButtonPressed.bind(this);
        this.handleCompetitorButtonPressed = this.handleCompetitorButtonPressed.bind(this);
        this.handleSportSelect = this.handleSportSelect.bind(this);
        this.handlePostcodeEntry = this.handlePostcodeEntry.bind(this);
    }

    handleSportSelect(e){ //will get the object that called this function and get the value for sport
        this.setState({
            sport: e.value,
        })
        fetch("/api/person")
        .then((response) => response.json())
        .then((data) => this.setState({result: data,}));
        console.log(this.state);
    }

    handlePostcodeEntry(e){
        this.setState({
            postcode: e.target.value,
        })
    }

    handleTeamButtonPressed(){
        this.setState({mode: "find-team",}) 
        //console.log(this.state);
        let r = this.state.result;
        let filtered = r.filter(a => a.sport == "Tennis");
        this.setState({result: filtered,})
        console.log(this.state);
    }

    getUsers(){
        fetch("/api/person")
        .then((response) => response.json())
        .then((data) => this.setState({result: data,}));
    }

    handleMemberButtonPressed(){
        this.setState({mode: "find-member",}) 
        console.log(this.state); 
    }

    handleCompetitorButtonPressed(){
        this.setState({mode: "find-competitor",}) 
        console.log(this.state); 
    }

    render() {
        return <Grid container spacing = {1}>
            <Grid item xs={12} align="center">
                <Typography component= 'h1' variant='h1'>
                    Team Matcher
                </Typography>
            </Grid>&nbsp;&nbsp;&nbsp;
            <Grid item xs={12} align="center">
                <FormControl>
                    <Select placeholder= "Select a sport" options={sports} onChange={this.handleSportSelect}>
                    
                    </Select>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField required={true} onChange={this.handlePostcodeEntry}/>
                    <FormHelperText>
                        <div align = 'center'>Postcode</div>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl component= 'fieldset'>
                    <FormHelperText>
                        <div align = 'center'>Click a button to start your search</div>
                    </FormHelperText>
                    <Button color="secondary" variant="contained" to="/search" component={Link} onClick={this.handleTeamButtonPressed}>
                        Find Team</Button> &nbsp;&nbsp;&nbsp;
                    <Button color="secondary" variant="contained" to="/search" component={Link} onClick={this.handleMemberButtonPressed}>
                        Find Team Member</Button> &nbsp;&nbsp;&nbsp;
                    <Button color="secondary" variant="contained" to="/search" component={Link} onClick={this.handleCompetitorButtonPressed}>
                        Find Competitor</Button> &nbsp;&nbsp;&nbsp;

                     <Button color="primary" variant="contained" onClick={this.handleTeamButtonPressed}>
                        Find Competitor Test</Button> &nbsp;&nbsp;&nbsp;
                </FormControl>
            </Grid>
        </Grid>;
    }
}