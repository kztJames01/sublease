<template>
  <div>
    <!-- Hero banner -->
    <section class="relative pt-16 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
      <div class="absolute top-20 right-[10%] w-72 h-72 rounded-full bg-orange/10 blur-3xl" />
      <div class="absolute bottom-20 left-[5%] w-96 h-96 rounded-full bg-primary-bg/40 blur-3xl" />
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-24">
        <div
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 600 } }"
        >
          <span class="text-sm font-semibold text-orange uppercase tracking-widest">Overview</span>
          <h1 class="text-4xl lg:text-5xl font-display font-bold text-white mt-2">Dashboard</h1>
        </div>
      </div>
    </section>

    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-14 relative z-10 pb-16">
      <!-- Stats -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-10">
        <div
          v-for="(stat, i) in stats"
          :key="stat.label"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: i * 100, duration: 450 } }"
          class="bg-surface rounded-2xl shadow-lg p-6 border border-border hover:shadow-xl transition-shadow duration-300"
        >
          <p class="text-sm text-text-soft">{{ stat.label }}</p>
          <p class="text-3xl font-bold text-text-dark mt-1">{{ stat.value }}</p>
        </div>
      </div>

      <!-- My Listings -->
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 500 } }"
        class="mb-10"
      >
        <div class="flex items-center justify-between mb-5">
          <h2 class="text-xl font-display font-bold text-text-dark">My Listings</h2>
          <router-link to="/listings/new" class="text-primary-bg hover:text-orange text-sm font-semibold transition flex items-center gap-1">
            + New Listing
          </router-link>
        </div>
        <div v-if="myListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(listing, i) in myListings"
            :key="listing.id"
            v-motion
            :initial="{ opacity: 0, y: 20 }"
            :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 80, duration: 400 } }"
          >
            <ListingCard :listing="listing" />
          </div>
        </div>
        <p v-else class="text-text-soft">No listings yet.</p>
      </div>

      <!-- My Items -->
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 500 } }"
      >
        <div class="flex items-center justify-between mb-5">
          <h2 class="text-xl font-display font-bold text-text-dark">My Items</h2>
          <router-link to="/items/new" class="text-primary-bg hover:text-orange text-sm font-semibold transition flex items-center gap-1">
            + New Item
          </router-link>
        </div>
        <div v-if="myItems.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(item, i) in myItems"
            :key="item.id"
            v-motion
            :initial="{ opacity: 0, y: 20 }"
            :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 80, duration: 400 } }"
            class="bg-surface rounded-2xl shadow-sm overflow-hidden border border-border hover:shadow-lg transition-shadow duration-300 group"
          >
            <div class="overflow-hidden">
              <img :src="item.image || '/placeholder.jpg'" :alt="item.name" class="w-full h-40 object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="p-5">
              <h3 class="font-semibold truncate text-text-dark">{{ item.name }}</h3>
              <p class="text-orange font-bold mt-1">${{ item.price }}</p>
              <div class="flex gap-3 mt-3">
                <router-link :to="`/items/${item.id}/edit`" class="text-sm text-text-soft hover:text-primary-bg transition">Edit</router-link>
                <router-link :to="`/items/${item.id}`" class="text-sm text-primary-bg hover:text-orange transition font-medium">View</router-link>
              </div>
            </div>
          </div>
        </div>
        <p v-else class="text-text-soft">No items yet.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { listings as listingsApi, items as itemsApi, conversations as convoApi } from '../api'
import ListingCard from '../components/ListingCard.vue'

const authStore = useAuthStore()
const myListings = ref([])
const myItems = ref([])
const conversationCount = ref(0)

const stats = computed(() => [
  { label: 'Active Listings', value: myListings.value.filter(l => !l.is_sold).length },
  { label: 'Sold', value: myListings.value.filter(l => l.is_sold).length },
  { label: 'Items', value: myItems.value.length },
  { label: 'Messages', value: conversationCount.value },
])

onMounted(async () => {
  const userId = authStore.user?.id
  try {
    const [listRes, itemRes, convoRes] = await Promise.all([
      listingsApi.list(),
      itemsApi.list(),
      convoApi.list(),
    ])
    const listData = Array.isArray(listRes.data) ? listRes.data : listRes.data.results || []
    const itemData = Array.isArray(itemRes.data) ? itemRes.data : itemRes.data.results || []
    const convoData = Array.isArray(convoRes.data) ? convoRes.data : convoRes.data.results || []
    myListings.value = listData.filter(l => l.created_by === userId)
    myItems.value = itemData.filter(i => i.created_by === userId)
    conversationCount.value = convoData.length
  } catch {
    // silent
  }
})
</script>
