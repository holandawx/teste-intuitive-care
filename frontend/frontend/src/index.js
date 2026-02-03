import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Detalhe from '../views/Detalhe.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/operadora/:cnpj', component: Detalhe }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
