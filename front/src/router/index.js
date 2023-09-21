import { createRouter, createWebHistory } from 'vue-router'

import BoardView from '../views/BoardView.vue'
import WeekView from '../views/WeekView.vue'
import RoleView from '../views/RoleView.vue'

const routes = [

  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/',
    name:'board',
    component: BoardView
  }
  ,{
    path:'/week',
    name:'/week',
    component: WeekView
  }
  ,{
    path:'/role',
    name:'role',
    component: RoleView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
