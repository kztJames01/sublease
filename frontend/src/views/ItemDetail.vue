<template>
  <div class="min-h-screen bg-page">
    <!-- Top bar: back + help -->
    <div :class="scrolled ? 'bg-primary-bg/95 backdrop-blur shadow-lg' : 'bg-transparent'"
      class="fixed top-0 left-0 right-0 z-50 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
        <button @click="goBack"
          class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back to Dashboard
        </button>
        <button @click="showHelp = !showHelp"
          class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Help
        </button>
      </div>
    </div>

    <Transition enter-active-class="transition duration-200" enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150"
      leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="showHelp"
        class="fixed top-14 right-4 z-50 w-80 bg-white rounded-2xl shadow-2xl border border-border p-5">
        <h3 class="font-semibold text-text-dark mb-2">Need help?</h3>
        <p class="text-sm text-text-muted leading-relaxed">Choose "Individual Sublease" to list your own place, or
          "Apartment Complex" to register a property management listing. Visit our <router-link to="/faq"
            class="text-orange hover:underline">FAQ</router-link> for more info.</p>
      </div>
    </Transition>

    <div>
      <div v-if="loading" class="flex items-center justify-center min-h-[60vh]">
        <div class="w-8 h-8 border-2 border-orange border-t-transparent rounded-full animate-spin" />
      </div>

      <template v-else-if="item">
        <!-- Hero image -->
        <div class="relative bg-[#0a1628]">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-6">
            <img :src="item.image || '/placeholder.jpg'" :alt="item.name" class="w-full h-[400px] object-cover rounded-2xl" />
          </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="grid lg:grid-cols-3 gap-10">
            <div class="lg:col-span-2 space-y-6">
              <div
                v-motion
                :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
              >
                <h1 class="text-3xl lg:text-4xl font-display font-bold text-text-dark">{{ item.name }}</h1>
                <p class="text-sm text-text-soft mt-2">Listed {{ formatDate(item.created_at) }}</p>
              </div>
              <div
                v-if="item.description"
                v-motion
                :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 150, duration: 500 } }"
              >
                <h2 class="text-xl font-semibold text-text-dark mb-3">Description</h2>
                <p class="text-text-muted leading-relaxed whitespace-pre-line">{{ item.description }}</p>
              </div>
            </div>

            <!-- Sidebar -->
            <div>
              <div
                v-motion
                :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 200, duration: 500 } }"
                class="bg-white rounded-3xl shadow-xl p-7 sticky top-20 border border-border/50"
              >
                <p class="text-4xl font-bold text-primary-bg">${{ item.price }}</p>
                <span v-if="item.is_sold" class="inline-block mt-2 px-3 py-1 rounded-full text-xs font-medium bg-destructive/10 text-destructive">Sold</span>

                <div v-if="isOwner" class="mt-6 space-y-3">
                  <router-link :to="`/items/${item.id}/edit`" class="block w-full text-center bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20">
                    Edit Item
                  </router-link>
                  <button @click="deleteItem" class="w-full bg-destructive/8 text-destructive py-3.5 rounded-2xl font-semibold hover:bg-destructive/12 transition border border-destructive/15">
                    Delete Item
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <div v-else class="flex flex-col items-center justify-center min-h-[60vh] text-text-soft gap-3">
        <p>Item not found.</p>
        <button @click="goBack" class="mt-2 text-sm text-orange hover:underline">Go back</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { items as itemsApi } from '../api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const item = ref(null)
const loading = ref(true)
const showHelp = ref(false)
const isOwner = computed(() => item.value?.created_by === authStore.user?.id)
const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 20
}


function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/dashboard')
}

async function deleteItem() {
  if (!confirm('Delete this item?')) return
  try {
    await itemsApi.delete(item.value.id)
    router.push('/dashboard')
  } catch {
    alert('Failed to delete.')
  }
}

onMounted(async () => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
  try {
    const { data } = await itemsApi.get(route.params.id)
    item.value = data
  } catch {
    item.value = null
  } finally {
    loading.value = false
  }
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>
