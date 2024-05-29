import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login_register.vue'
import Index from '../views/index.vue'
import Creation from '../views/creation_top.vue'
import Detail from '../views/Detail.vue'
import info from '../components/info.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/creation',
    name: 'creation',
    component: Creation
  },
  {
    path: '/detail',
    name: 'detail',
    component: Detail,
    children: [
      {
        path: '/detail/info/:id',
        name: 'info',
        component: info
      }
    ]
  }
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
