import {backendLookup} from '../lookup'

export function apiForumCreate(newForum, callback){
    backendLookup("POST", "/forums/create/", callback, {content: newForum})
}

export function apiForumAction(ForumId, action, callback) {
    const data = {id: ForumId, action: action}
    backendLookup("POST", "/forums/action/", callback, data)
}
  
export function apiForumList(callback) {
    backendLookup("GET", "/forums/", callback)
}