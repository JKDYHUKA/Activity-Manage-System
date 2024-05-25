import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login_register.vue'
import Index from '../views/index.vue'
const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/index',
    name: 'index',
    component: Index
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
