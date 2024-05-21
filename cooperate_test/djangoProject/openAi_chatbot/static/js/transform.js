const travel_page = document.getElementById("b");
const chat_page = document.getElementById("a");

chat_page.addEventListener('click', function () {
    window.location.href='/';
})

travel_page.addEventListener('click', function () {
    window.location.href='/travel_chatbot';
})