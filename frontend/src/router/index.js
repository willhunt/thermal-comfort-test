import Vue from 'vue'
import VueRouter from 'vue-router'

// Lazy loading
const Home = () => import('@/views/Home.vue')
const Profile = () => import('@/views/Profile.vue')
const Login = () => import('@/views/Login.vue')
const Register = () => import('@/views/Register.vue')
const Manage = () => import('@/views/Manage.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {title: 'Home' }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: { title: 'Profile' }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { title: 'Register' }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { title: 'Login' }
  },
  {
    path: '/manage',
    name: 'Manage',
    component: Manage,
    meta: { title: 'Manage Test' }
  }
]

const router = new VueRouter({
  routes
})

export default router
