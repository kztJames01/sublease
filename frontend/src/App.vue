<template>
  <div class="min-h-screen flex flex-col">
    <Navbar v-if="!isAuthRoute" />
    <main class="flex-1">
      <router-view />
    </main>
    <Footer v-if="!isAuthRoute" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const route = useRoute()

const authRoutes = ['login', 'signup', 'password-reset']
const isAuthRoute = computed(() => authRoutes.includes(route.name))
</script>
