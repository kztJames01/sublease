<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
      <div>
        <h1 class="text-3xl font-display font-bold text-text-dark">Search Listings</h1>
        <p class="text-text-dark/70 mt-1">{{ filteredListings.length }} results found</p>
      </div>
      <div class="flex gap-2">
        <button
          @click="activeTab = 'subleases'"
          :class="activeTab === 'subleases' ? 'bg-primary-bg text-primary-fg' : 'bg-surface text-text-dark/75 border border-border'"
          class="px-4 py-2 rounded-lg font-medium transition"
        >
          Subleases
        </button>
        <button
          @click="activeTab = 'apartments'"
          :class="activeTab === 'apartments' ? 'bg-primary-bg text-primary-fg' : 'bg-surface text-text-dark/75 border border-border'"
          class="px-4 py-2 rounded-lg font-medium transition"
        >
          Apartments
        </button>
      </div>
    </div>

    <!-- Filters -->
    <div class="bg-surface rounded-xl shadow-sm p-4 mb-6 flex flex-wrap gap-4 items-center border border-border">
      <input
        v-model="search"
        type="text"
        placeholder="Search by title or address..."
        class="flex-1 min-w-[200px] px-4 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-bg/35"
      />
      <select v-model="sortBy" class="px-4 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-bg/35">
        <option value="newest">Newest First</option>
        <option value="price-asc">Price: Low to High</option>
        <option value="price-desc">Price: High to Low</option>
      </select>
      <select v-model="priceRange" class="px-4 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-bg/35">
        <option value="">Any Price</option>
        <option value="0-500">Under $500</option>
        <option value="500-1000">$500 - $1,000</option>
        <option value="1000-1500">$1,000 - $1,500</option>
        <option value="1500+">$1,500+</option>
      </select>
    </div>

    <!-- Results -->
    <div v-if="loading" class="text-center py-16 text-text-dark/55">Loading...</div>
    <div v-else-if="filteredListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <ListingCard v-for="listing in filteredListings" :key="listing.id" :listing="listing" />
    </div>
    <div v-else class="text-center py-16">
      <p class="text-text-dark/55 text-lg">No listings match your search.</p>
      <router-link to="/listings/new" class="inline-block mt-4 text-primary-bg font-medium hover:text-primary-bg/80">Create a listing →</router-link>
    </div>
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
