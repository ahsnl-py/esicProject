event.preventDefault()
const newVal = textAreaRef.current.value
let tempNewForum = [...newForum]
// change this to a server side call
createForum(newVal, (response, status)=>{
  if (status === 201){
    tempNewForum.unshift(response)
  } else {
    console.log(response)
    alert("An error occured please try again")
  }
})