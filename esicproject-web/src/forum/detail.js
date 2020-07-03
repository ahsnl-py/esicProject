
import React, {useState}  from 'react'

import {ActionBtn} from './button'

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
    const path = window.location.pathname
    const match = path.match(/(?<forumid>\d+)/)
    const urlForumId = match ? match.groups.forumid : -1

    const isDetail = `${forum.id}` === `${urlForumId}` 
    const handleLink = (event) => {
      event.preventDefault()
      window.location.href = `/${forum.id}`
    }
    const handlePerformAction = (newActionForum, status ) => {
      if (status === 200) {
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
            <div className='btn btn-group'>
        {(actionForum && hideAction !== true ) && <React.Fragment>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "like", display:"Likes"}}/>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "unlike", display:"Unlike"}}/>
          <ActionBtn forum={actionForum} didPerformAction={handlePerformAction} action={{type: "repost", display:"Repost"}}/>
          </React.Fragment>
}  
          {isDetail === true ? null : <button className="btn btn-outline-primary btn-sm" onClick={handleLink}>View</button>}
        </div>
    </div>
  }