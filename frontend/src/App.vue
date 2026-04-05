<template>
  <div class="min-h-screen flex flex-col">
    <Navbar v-if="!hideChrome" />
    <main class="flex-1">
      <router-view />
    </main>
    <Footer v-if="!hideChrome" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const route = useRoute()

const hideChromeRoutes = ['login', 'signup', 'password-reset', 'listing-detail', 'item-detail', 'create-item', 'edit-item', 'create-listing']
const hideChrome = computed(() => hideChromeRoutes.includes(route.name))
</script>
