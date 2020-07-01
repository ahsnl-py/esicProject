import React, {useEffect, useState} from 'react'; 

import {loadForum, createForum} from '../lookup'

//parent components
export function ForumComponent(props) {
  const textAreaRef = React.createRef()
  const [newForum, setNewForum] = useState([])

  const handleBackendUpdate = (response, status) => {
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
    createForum(newVal, handleBackendUpdate)
    textAreaRef.current.value = ''
  }
  return <div className={props.className}>
    <div className='col-12 mb-3'>
      <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} required={true} className='form-control' name='forum'>

        </textarea>
        <button type='submit' className='btn btn-primary my-3'>Share</button>
      </form>
      </div>
    <ForumList newForum={newForum} />
  </div>
}

// child components 
export function ForumList(props) {
  const [forumInit, setForumInit] = useState([])
  const [forum, setForum] = useState([])
  const [forumDidSet, setForumDidSet] = useState(false)
  useEffect(()=>{
    const final = [...props.newForum].concat(forumInit)
    if (final.length !== forum.length) {
      setForum(final)
    }
  }, [props.newForum, forum, forumInit])

  useEffect(() => {
    if (forumDidSet === false){
      const myCallback = (response, status) => {
        if (status === 200){
          setForumInit(response)
          setForumDidSet(true)
        } else {
          alert("There was an error")
        }
      }
      loadForum(myCallback)
    }
  }, [forumInit, forumDidSet, setForumDidSet])
  return forum.map((item, index)=>{
    return <Forum forum={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />
  })
}

export function ActionBtn(props) {
    const {forum, action} = props
    const [likes, setLikes] = useState(forum.likes ? forum.likes : 0)
    const [userLike, setUserLike] = useState(forum.userLike ? true : false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const handleClick = (event) => {
      event.preventDefault()
      if (action.type === 'like') {
        if (userLike === true) {
          setLikes(likes - 1)
          setUserLike(false)
        } else {
          setLikes(likes + 1)
          setUserLike(true)
        }
      }
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return  <button className={className} onClick={handleClick}>{display}</button> 
}
  
export function Forum(props) {
    const {forum} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{forum.id} - {forum.content}</p>
        <div className='btn btn-group'>
          <ActionBtn forum={forum} action={{type: "like", display: 'likes'}}/>
          <ActionBtn forum={forum} action={{type: "repost", display: ''}}/>
        </div>
    </div>
  }






  