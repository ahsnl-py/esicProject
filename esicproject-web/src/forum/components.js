import React, {useState} from 'react'; 

import {ForumList} from './list'
import {ForumCreate} from './create'

//parent components
export function ForumComponent(props) {
  const [newForum, setNewForum] = useState([])
  const canPost = props.canPost === "false" ? false : true
  const handleNewForum = (newForum) =>{
    let tempNewForum = [...newForum]
    if (status === 201) {
      tempNewForum.unshift(response)
      setNewForum(tempNewForum)
    } else {
      alert("There was an error, please try again")
    }
  }
  const handleSubmit = (event) => {
    event.preventDefault()
    const newVal = textAreaRef.current.value
    // backend api request
    apiForumCreate(newVal, handleBackendUpdate)
    textAreaRef.current.value = ''
  }
  return <div className={props.className}>
          {canPost === true && <ForumCreate didPost={handleNewForum} className='col-12 mb-3'/>}
          <ForumList newForum={newForum} {...props}/>
        </div>
}













  