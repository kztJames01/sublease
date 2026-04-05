import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/Home.vue') },
  { path: '/search', name: 'search', component: () => import('../views/Search.vue') },
  { path: '/faq', name: 'faq', component: () => import('../views/FAQ.vue') },
  { path: '/contact', name: 'contact', component: () => import('../views/Contact.vue') },
  { path: '/login', name: 'login', component: () => import('../views/Login.vue'), meta: { guest: true } },
  { path: '/signup', name: 'signup', component: () => import('../views/Signup.vue'), meta: { guest: true } },
  { path: '/password-reset', name: 'password-reset', component: () => import('../views/PasswordReset.vue'), meta: { guest: true } },
  { path: '/dashboard', name: 'dashboard', component: () => import('../views/Dashboard.vue'), meta: { requiresAuth: true } },
  { path: '/inbox', name: 'inbox', component: () => import('../views/Messaging.vue'), meta: { requiresAuth: true } },
  { path: '/inbox/:id', name: 'conversation', component: () => import('../views/Messaging.vue'), meta: { requiresAuth: true } },
  { path: '/listings/new', name: 'create-listing', component: () => import('../views/CreateListing.vue'), meta: { requiresAuth: true } },
  { path: '/apartment-portal', name: 'apartment-portal', component: () => import('../views/ApartmentPortal.vue'), meta: { requiresAuth: true, requiresApartmentApproval: true } },
  { path: '/listings/:id', name: 'listing-detail', component: () => import('../views/ListingDetail.vue') },
  { path: '/items/new', name: 'create-item', component: () => import('../views/ItemForm.vue'), meta: { requiresAuth: true } },
  { path: '/items/:id', name: 'item-detail', component: () => import('../views/ItemDetail.vue') },
  { path: '/items/:id/edit', name: 'edit-item', component: () => import('../views/ItemForm.vue'), meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

router.beforeEach(async (to) => {
  const authStore = useAuthStore()
  if (authStore.loading) await authStore.fetchUser()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }

  if (to.meta.requiresApartmentApproval) {
    const approved = await authStore.fetchApartmentPortalApproval()
    if (!approved) {
      return { name: 'dashboard' }
    }
  }

  // Redirect authenticated users away from auth pages
  if (to.meta.guest && authStore.isAuthenticated) {
    return { name: 'home' }
  }
})

export default router
