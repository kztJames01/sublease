<template>
  <div>
    <!-- Hero Section -->
    <section class="relative text-primary-fg" style="background: linear-gradient(135deg, rgb(var(--primary-background)) 0%, rgb(var(--primary-background) / 0.94) 48%, rgb(var(--secondary-background)) 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
        <div class="max-w-2xl">
          <h1 class="text-4xl lg:text-6xl font-display font-bold leading-tight">
            Find Your Perfect<br /><span class="text-primary-fg/80">Sublease</span>
          </h1>
          <p class="mt-4 text-lg text-primary-fg/85">
            Search student housing, apartments, and subleases near your campus.
          </p>
          <div class="mt-8 flex flex-col sm:flex-row gap-3">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search by location, school, or keyword..."
              class="flex-1 px-5 py-3 rounded-xl text-text-dark placeholder:text-text-dark/45 focus:outline-none focus:ring-2 focus:ring-primary-bg/35"
              @keyup.enter="goSearch"
            />
            <button @click="goSearch" class="bg-surface text-primary-bg font-semibold px-6 py-3 rounded-xl hover:bg-surface-alt transition">
              Search
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-display font-bold text-text-dark">How It Works</h2>
        <p class="mt-2 text-text-dark/70">Three simple steps to find your next place</p>
      </div>
      <div class="grid md:grid-cols-3 gap-8">
        <div v-for="feature in features" :key="feature.title" class="text-center p-6 rounded-2xl bg-surface shadow-sm hover:shadow-md transition border border-border">
          <div class="w-14 h-14 mx-auto mb-4 bg-secondary-bg/15 text-secondary-bg rounded-xl flex items-center justify-center text-2xl">
            {{ feature.icon }}
          </div>
          <h3 class="text-lg font-semibold mb-2">{{ feature.title }}</h3>
          <p class="text-text-dark/70 text-sm">{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- Latest Listings -->
    <section class="bg-secondary-bg/8 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between mb-8">
          <h2 class="text-3xl font-display font-bold text-text-dark">Latest Listings</h2>
          <router-link to="/search" class="text-primary-bg hover:text-primary-bg/80 font-medium">View all →</router-link>
        </div>
        <div v-if="loading" class="text-center py-12 text-text-dark/55">Loading listings...</div>
        <div v-else-if="latestListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <ListingCard v-for="listing in latestListings" :key="listing.id" :listing="listing" />
        </div>
        <div v-else class="text-center py-12 text-text-dark/55">No listings yet. Be the first to post!</div>
      </div>
    </section>

    <!-- Reviews -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-display font-bold text-text-dark text-center mb-10">What Students Say</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div v-for="review in reviews" :key="review.name" class="bg-surface p-6 rounded-2xl shadow-sm border border-border">
          <div class="flex items-center gap-1 text-orange mb-3">
            <span v-for="n in 5" :key="n">★</span>
          </div>
          <p class="text-text-dark/75 text-sm mb-4">{{ review.text }}</p>
          <p class="font-semibold text-text-dark">{{ review.name }}</p>
        </div>
      </div>
    </section>

    <!-- Newsletter -->
    <section class="bg-primary-bg text-primary-fg py-16">
      <div class="max-w-2xl mx-auto px-4 text-center">
        <h2 class="text-3xl font-display font-bold mb-3">Stay Updated</h2>
        <p class="text-primary-fg/85 mb-6">Get notified about new subleases in your area.</p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center">
          <input type="email" placeholder="Enter your email" class="px-5 py-3 rounded-xl text-text-dark placeholder:text-text-dark/45 focus:outline-none flex-1 max-w-md" />
          <button class="bg-surface text-primary-bg font-semibold px-6 py-3 rounded-xl hover:bg-surface-alt transition">Subscribe</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { listings } from '../api'
import ListingCard from '../components/ListingCard.vue'

const router = useRouter()
const searchQuery = ref('')
const latestListings = ref([])
const loading = ref(true)

const features = [
  { icon: '🔍', title: 'Search Subleases', description: 'Browse verified listings from students near your campus.' },
  { icon: '🏠', title: 'List Your Property', description: 'Create a listing in minutes and reach thousands of students.' },
  { icon: '💬', title: 'Connect Directly', description: 'Message hosts directly and arrange viewings on your schedule.' },
]

const reviews = [
  { name: 'Alex M.', text: 'Found my sublease in less than a week. The direct messaging made everything so easy!' },
  { name: 'Sarah K.', text: 'Listed my apartment and got 5 inquiries on the first day. Highly recommend!' },
  { name: 'Jordan T.', text: 'Clean interface and great filters. Way better than scrolling through social media posts.' },
]

function goSearch() {
  router.push({ name: 'search', query: { q: searchQuery.value } })
}

onMounted(async () => {
  try {
    const { data } = await listings.list({ limit: 6 })
    latestListings.value = Array.isArray(data) ? data.slice(0, 6) : (data.results || []).slice(0, 6)
  } catch {
    latestListings.value = []
  } finally {
    loading.value = false
  }
})
</script>
