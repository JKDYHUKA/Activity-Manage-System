const messageList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');
const buttonSend = document.querySelector('.btn-chat');

buttonSend.addEventListener('mouseover', function () {
    if (messageInput.value.trim() !== '') {
    buttonSend.classList.add('active');
  } else {
    buttonSend.classList.remove('active');
  }
})

buttonSend.addEventListener('mouseout', function () {
    buttonSend.classList.remove('active');
})

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (message.length == 0){
        return;
    }

    const messageItem = document.createElement('li');
    messageItem.classList.add('message', 'sent');
    messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
              <b>You</b>
            </div>
            <div class="message-content">
              ${message}
            </div>
          </div>`;
    messageList.appendChild(messageItem);

    messageInput.value = '';

    fetch('',{
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: new URLSearchParams({
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'message': message
        })
    })
        .then(response => response.json())
        .then(data => {
            const response = data.response;
            const final_response = response.replace(/\n/g, '<br>');
            const messageItem = document.createElement('li');
            messageItem.classList.add('message', 'received');
            messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
              <b>AI ChatBot</b>
            </div>
            <div class="message-content">
              ${final_response}
            </div>
          </div>`;
            messageList.appendChild(messageItem);


        })
})


