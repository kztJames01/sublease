<template>
  <div>
    <!-- Hero Section -->
    <section class="relative overflow-hidden min-h-[90vh] flex items-center pt-16">
      <!-- Background layers -->
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_50%_at_80%_-20%,rgba(252,163,17,0.18),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-page to-transparent" />

      <!-- Floating shapes -->
      <div class="absolute top-20 right-[10%] w-72 h-72 rounded-full bg-orange/10 blur-3xl" />
      <div class="absolute bottom-20 left-[5%] w-96 h-96 rounded-full bg-primary-bg/40 blur-3xl" />

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-0 w-full">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <div
              v-motion
              :initial="{ opacity: 0, y: 20 }"
              :enter="{ opacity: 1, y: 0, transition: { delay: 100, duration: 600 } }"
            >
              <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur text-white/80 text-sm font-medium border border-white/10 mb-6">
                <span class="w-2 h-2 rounded-full bg-orange animate-pulse" />
                Trusted by 10,000+ students
              </span>
            </div>

            <h1
              v-motion
              :initial="{ opacity: 0, y: 30 }"
              :enter="{ opacity: 1, y: 0, transition: { delay: 200, duration: 700 } }"
              class="text-5xl lg:text-7xl font-display font-bold leading-[1.05] text-white"
            >
              Find Your
              <br />
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-orange via-orange to-yellow-300">
                Perfect Sublease
              </span>
            </h1>

            <p
              v-motion
              :initial="{ opacity: 0, y: 20 }"
              :enter="{ opacity: 1, y: 0, transition: { delay: 400, duration: 600 } }"
              class="mt-6 text-lg lg:text-xl text-white/70 max-w-lg leading-relaxed"
            >
              Search student housing, apartments, and subleases near your campus — all in one place.
            </p>

            <div
              v-motion
              :initial="{ opacity: 0, y: 20 }"
              :enter="{ opacity: 1, y: 0, transition: { delay: 550, duration: 600 } }"
              class="mt-10 flex flex-col sm:flex-row gap-3"
            >
              <div class="relative flex-1">
                <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-text-soft" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                <input
                  v-model="searchQuery"
                  type="text"
                  placeholder="Search by location, school, or keyword..."
                  class="w-full pl-12 pr-5 py-4 rounded-2xl bg-white/95 backdrop-blur text-text-dark placeholder:text-text-soft/70 focus:outline-none focus:ring-2 focus:ring-orange/40 shadow-lg text-sm"
                  @keyup.enter="goSearch"
                />
              </div>
              <button @click="goSearch" class="bg-orange text-primary-bg font-bold px-8 py-4 rounded-2xl hover:bg-orange/90 transition shadow-lg shadow-orange/20 text-sm">
                Search
              </button>
            </div>

            <div
              v-motion
              :initial="{ opacity: 0 }"
              :enter="{ opacity: 1, transition: { delay: 750, duration: 600 } }"
              class="mt-8 flex items-center gap-6 text-white/80 text-sm"
            >
              <span class="flex items-center gap-2"><svg class="w-4 h-4 text-orange" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Verified listings</span>
              <span class="flex items-center gap-2"><svg class="w-4 h-4 text-orange" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Direct messaging</span>
              <span class="flex items-center gap-2"><svg class="w-4 h-4 text-orange" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Free to use</span>
            </div>
          </div>

          <!-- Right side: floating stat cards -->
          <div class="hidden lg:flex justify-center relative">
            <div
              v-motion
              :initial="{ opacity: 0, scale: 0.9, y: 40 }"
              :enter="{ opacity: 1, scale: 1, y: 0, transition: { delay: 500, duration: 800 } }"
              class="relative"
            >
              <div class="w-80 h-80 rounded-3xl bg-gradient-to-br from-white/10 to-white/5 backdrop-blur border border-white/10 p-8 flex flex-col justify-between">
                <div>
                  <div class="w-12 h-12 rounded-2xl bg-orange/20 flex items-center justify-center mb-4">
                    <svg class="w-6 h-6 text-orange" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                  </div>
                  <p class="text-white/50 text-sm">Available listings</p>
                  <p class="text-4xl font-bold text-white mt-1">2,400+</p>
                </div>
                <div class="flex gap-3">
                  <div class="flex-1 rounded-xl bg-white/8 p-3 text-center">
                    <p class="text-xl font-bold text-orange">98%</p>
                    <p class="text-[11px] text-white/50 mt-0.5">Satisfaction</p>
                  </div>
                  <div class="flex-1 rounded-xl bg-white/8 p-3 text-center">
                    <p class="text-xl font-bold text-orange">3 days</p>
                    <p class="text-[11px] text-white/50 mt-0.5">Avg. match</p>
                  </div>
                </div>
              </div>

              <!-- Floating badge -->
              <div
                v-motion
                :initial="{ opacity: 0, x: 30 }"
                :enter="{ opacity: 1, x: 0, transition: { delay: 900, duration: 600 } }"
                class="absolute -right-8 top-16 bg-white rounded-2xl shadow-2xl p-4 flex items-center gap-3 border border-border"
              >
                <div class="w-10 h-10 rounded-xl bg-green-500/15 flex items-center justify-center">
                  <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                </div>
                <div>
                  <p class="text-sm font-semibold text-text-dark">Lease signed!</p>
                  <p class="text-xs text-text-soft">Just now</p>
                </div>
              </div>

              <!-- Floating badge left -->
              <div
                v-motion
                :initial="{ opacity: 0, x: -30 }"
                :enter="{ opacity: 1, x: 0, transition: { delay: 1100, duration: 600 } }"
                class="absolute -left-6 bottom-12 bg-white rounded-2xl shadow-2xl p-4 flex items-center gap-3 border border-border"
              >
                <div class="w-10 h-10 rounded-xl bg-orange/15 flex items-center justify-center">
                  <svg class="w-5 h-5 text-orange" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                </div>
                <div>
                  <p class="text-sm font-semibold text-text-dark">5 new messages</p>
                  <p class="text-xs text-text-soft">2 min ago</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 600 } }"
        class="text-center mb-16"
      >
        <span class="text-sm font-semibold text-orange uppercase tracking-widest">How it works</span>
        <h2 class="text-4xl font-display font-bold text-text-dark mt-3">Three Simple Steps</h2>
        <p class="mt-3 text-text-muted max-w-lg mx-auto">From search to signing — we make finding your next place effortless.</p>
      </div>
      <div class="grid md:grid-cols-3 gap-8">
        <div
          v-for="(feature, i) in features"
          :key="feature.title"
          v-motion
          :initial="{ opacity: 0, y: 30 }"
          :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 150, duration: 500 } }"
          class="group text-center p-8 rounded-3xl bg-surface border border-border hover:border-orange/30 hover:shadow-xl hover:shadow-orange/5 transition-all duration-300"
        >
          <div class="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-orange/15 to-orange/5 text-orange rounded-2xl flex items-center justify-center text-3xl group-hover:scale-110 transition-transform duration-300">
            {{ feature.icon }}
          </div>
          <h3 class="text-lg font-bold mb-2 text-text-dark">{{ feature.title }}</h3>
          <p class="text-text-muted text-sm leading-relaxed">{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- Latest Listings -->
    <section class="relative py-24">
      <!-- White-to-prussian gradient top -->
      <div class="absolute inset-0 bg-primary-bg" />
      <div class="absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-page to-transparent" />
      <div class="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-page to-transparent" />
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 600 } }"
          class="flex items-end justify-between mb-10"
        >
          <div>
            <span class="text-sm font-semibold text-orange uppercase tracking-widest">Browse</span>
            <h2 class="text-4xl font-display font-bold text-white mt-2">Latest Listings</h2>
          </div>
          <router-link to="/search" class="text-white/80 hover:text-orange font-semibold text-sm transition flex items-center gap-1">
            View all
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </router-link>
        </div>
        <div v-if="loading" class="text-center py-16 text-white/60">Loading listings...</div>
        <div v-else-if="latestListings.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(listing, i) in latestListings"
            :key="listing.id"
            v-motion
            :initial="{ opacity: 0, y: 30 }"
            :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 100, duration: 500 } }"
          >
            <ListingCard :listing="listing" />
          </div>
        </div>
        <div v-else class="text-center py-16 text-white/60">No listings yet. Be the first to post!</div>
      </div>
    </section>

    <!-- Reviews -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 600 } }"
        class="text-center mb-14"
      >
        <span class="text-sm font-semibold text-orange uppercase tracking-widest">Testimonials</span>
        <h2 class="text-4xl font-display font-bold text-text-dark mt-3">What Students Say</h2>
      </div>
      <div class="grid md:grid-cols-3 gap-8">
        <div
          v-for="(review, i) in reviews"
          :key="review.name"
          v-motion
          :initial="{ opacity: 0, y: 30 }"
          :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 150, duration: 500 } }"
          class="bg-surface p-8 rounded-3xl border border-border hover:shadow-lg transition-shadow duration-300"
        >
          <div class="flex items-center gap-1 text-orange mb-4">
            <span v-for="n in 5" :key="n">★</span>
          </div>
          <p class="text-text-muted text-sm leading-relaxed mb-6">"{{ review.text }}"</p>
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-primary-bg/10 flex items-center justify-center text-primary-bg font-bold text-sm">
              {{ review.name.charAt(0) }}
            </div>
            <p class="font-semibold text-text-dark text-sm">{{ review.name }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA / Newsletter -->
    <section class="relative overflow-hidden py-24">
      <div class="absolute inset-0 bg-gradient-to-b from-primary-bg via-[#0f1d36] to-[#0a1628]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_50%_at_50%_0%,rgba(252,163,17,0.1),transparent)]" />
      <div
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visibleOnce="{ opacity: 1, y: 0, transition: { duration: 700 } }"
        class="relative max-w-2xl mx-auto px-4 text-center"
      >
        <h2 class="text-4xl font-display font-bold text-white mb-4">Stay Updated</h2>
        <p class="text-white/65 text-lg mb-10">Get notified about new subleases in your area — never miss a listing.</p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center">
          <input
            type="email"
            placeholder="Enter your email"
            class="px-5 py-4 rounded-2xl bg-white/95 text-text-dark placeholder:text-text-soft/70 focus:outline-none focus:ring-2 focus:ring-orange/40 flex-1 max-w-md shadow-lg text-sm"
          />
          <button class="bg-orange text-primary-bg font-bold px-8 py-4 rounded-2xl hover:bg-orange/90 transition shadow-lg shadow-orange/20 text-sm">
            Subscribe
          </button>
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
  { icon: '🔍', title: 'Search Subleases', description: 'Browse verified listings from students near your campus with powerful filters.' },
  { icon: '🏠', title: 'List Your Property', description: 'Create a listing in minutes and reach thousands of students looking for housing.' },
  { icon: '💬', title: 'Connect Directly', description: 'Message hosts directly and arrange viewings on your own schedule.' },
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
