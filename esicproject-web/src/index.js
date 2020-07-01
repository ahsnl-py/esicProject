import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {ForumComponent} from './forum'
import * as serviceWorker from './serviceWorker';

const appEl = document.getElementById('root')
if (appEl) {
  ReactDOM.render(<App />, appEl)
}

const forumEl = document.getElementById('forum-el')
if (forumEl) {
  ReactDOM.render(<ForumComponent />, forumEl)
}


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
