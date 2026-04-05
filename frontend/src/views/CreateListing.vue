<template>
  <div class="min-h-screen bg-page">
    <!-- Top bar: back + help -->
    <div :class="scrolled ? 'bg-primary-bg/95 backdrop-blur shadow-lg' : 'bg-transparent'"
      class="fixed top-0 left-0 right-0 z-50 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
        <button @click="goBack" class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          Back to Dashboard
        </button>
        <button @click="showHelp = !showHelp" class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          Help
        </button>
      </div>
    </div>

    <Transition enter-active-class="transition duration-200" enter-from-class="opacity-0 -translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150" leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="showHelp" class="fixed top-14 right-4 z-50 w-80 bg-white rounded-2xl shadow-2xl border border-border p-5">
        <h3 class="font-semibold text-text-dark mb-2">Need help?</h3>
        <p class="text-sm text-text-muted leading-relaxed">Choose "Individual Sublease" to list your own place, or "Apartment Complex" to register a property management listing. Visit our <router-link to="/faq" class="text-orange hover:underline">FAQ</router-link> for more info.</p>
      </div>
    </Transition>

    <!-- Dark hero -->
    <div class="relative bg-gradient-to-r from-[#0a1628] via-primary-bg to-[#1a3a6b] pt-[5.5rem] pb-10 px-4 sm:px-6 lg:px-8">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="absolute top-20 right-[10%] w-72 h-72 rounded-full bg-orange/10 blur-3xl" />
      <div class="absolute bottom-20 left-[5%] w-96 h-96 rounded-full bg-primary-bg/40 blur-3xl" />
      <div class="relative max-w-3xl mx-auto">
        <span class="text-sm font-semibold text-orange uppercase tracking-widest">Application</span>
        <h1 class="text-3xl lg:text-4xl font-display font-bold text-white mt-1">Create Listing</h1>
      </div>
    </div>

    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 relative z-10 pb-16">
      <!-- Type Toggle -->
      <div class="flex gap-2 mb-6">
        <button @click="listingType = 'individual'"
          :class="listingType === 'individual' ? 'bg-primary-bg text-white border-primary-bg shadow-lg shadow-primary-bg/20' : 'bg-white text-text-muted border-border'"
          class="px-5 py-2.5 rounded-xl font-medium transition border">
          Individual Sublease
        </button>
        <button @click="listingType = 'apartment'"
          :class="listingType === 'apartment' ? 'bg-primary-bg text-white border-primary-bg shadow-lg shadow-primary-bg/20' : 'bg-white text-text-muted border-border'"
          class="px-5 py-2.5 rounded-xl font-medium transition border">
          Apartment Complex
        </button>
      </div>

      <!-- Individual Listing Form -->
      <form v-if="listingType === 'individual'" @submit.prevent="submitIndividual"
        v-motion :initial="{ opacity: 0, y: 20 }" :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
        class="bg-white rounded-3xl shadow-xl p-8 space-y-5 border border-border/50">
        <div v-if="error" class="bg-destructive/8 text-destructive text-sm rounded-xl px-4 py-3 border border-destructive/15">{{ error }}</div>

        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Property Type</label>
          <select v-model="individual.property_type" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
            <option value="" disabled>Select type</option>
            <option v-for="pt in propTypes" :key="pt.id" :value="pt.id">{{ pt.name }}</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Title</label>
          <input v-model="individual.title" type="text" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Bedrooms</label>
            <input v-model.number="individual.bedrooms" type="number" min="0" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Bedroom Setup</label>
            <select v-model="individual.bedroom_privacy" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
              <option value="" disabled>Select setup</option>
              <option value="private">Private</option>
              <option value="shared">Shared</option>
            </select>
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Bathrooms</label>
            <input v-model.number="individual.bathrooms" type="number" min="0" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Bathroom Setup</label>
            <select v-model="individual.bathroom_privacy" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
              <option value="" disabled>Select setup</option>
              <option value="private">Private</option>
              <option value="shared">Shared</option>
            </select>
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Address</label>
          <input v-model="individual.address" type="text" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Sublease Website</label>
          <input v-model="individual.website_url" type="url" required placeholder="https://example.com/listing"
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Price ($/month)</label>
          <input v-model.number="individual.price" type="number" min="0" step="0.01" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Description</label>
          <textarea v-model="individual.description" rows="4" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition"></textarea>
        </div>

        <!-- Amenities -->
        <div>
          <label class="block text-sm font-medium text-text-muted mb-3">Amenities</label>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
            <button
              v-for="a in amenityOptions"
              :key="a.name"
              type="button"
              @click="toggleAmenity(a.name)"
              :class="selectedAmenities.has(a.name)
                ? 'border-orange bg-orange/10 text-orange'
                : 'border-border bg-white text-text-muted hover:border-primary-bg/30'"
              class="flex items-center gap-2.5 px-4 py-3 rounded-xl border transition text-sm font-medium"
            >
              <span class="text-lg">{{ amenityIcon(a.name) }}</span>
              {{ a.name }}
            </button>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Cover Image</label>
          <input type="file" accept="image/*" required @change="individual.images = $event.target.files[0]"
            class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Gallery Images (optional, up to 10)</label>
          <input type="file" accept="image/*" multiple @change="individual.gallery = [...$event.target.files]"
            class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Video (optional)</label>
          <input type="file" accept="video/*" @change="individual.video = $event.target.files[0]"
            class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
        </div>
        <button type="submit" :disabled="submitting"
          class="w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20 disabled:opacity-50">
          {{ submitting ? 'Creating...' : 'Create Listing' }}
        </button>
      </form>

      <!-- Apartment Listing Form -->
      <form v-else @submit.prevent="submitApartment"
        v-motion :initial="{ opacity: 0, y: 20 }" :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
        class="bg-white rounded-3xl shadow-xl p-8 space-y-5 border border-border/50">
        <div v-if="error" class="bg-destructive/8 text-destructive text-sm rounded-xl px-4 py-3 border border-destructive/15">{{ error }}</div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">First Name</label>
            <input v-model="apartment.first_name" type="text" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Last Name</label>
            <input v-model="apartment.last_name" type="text" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Email</label>
          <input v-model="apartment.email" type="email" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Phone</label>
          <input v-model="apartment.phone" type="text" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Company</label>
          <input v-model="apartment.company" type="text" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Property Website</label>
          <input v-model="apartment.website_url" type="url" required placeholder="https://example.com"
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div class="grid grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">City</label>
            <input v-model="apartment.city" type="text" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">State</label>
            <input v-model="apartment.state" type="text" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-muted mb-1.5">Zip Code</label>
            <input v-model="apartment.zipCode" type="text" required
              class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Country</label>
          <input v-model="apartment.country" type="text" required
            class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <button type="submit" :disabled="submitting"
          class="w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20 disabled:opacity-50">
          {{ submitting ? 'Submitting...' : 'Submit Application' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { listings as listingsApi, apartmentListings, propertyTypes, amenities as amenitiesApi } from '../api'

const DEFAULT_AMENITIES = [
  'In-unit Laundry',
  'On-site Laundry',
  'Pool',
  'Gym',
  'Parking',
  'High-speed Internet',
  'Air Conditioning',
  'Heating',
  'Pet Friendly',
  'Balcony or Patio',
  'Dishwasher',
  'Elevator',
  'Security System',
  'Storage Space',
]

const router = useRouter()
const listingType = ref('individual')
const error = ref('')
const submitting = ref(false)
const showHelp = ref(false)
const propTypes = ref([])
const amenityOptions = ref(DEFAULT_AMENITIES.map((name) => ({ name })))
const selectedAmenities = reactive(new Set())
const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 20
}

const individual = reactive({
  property_type: '', title: '', bedrooms: 1, bedroom_privacy: '', bathrooms: 1, bathroom_privacy: '',
  address: '', website_url: '', price: 0, description: '',
  images: null, gallery: [], video: null,
})

const apartment = reactive({
  first_name: '', last_name: '', email: '', phone: '',
  company: '', website_url: '', city: '', zipCode: '', state: '', country: '',
})
function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/dashboard')
}

function toggleAmenity(id) {
  if (selectedAmenities.has(id)) selectedAmenities.delete(id)
  else selectedAmenities.add(id)
}

function amenityIcon(name) {
  const n = name.toLowerCase()
  if (n.includes('laundry')) return '🧺'
  if (n.includes('pool') || n.includes('swim')) return '🏊'
  if (n.includes('parking')) return '🅿️'
  if (n.includes('gym') || n.includes('fitness')) return '🏋️'
  if (n.includes('wifi') || n.includes('internet')) return '📶'
  if (n.includes('air') || n.includes('ac')) return '❄️'
  if (n.includes('heat')) return '🔥'
  if (n.includes('garbage') || n.includes('trash')) return '🗑️'
  if (n.includes('pet')) return '🐾'
  if (n.includes('balcon') || n.includes('patio')) return '🌿'
  if (n.includes('dishwash')) return '🍽️'
  if (n.includes('elevator')) return '🛗'
  if (n.includes('security')) return '🔒'
  if (n.includes('storage')) return '📦'
  return '✨'
}

onMounted(async () => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
  try {
    const [ptRes, amRes] = await Promise.all([propertyTypes.list(), amenitiesApi.list()])
    propTypes.value = Array.isArray(ptRes.data) ? ptRes.data : ptRes.data.results || []
    const fromApi = Array.isArray(amRes.data) ? amRes.data : amRes.data.results || []
    const merged = new Set(DEFAULT_AMENITIES.map((name) => name.toLowerCase()))
    const mergedAmenities = [...DEFAULT_AMENITIES]
    for (const a of fromApi) {
      const name = String(a?.name || '').trim()
      if (!name) continue
      if (!merged.has(name.toLowerCase())) {
        merged.add(name.toLowerCase())
        mergedAmenities.push(name)
      }
    }
    amenityOptions.value = mergedAmenities.map((name) => ({ name }))
  } catch { /* silent */ }
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})

async function submitIndividual() {
  error.value = ''
  submitting.value = true
  try {
    const fd = new FormData()
    for (const [key, val] of Object.entries(individual)) {
      if (key === 'gallery') continue
      if (val !== null && val !== '') fd.append(key, val)
    }
    // Gallery images
    if (individual.gallery?.length) {
      for (const file of individual.gallery) {
        fd.append('gallery_images', file)
      }
    }
    // Amenities
    for (const amenityName of selectedAmenities) {
      fd.append('amenity_names', amenityName)
    }
    const { data } = await listingsApi.create(fd)
    router.push(`/listings/${data.id}`)
  } catch (e) {
    error.value = typeof e.response?.data === 'object' ? Object.values(e.response.data).flat().join(' ') : 'Failed to create listing.'
  } finally {
    submitting.value = false
  }
}

async function submitApartment() {
  error.value = ''
  submitting.value = true
  try {
    await apartmentListings.create(apartment)
    router.push('/dashboard')
  } catch (e) {
    error.value = typeof e.response?.data === 'object' ? Object.values(e.response.data).flat().join(' ') : 'Failed to submit.'
  } finally {
    submitting.value = false
  }
}
</script>
