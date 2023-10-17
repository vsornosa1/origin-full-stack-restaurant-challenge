import { createRouter, createWebHashHistory } from 'vue-router'

const Menu   = () => import('@/components/Menu.vue')
const Orders = () => import('@/components/Orders.vue')
const Login  = () => import('@/components/auth/Login.vue') 
const Register  = () => import('@/components/auth/Register.vue') 

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: '/', component: Login },
  { path: '/register', component: Register },
  { path: '/menu', component: Menu },
  { path: '/orders', component: Orders },
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

export default router;
