import React, {useEffect, useState}  from'react';
import logo from './logo.svg';
import './App.css';

function Forum(props) {
  const {forum} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return <div className={className}>
      <p>{forum.id} - {forum.content}</p>
  </div>
}

function loadForum(callback) {
  const xhr = new XMLHttpRequest() //
  const method = 'GET'
  const url = 'http://localhost:8000/api/forums/' // localhost:/index
  const responseType = "json"
  xhr.responseType = responseType
  xhr.open(method, url)
  xhr.onload = function() {
    callback(xhr.response, xhr.status)
  }  
  xhr.onerror = function (e) {
    console.log(e)
    callback({"message": "There was an error"}, 400)
  }
  xhr.send()
}

function App() {
  const [forums, setForum] = useState([])
 
  useEffect(() => {
    const myCallback = (response, status) => {
      console.log(response, status)
      if (status === 200){
        setForum(response)
      } else {
        alert("There was an error")
      }
    }
    loadForum(myCallback)
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {forums.map((item, index)=>{
            return <Forum forum={item} />
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
