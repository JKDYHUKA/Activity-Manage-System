<template>
    <div class="card-body messages-box">
        <ul class="list-unstyled messages-list">
            <li v-for="messageItem in messages" :key="messageItem.id" 
            :class="{'message': 'true', 'sent': messageItem.sender === 'You', 'received': messageItem.sender === 'GPT-3.5-turbo'}">
                <div class="message-text">
                    <div class="message-sender">
                        <b>{{ messageItem.sender }}</b>
                    </div>
                    <div class="message-content">
                        <pre>{{ messageItem.content }}</pre>
                    </div>
                </div>
            </li>
        </ul>
        <div class="form-area">
            <form class="message-form" v-on:submit.prevent="sendMessage">
            <!-- {% csrf_token %} -->
                <div class="input-group">
                    <!-- <input 
                    type="text" 
                    class="message-input" 
                    placeholder="Type your message..."
                    v-model="messageInput"> -->
                    <textarea class="message-input" placeholder="Type your message..." v-model="messageInput"></textarea>
                    <div class="input-group-append">
                        <button 
                        type="submit" 
                        class="btn btn-primary btn-chat"
                        v-bind:class="{ active:isMessageNotEmpty }">Send</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <br><br>
    <br><br>
    <br><br>
</template>

<script>
import { defineComponent, ref, computed, onMounted} from 'vue'
import Cookies from 'js-cookie'

export default defineComponent({
    setup() {
        // const messageForm = document.querySelector('.message-form');
        // const messageList = document.querySelector('.message-list');
        var messageInput = ref('');
        const isMessageNotEmpty = computed(() => messageInput.value.trim() !== '')
        var messages = ref([
            {
                id: 1, 
                sender: 'GPT-3.5-turbo', 
                content: "Here is Jian Yang Huang's GPT proxy website, you can treat this website like chat.openai.com",
            }
        ])

        function sendMessage() {
            const message = messageInput.value.trim();
            if (message.length === 0) {return;}
            
            const newMessage = {
                id: messages.value.length + 1,
                sender: 'You',
                content: message,
            }

            messages.value.push(newMessage);

            messageInput.value = '';

            const csrftoken = Cookies.get('csrftoken');
            console.log(csrftoken);

            const headers = new Headers();
            headers.append('Content-Type', 'application/json');
            headers.append('X-CSRFToken', csrftoken);

            const requestData = JSON.stringify({ message })
            console.log(requestData)

            fetch('http://127.0.0.1:8000/api/get_message', {
                method: 'POST',
                headers: headers,
                body: requestData, 
            })
            .then(response => response.json())
            .then(data => {
                const response = data.response;
                console.log(data)
                console.log(response)
                const final_response = response.replace(/\n/g, '<br>');
                const newResponseMessage = {
                    id: messages.value.length + 1,
                    sender: 'GPT-3.5-turbo',
                    content: final_response,
                };

                messages.value.push(newResponseMessage);
            });

            if(isMessageNotEmpty.value){
                console.log('success');
                messageInput.value = '';
            }
        }

        function getHistoryMessages() {
            const csrftoken = Cookies.get('csrftoken');
            const headers = new Headers();
            headers.append('Content-Type', 'application/json');
            headers.append('X-CSRFToken', csrftoken);

            fetch('http://127.0.0.1:8000/api/getHistoryMessage', {
                method: 'GET',
                headers: headers
            })
            .then(response => response.json())
            .then(data => {
                
                data.message.forEach(element => {
                    let senderValue;

                    if (element.role === 'assistant'){
                        senderValue = 'GPT-3.5-turbo'
                    }
                    else{
                        senderValue = 'user'
                    }

                    const historyMessage = {
                        id: messages.value.length + 1,
                        sender: senderValue,

                        content: element.content,
                    }
                    messages.value.push(historyMessage)
                });
            })
        }

        onMounted(() => {
            // Call the getHistoryMessage function when the component is mounted
            getHistoryMessages();
        });
        
        return {
            messageInput,
            isMessageNotEmpty,
            messages,
            sendMessage,
            getHistoryMessages,
        }

        
    },
//     created(){
//        this.getMsgList();
//     },
//     methods:{
//         getMsgList(){
//              console.log("huoqu")
// }
//     }
})


</script>


<style scoped src="../styles/chatbot.css">

</style>