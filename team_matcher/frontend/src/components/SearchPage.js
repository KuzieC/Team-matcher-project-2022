import React, {Component} from "react";
import {Button, Grid, Typography, TextField, FormControl, FormHelperText, Radio, RadioGroup, FormControlLabel } from '@material-ui/core';
import {Link} from "react-router-dom";
import Select from 'react-select';

export default class SearchPage extends Component{
    constructor(props){
        super(props);
    }
    

    render() {
        return <Grid container spacing = {1}>
            <Grid item xs={12} align="center">
                <FormControl component= 'fieldset'>
                     <p>search page</p>
                </FormControl>
            </Grid>
        </Grid>
    }
}