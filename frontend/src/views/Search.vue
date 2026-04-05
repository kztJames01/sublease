<template>
  <div>
    <!-- Hero banner -->
    <section class="relative pt-16 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_60%_40%_at_80%_-20%,rgba(252,163,17,0.12),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
      <div class="absolute top-20 right-[10%] w-72 h-72 rounded-full bg-orange/10 blur-3xl" />
      <div class="absolute bottom-20 left-[5%] w-96 h-96 rounded-full bg-primary-bg/40 blur-3xl" />
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-20">
        <div
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 600 } }"
        >
          <span class="text-sm font-semibold text-orange uppercase tracking-widest">Browse</span>
          <h1 class="text-4xl lg:text-5xl font-display font-bold text-white mt-2">Search Listings</h1>
          <p class="text-white/60 mt-3 text-lg">{{ filteredListings.length }} results found</p>
        </div>

        <!-- Tabs -->
        <div
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: 200, duration: 500 } }"
          class="flex gap-2 mt-8"
        >
          <button
            @click="activeTab = 'subleases'"
            :class="activeTab === 'subleases' ? 'bg-orange text-primary-bg font-bold' : 'bg-white/10 text-white/75 border border-white/10'"
            class="px-5 py-2.5 rounded-xl text-sm transition"
          >
            Subleases
          </button>
          <button
            @click="activeTab = 'apartments'"
            :class="activeTab === 'apartments' ? 'bg-orange text-primary-bg font-bold' : 'bg-white/10 text-white/75 border border-white/10'"
            class="px-5 py-2.5 rounded-xl text-sm transition"
          >
            Apartments
          </button>
        </div>
      </div>
    </section>

    <!-- Filters + Results -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 relative z-10 pb-16">
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0, transition: { delay: 300, duration: 500 } }"
        class="bg-surface rounded-2xl shadow-xl p-5 mb-8 flex flex-wrap gap-4 items-center border border-border"
      >
        <div class="relative flex-1 min-w-[200px]">
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-text-soft" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input
            v-model="search"
            type="text"
            placeholder="Search by title or address..."
            class="w-full pl-10 pr-4 py-2.5 border border-border rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20"
          />
        </div>
        <select v-model="sortBy" class="px-4 py-2.5 border border-border rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20">
          <option value="newest">Newest First</option>
          <option value="price-asc">Price: Low to High</option>
          <option value="price-desc">Price: High to Low</option>
        </select>
        <select v-model="priceRange" class="px-4 py-2.5 border border-border rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20">
          <option value="">Any Price</option>
          <option value="0-500">Under $500</option>
          <option value="500-1000">$500 - $1,000</option>
          <option value="1000-1500">$1,000 - $1,500</option>
          <option value="1500+">$1,500+</option>
        </select>
      </div>

      <div v-if="loading" class="text-center py-16 text-text-soft">Loading...</div>
      <div v-else-if="filteredListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="(listing, i) in filteredListings"
          :key="listing.id"
          v-motion
          :initial="{ opacity: 0, y: 25 }"
          :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 80, duration: 450 } }"
        >
          <ListingCard :listing="listing" />
        </div>
      </div>
      <div v-else class="text-center py-16">
        <p class="text-text-soft text-lg">No listings match your search.</p>
        <router-link to="/listings/new" class="inline-block mt-4 text-primary-bg font-semibold hover:text-orange transition">Create a listing →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { listings as listingsApi } from '../api'
import ListingCard from '../components/ListingCard.vue'

const route = useRoute()
const activeTab = ref('subleases')
const search = ref(route.query.q || '')
const sortBy = ref('newest')
const priceRange = ref('')
const allListings = ref([])
const loading = ref(true)

const filteredListings = computed(() => {
  let result = [...allListings.value]

  if (search.value) {
    const q = search.value.toLowerCase()
    result = result.filter(l => l.title?.toLowerCase().includes(q) || l.address?.toLowerCase().includes(q))
  }

  if (priceRange.value) {
    const [min, max] = priceRange.value.includes('+')
      ? [parseInt(priceRange.value), Infinity]
      : priceRange.value.split('-').map(Number)
    result = result.filter(l => l.price >= min && l.price <= max)
  }

  if (sortBy.value === 'price-asc') result.sort((a, b) => a.price - b.price)
  else if (sortBy.value === 'price-desc') result.sort((a, b) => b.price - a.price)

  return result
})

onMounted(async () => {
  try {
    const { data } = await listingsApi.list()
    allListings.value = Array.isArray(data) ? data : data.results || []
  } catch {
    allListings.value = []
  } finally {
    loading.value = false
  }
})
</script>
