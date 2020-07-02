import React from 'react'; 

import {apiForumAction} from './lookup'

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