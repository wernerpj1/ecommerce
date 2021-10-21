import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import store from '../store'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Contato from '../views/Contato.vue'
import Cart from '../views/Cart.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import MyAccount from '../views/MyAccount.vue'
import BrandsView from '../views/BrandsView.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout, 
    meta: {
      requireLogin: true
  }
  },
  {
    path: '/cart/Success',
    name: 'Success',
    component: Success
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
        requireLogin: true
    }
  },
  
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  {
    path: '/contato',
    name: 'Contato',
    component: Contato
  },
  {
    path: '/marca/:brands_slug',
    name: 'BrandsView',
    component: BrandsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path }});
    } else {
      next()
    }
})

export default router
