import React, {useEffect ,useState} from 'react'; 

import {ForumList} from './list'
import {ForumCreate} from './create'

import {Forum} from './detail'
import {apiForumDetail} from './lookup'

//parent components
export function ForumComponent(props) {
  const [newForum, setNewForum] = useState([])
  const canPost = props.canPost === "false" ? false : true
  const handleNewForum = (newForum) =>{
    let tempNewForum = [...newForum]
    tempNewForum.unshift(tempNewForum)
    setNewForum(tempNewForum)
  }
  return <div className={props.className}>
          {canPost === true && <ForumCreate didPost={handleNewForum} className='col-12 mb-3'/>}
          <ForumList newForum={newForum} {...props}/>
        </div>
}


export function ForumDetailComponent(props){
  const {forumId} = props
  const [didLookup, setDidLookup] = useState(false) 
  const [forum, setForum] = useState(null)

  const handleBackendLookup = (response, status) => {
    if (status === 200) {
      setForum(response)
    } else {
      alert("There was an error finding your forum.")
    }
  }
  useEffect(()=>{
    if (didLookup === false){

      apiForumDetail(forumId, handleBackendLookup)
      setDidLookup(true)
    }
  }, [forumId, didLookup, setDidLookup])
  return forum === null ? null : 
  <Forum forum={forum} className={props.className} />
}









  