import React, {useEffect, useState} from 'react'; 

import {
  apiForumAction,
  apiForumCreate,
  apiForumList} from './lookup'

//parent components
export function ForumComponent(props) {
  const textAreaRef = React.createRef()
  const [newForum, setNewForum] = useState([])

  const canPost = props.canPost === "false" ? false : true
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
    apiForumCreate(newVal, handleBackendUpdate)
    textAreaRef.current.value = ''
  }
  return <div className={props.className}>
          {canPost === true && <div className='col-12 mb-3'>
            <form onSubmit={handleSubmit}>
              <textarea ref={textAreaRef} required={true} className='form-control' name='forum'>

              </textarea>
              <button type='submit' className='btn btn-primary my-3'>Share</button>
            </form>
            </div>
}
    <ForumList newForum={newForum} {...props}/>
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
      const handleForumListLookup = (response, status) => {
        if (status === 200){
          setForumInit(response)
          setForumDidSet(true)
        } else {
          alert("There was an error")
        }
      }
      apiForumList(props.username, handleForumListLookup)
    }
  }, [forumInit, forumDidSet, setForumDidSet, props.username])


  const handleDidRepost = (newForum) => {
    const updateForumInit = [...forumInit]
    updateForumInit.unshift(newForum)
    setForumInit(updateForumInit)
    const updateFinalForum = [...forum]
    updateFinalForum.unshift(forum)
    setForum(updateFinalForum)
  }

  return forum.map((item, index)=>{
    return <Forum 
    forum={item} 
    didRepost = {handleDidRepost}
    className='my-5 py-5 border bg-white text-dark' 
    key={`${index}-{item.id}`} />
    
  })
}

export function ActionBtn(props) {
    const {forum, action, didPerformAction} = props
    const likes = forum.likes ? forum.likes : 0
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    
    const handleActionBackendEvent = (response, status) => {
      console.log(response, status)
      if ((status === 200 || status === 201) && didPerformAction ) {
        didPerformAction(response, status)
      } 
    }

    const handleClick = (event) => {
      event.preventDefault()
      apiForumAction(forum.id, action.type, handleActionBackendEvent)
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return  <button className={className} onClick={handleClick}>{display}</button> 
}

export function ParentForum(props){
  const {forum} = props
  return forum.parent ? <div className='row'>
  <div className='col-11 mx-auto p-3 border rounded'>
    <p className='mb-0 text-muted small'>Repost</p>
    <Forum hideAction className={' '} forum={forum.parent} />
  </div>
  </div> : null
}

// make some change here .. continue from series 70
export function Forum(props) {
    const {forum, didRepost} = props
    const [actionForum, setActionForum, hideAction] = useState(props.forum ? props.forum : null)
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    
    const handlePerformAction = (newActionForum, status ) => {
      if (status === 2000) {
        setActionForum(newActionForum)
      } else if (status === 201 ) {
        if (didRepost) {
          didRepost(newActionForum)
        }
        //let the list know
      }

      //set action forum
    }

//continue here...
    return <div className={className}>
            <div>
              <p>{forum.id} - {forum.content}</p>
              <ParentForum forum={forum} />
            </div>
        {(actionForum && hideAction !== true ) && <div className='btn btn-group'>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "like", display:"Likes"}}/>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "unlike", display:"Unlike"}}/>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "repost", display:"Repost"}}/>
        </div>
}
    </div>
    }






  