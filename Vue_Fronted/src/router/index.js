import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login_register.vue'
import Index from '../views/index.vue'
import Personal from '../views/Personal.vue'

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
  {
    path: '/detail',
    name: 'detail',
    component: Personal,
    // children: [
    //   {
    //     path: '/',
    //     component: r => require.ensure([], () => r(require('@/views/Index')), 'index')
    //   },
    //   {
    //     path: '/newsuser/personal/:id',
    //     component: r => require.ensure([], () => r(require('@/views/person/Personal')), 'personal'),
    //     meta: {
    //       requireLogin: true
    //     },
    //     children: [
    //       {
    //         // path: '/personal/info/:id',
    //         path: '/newsuser/personal/info/:id',
    //         name:'info',
    //         component: r => require.ensure([], () => r(require('@/views/person/Info')), 'info')
    //       },
    //       {
    //         path:'/newsuser/personal/myarticle/:id',
    //         name:'myarticle',
    //         component: r => require.ensure([], () => r(require('@/views/person/MyArticle')), 'myarticle')
    //       },
    //       {
    //         path:'/newsuser/personal/mycollect/:id',
    //         name:'mycollect',
    //         component: r => require.ensure([], () => r(require('@/views/person/MyCollect')), 'mycollect')
    //       },
    //       {
    //         path:'/newsuser/personal/myfan/:id',
    //         name:'myfan',
    //         component: r => require.ensure([], () => r(require('@/views/person/MyFanAndFollow')), 'myfan')
    //       },
    //       {
    //         path:'/newsuser/personal/myfollow/:id',
    //         name:'myfollow',
    //         component: r => require.ensure([], () => r(require('@/views/person/MyFanAndFollow')), 'myfollow')
    //       }
    //     ]
    //   }
    // ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
