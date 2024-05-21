    const generaliseButton = document.querySelector('.generalise-button');

    // 添加点击事件处理函数
    generaliseButton.addEventListener('click', function() {
        // 在这里添加跳转的页面URL
        const nextPageUrl = '/travel_chatbot/generalise';

        // 进行页面跳转
        window.location.href = nextPageUrl;
    });