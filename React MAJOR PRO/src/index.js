import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router,Route} from 'react-router-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
      <Router>
          <Route path="/" component={App} />
      </Router>, 
      document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();


class BookDashboard extends React.Component {
    
        state = {
            login: []    
      }   
        componentDidMount() {
    
            fetch('http://127.0.0.1:8000/api/login/')
    
                .then(response => response.json())
    
                .then(data => {
    
                    this.setState({login: data});
    
                });
    
        }

    
    }