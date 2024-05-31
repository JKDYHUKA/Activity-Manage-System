export function set_post_header() {
    const csrfToken = localStorage.getItem('csrfToken')
    const jwtToken = localStorage.getItem('jwtToken')
    console.log("csrfToken: ", csrfToken)
  
    // 构建请求头
    const headers = {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken, // 使用X-CSRFToken来指定CSRF Token
      'Authorization': 'Bearer ' + jwtToken,
    };
  
    return headers;
  }


export function set_no_csrf_header(){
    const jwtToken = localStorage.getItem('jwtToken')
  
    // 构建请求头
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + jwtToken,
    };
  
    return headers;
}


export function isTokenExpired(){
    const expirationTimestamp = localStorage.getItem('tokenExpiration');
    if (!expirationTimestamp) {
        // 如果没有保存过期时间戳，则认为令牌已过期
        return true;
    }
    const currentTimestamp = Math.floor(Date.now() / 1000);
    return currentTimestamp >= expirationTimestamp;
}