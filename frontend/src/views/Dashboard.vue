<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-display font-bold text-text-dark mb-8">Dashboard</h1>

    <!-- Stats -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <div class="bg-surface rounded-xl shadow-sm p-5 border border-border">
        <p class="text-sm text-text-soft">Active Listings</p>
        <p class="text-2xl font-bold text-text-dark mt-1">{{ myListings.filter(l => !l.is_sold).length }}</p>
      </div>
      <div class="bg-surface rounded-xl shadow-sm p-5 border border-border">
        <p class="text-sm text-text-soft">Sold</p>
        <p class="text-2xl font-bold text-text-dark mt-1">{{ myListings.filter(l => l.is_sold).length }}</p>
      </div>
      <div class="bg-surface rounded-xl shadow-sm p-5 border border-border">
        <p class="text-sm text-text-soft">Items</p>
        <p class="text-2xl font-bold text-text-dark mt-1">{{ myItems.length }}</p>
      </div>
      <div class="bg-surface rounded-xl shadow-sm p-5 border border-border">
        <p class="text-sm text-text-soft">Messages</p>
        <p class="text-2xl font-bold text-text-dark mt-1">{{ conversationCount }}</p>
      </div>
    </div>

    <!-- My Listings -->
    <div class="mb-10">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-xl font-semibold">My Listings</h2>
        <router-link to="/listings/new" class="text-primary-bg hover:text-primary-bg/80 text-sm font-medium">+ New Listing</router-link>
      </div>
      <div v-if="myListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <ListingCard v-for="listing in myListings" :key="listing.id" :listing="listing" />
      </div>
      <p v-else class="text-text-soft">No listings yet.</p>
    </div>

    <!-- My Items -->
    <div>
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-xl font-semibold">My Items</h2>
        <router-link to="/items/new" class="text-primary-bg hover:text-primary-bg/80 text-sm font-medium">+ New Item</router-link>
      </div>
      <div v-if="myItems.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="item in myItems" :key="item.id" class="bg-surface rounded-xl shadow-sm overflow-hidden border border-border">
          <img :src="item.image || '/placeholder.jpg'" :alt="item.name" class="w-full h-40 object-cover" />
          <div class="p-4">
            <h3 class="font-semibold truncate">{{ item.name }}</h3>
            <p class="text-primary-bg font-bold mt-1">${{ item.price }}</p>
            <div class="flex gap-2 mt-3">
              <router-link :to="`/items/${item.id}/edit`" class="text-sm text-text-soft hover:text-primary-bg">Edit</router-link>
              <router-link :to="`/items/${item.id}`" class="text-sm text-primary-bg hover:text-primary-bg/80">View</router-link>
            </div>
          </div>
        </div>
      </div>
      <p v-else class="text-text-soft">No items yet.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { listings as listingsApi, items as itemsApi, conversations as convoApi } from '../api'
import ListingCard from '../components/ListingCard.vue'

const authStore = useAuthStore()
const myListings = ref([])
const myItems = ref([])
const conversationCount = ref(0)

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
