import Vue from "vue";
import VueRouter from "vue-router";
import store from '../../store/store.js'
import PrintPage from "@/components/PrintPage"
import LoginPage from "@/components/LoginPage"

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginPage
  },
  {
    path: "/",
    name: "print",
    component: PrintPage,
    meta: {
      requiresAuth: true
    }
  }
];

const router = new VueRouter({
  mode: "hash",
  routes: routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})

export default router;