const messagesBox = document.querySelector('.messages-box');
const historyMessageList = document.querySelector('.history-message-list');

const listWidth = historyMessageList.offsetWidth;
messagesBox.style.marginLeft = listWidth + 'px';
