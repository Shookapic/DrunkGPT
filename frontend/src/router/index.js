import { createRouter, createWebHistory } from 'vue-router'
import ChatBot from '../views/ChatInterfaceView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/chat',
      name: 'ChatBot',
      component: ChatBot,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/login'
    }
  ]
})

async function checkAuth(to, from, next) {
  try {
    let username = localStorage.getItem('username');

    const response = await fetch('http://10.106.1.161:5001/is_logged_in', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username })
    });

    if (!response.ok) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      });
      return;
    }

    const data = await response.json();

    if (data.state) {
      next();
    } else {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      });
    }
  } catch (error) {
    console.error('Error checking user authentication:', error);
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    });
  }
}

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    await checkAuth(to, from, next);
  } else {
    next();
  }
});

export default router
