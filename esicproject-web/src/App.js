import React, {useEffect, useState}  from'react';
import logo from './logo.svg';
import './App.css';

function loadForum(callback) {
  const xhr = new XMLHttpRequest()
  const method = 'GET' // "POST"
  const url = "http://localhost:8000/home/api/forum/"
  const responseType = "json"
  xhr.responseType = responseType
  xhr.open(method, url)
  xhr.onload = function() {
    callback(xhr.response, xhr.status)
  }
  xhr.onerror = function (e) {
    console.log(e)
    callback({"message": "The request was an  error"}, 400)
  }
  xhr.send()
}

function App() {
  const [forums, setForums] = useState([])
  //get data from backend 
  useEffect(() => {
    const myCallBack = (response, status) => {
      console.log(response, status)
      if (status == 200) {
        setForums(response)
      } else {
        alert('There was an error')
      }
    }
    loadForum(myCallBack)
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {forums.map((forum, index)=>{
            return <li>{forum.content}</li>
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
