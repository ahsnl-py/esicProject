export function loadForum(callback) {
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