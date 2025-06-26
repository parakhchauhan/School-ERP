import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import DashboardPage from '../views/DashboardPage.vue'
import RegisterStudentPage from '../views/RegisterStudentPage.vue'
import StudentPage from '../views/StudentPage.vue'
import TeacherPage from '../views/TeacherPage.vue'
import FinancePage from '../views/FinancePage.vue'
import RegisterAdminPage from '../views/RegisterAdminPage.vue'
import ForgetPassword from '../views/ForgetPassword.vue'
import users from '../views/users.vue'

const routes = [
  { path: '/', component: LoginPage }, // Unprotected
  { path: '/dashboard', component: DashboardPage, meta: { requiresAuth: true } },
  { path: '/RegisterStudentPage', component: RegisterStudentPage, meta: { requiresAuth: true } },
  { path: '/students', component: StudentPage, meta: { requiresAuth: true } },
  { path: '/teachers', component: TeacherPage, meta: { requiresAuth: true } },
  { path: '/finance', component: FinancePage, meta: { requiresAuth: true } },
  { path: '/users', component: users, meta: { requiresAuth: true } },
  { path: '/RegisterAdminPage', component: RegisterAdminPage, meta: { requiresAuth: true } },
  { path: '/ForgetPassword', component: ForgetPassword }, // Public route
  { path: '/', component: LoginPage }, // Explicit login path for redirects
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// 🔐 Navigation Guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/')
  } else {
    next()
  }
})

export default router