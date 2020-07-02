import React, {useEffect, useState} from 'react'; 

import {apiForumList} from './lookup'
import {Forum} from './detail'

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