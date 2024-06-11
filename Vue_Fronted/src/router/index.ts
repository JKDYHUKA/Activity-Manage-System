import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login_register.vue'
import Creation from '../views/creation_top.vue'
import Detail from '../views/Detail.vue'
import info from '../components/Info.vue'
import activity from '../components/activity/activity.vue'
const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/creation',
    name: 'creation',
    component: Creation
  },
  {
    path: '/',
    name: 'detail',
    component: Detail,
    children: [
      {
        path: '/info/:id',
        name: 'info',
        component: info
      },
      {
        path: '/activity/:id',
        name: 'activity',
        component: activity
      },
      // {
      //   path: '/creation/:id',
      //   name: 'creation',
      //   component: Creation
      // },
    ]
  }
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
