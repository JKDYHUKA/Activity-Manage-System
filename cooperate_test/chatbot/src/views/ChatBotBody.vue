<template>
    <div class="main-container">
        <HistoryList :model_type="modelType"></HistoryList>
        <ChatBody></ChatBody>
    </div>
</template>

<script>
import HistoryList from '../components/HistoryList.vue'
import ChatBody from '../components/ChatBody.vue'
export default {
    name: 'ChatBotBody',
    components: {
        HistoryList,
        ChatBody,
    },
    data(){
        return{
            modelType: 'gpt-3.5-turbo',
        }
    },
    setup() {
        
    },
}
</script>

<style src="../styles/head.css">

</style>
