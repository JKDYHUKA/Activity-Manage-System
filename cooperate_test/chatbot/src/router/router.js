import { createRouter, createWebHistory} from 'vue-router'
import LogInPage from '../components/LogInPage.vue'
import ChatBotBody from '../views/ChatBotBody'
import RegisterPage from '../components/RegisterPage'
import TravelChatBody from '../views/TravelChatBody'


const routes = [
    {
        path: '/',
        redirect: '/home' 
    },
    {
        path: '/home',
        name: 'home',
        component: ChatBotBody,
    },
    {
        path: '/login',
        name: 'LogInPage', 
        component: LogInPage,
    },
    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage,
    },
    {
        path: '/travelChat',
        name: 'TravelPage',
        component: TravelChatBody,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;