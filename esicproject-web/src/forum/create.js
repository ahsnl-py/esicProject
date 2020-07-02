
import React from 'react'
import {apiForumCreate} from './lookup'

export function ForumCreate(props) {
    const textAreaRef = React.createRef()
    const {didPost} = props
    const handleBackendUpdate = (response, status) => {
      if (status === 201) {
        didPost(response)
      } else {
        console.log(response)
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
        <form onSubmit={handleSubmit}>
            <textarea ref={textAreaRef} required={true} className='form-control' name='forum'>
            </textarea>
            <button type='submit' className='btn btn-primary my-3'>Share</button>
        </form>
    </div>
  }