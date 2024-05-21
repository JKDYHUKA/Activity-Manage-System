<template>
    <div class="history-message-list">
        <div class="button-container" :style="{backgroundColor: parentBackGroundColor} "
        @mouseover="changeBackGroundColor"
        @mouseout="resetBackGroundColor"
        @click="deleteData">
            <button type="submit" class="new_chat" :style="{ backgroundColor: parentBackGroundColor}">New Chat</button>
        </div>
    </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api';
import Cookies from 'js-cookie';

export default defineComponent({
  setup() {
    return {
      parentBackGroundColor: 'black',
      hoverBackGroundColor: 'rgb(30, 32, 35)',
      
    };
  },
  props: {
    model_type: String,
  },
  methods: {
    changeBackGroundColor() {
      this.parentBackGroundColor = this.hoverBackGroundColor;
    },
    resetBackGroundColor() {
      this.parentBackGroundColor = '#000000';
    },
    async deleteData() {
      try {
        const csrftoken = Cookies.get('csrftoken');
        console.log(csrftoken);

        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFToken', csrftoken);

        fetch('http://127.0.0.1:8000/api/deleteMessagesByType', {
          method: 'POST',
          headers: headers,
          body: JSON.stringify({
            model_type: this.model_type,
          }),
        });

        window.location.reload();
      } catch (error) {
        console.error('Error deleting data:', error);
      }
    },
  },
});

</script>

<style src="../styles/head.css">

</style>
