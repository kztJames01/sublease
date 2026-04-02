<template>
  <nav class="bg-white shadow-sm sticky top-0 z-50 border-b border-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        <router-link to="/" class="flex items-center gap-2">
          <span class="text-2xl font-display font-bold text-primary-bg">lvSpace</span>
        </router-link>

        <!-- Desktop nav -->
        <div class="hidden md:flex items-center gap-6">
          <router-link to="/search" class="text-text-dark/75 hover:text-primary-bg transition">Search</router-link>
          <router-link to="/faq" class="text-text-dark/75 hover:text-primary-bg transition">FAQ</router-link>
          <router-link to="/contact" class="text-text-dark/75 hover:text-primary-bg transition">Contact</router-link>
          <template v-if="authStore.isAuthenticated">
            <router-link to="/dashboard" class="text-text-dark/75 hover:text-primary-bg transition">Dashboard</router-link>
            <router-link to="/inbox" class="text-text-dark/75 hover:text-primary-bg transition">Inbox</router-link>
            <router-link to="/listings/new" class="bg-primary-bg text-primary-fg px-4 py-2 rounded-lg hover:bg-primary-bg/90 transition">List Property</router-link>
            <button @click="handleLogout" class="text-text-dark/65 hover:text-destructive transition">Logout</button>
          </template>
          <template v-else>
            <router-link to="/login" class="text-text-dark/75 hover:text-primary-bg transition">Login</router-link>
            <router-link to="/signup" class="bg-primary-bg text-primary-fg px-4 py-2 rounded-lg hover:bg-primary-bg/90 transition">Sign Up</router-link>
          </template>
        </div>

        <!-- Mobile toggle -->
        <button @click="mobileOpen = !mobileOpen" class="md:hidden p-2 text-text-dark/75">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile menu -->
    <div v-if="mobileOpen" class="md:hidden border-t border-border bg-white px-4 py-3 space-y-2">
      <router-link to="/search" class="block py-2 text-text-dark/75" @click="mobileOpen = false">Search</router-link>
      <router-link to="/faq" class="block py-2 text-text-dark/75" @click="mobileOpen = false">FAQ</router-link>
      <router-link to="/contact" class="block py-2 text-text-dark/75" @click="mobileOpen = false">Contact</router-link>
      <template v-if="authStore.isAuthenticated">
        <router-link to="/dashboard" class="block py-2 text-text-dark/75" @click="mobileOpen = false">Dashboard</router-link>
        <router-link to="/inbox" class="block py-2 text-text-dark/75" @click="mobileOpen = false">Inbox</router-link>
        <router-link to="/listings/new" class="block py-2 text-primary-bg font-medium" @click="mobileOpen = false">List Property</router-link>
        <button @click="handleLogout" class="block py-2 text-destructive">Logout</button>
      </template>
      <template v-else>
        <router-link to="/login" class="block py-2 text-text-dark/75" @click="mobileOpen = false">Login</router-link>
        <router-link to="/signup" class="block py-2 text-primary-bg font-medium" @click="mobileOpen = false">Sign Up</router-link>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const router = useRouter()
const mobileOpen = ref(false)

async function handleLogout() {
  await authStore.logout()
  mobileOpen.value = false
  router.push('/')
}

// Fetch user on app load
authStore.fetchUser()
</script>
