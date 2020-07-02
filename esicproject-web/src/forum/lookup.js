import {backendLookup} from '../lookup'

export function apiForumCreate(newForum, callback){
    backendLookup("POST", "/forums/create/", callback, {content: newForum})
}

export function apiForumAction(ForumId, action, callback) {
    const data = {id: ForumId, action: action}
    backendLookup("POST", "/forums/action/", callback, data)
}
 
export function apiForumDetail(forumId, callback) {
    backendLookup("GET", `/forums/${forumId}/`, callback)
}

export function apiForumList(username, callback) {
    let endpoint = "/forums/"
    if (username) {
        endpoint = `/forums/?username=${username}`
    }
    backendLookup("GET", endpoint, callback)
}