<template>
    <div class="main-container">
        <HistoryList :model_type="modelType"></HistoryList>
        <TravelChat></TravelChat>
    </div>
</template>

<script>
import HistoryList from '../components/HistoryList.vue'
import TravelChat from '../components/TravelChat.vue'
export default {
    name: 'TravelChatBody',
    components: {
        HistoryList,
        TravelChat,
    },
    data(){
        return{
            modelType: 'travel_chatbot',
        }
    },
    setup() {
        
    },
}
</script>

<style src="../styles/head.css">

</style>