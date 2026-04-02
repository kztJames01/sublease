<template>
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-8">Create Listing</h1>

    <!-- Type Toggle -->
    <div class="flex gap-2 mb-8">
      <button
        @click="listingType = 'individual'"
        :class="listingType === 'individual' ? 'bg-primary-500 text-white' : 'bg-white text-gray-600 border'"
        class="px-5 py-2.5 rounded-lg font-medium transition"
      >
        Individual Sublease
      </button>
      <button
        @click="listingType = 'apartment'"
        :class="listingType === 'apartment' ? 'bg-primary-500 text-white' : 'bg-white text-gray-600 border'"
        class="px-5 py-2.5 rounded-lg font-medium transition"
      >
        Apartment Complex
      </button>
    </div>

    <!-- Individual Listing Form -->
    <form v-if="listingType === 'individual'" @submit.prevent="submitIndividual" class="bg-white rounded-2xl shadow-sm p-8 space-y-5">
      <div v-if="error" class="bg-red-50 text-red-600 text-sm p-3 rounded-lg">{{ error }}</div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Property Type</label>
        <select v-model="individual.property_type" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300">
          <option value="" disabled>Select type</option>
          <option v-for="pt in propTypes" :key="pt.id" :value="pt.id">{{ pt.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
        <input v-model="individual.title" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Bedrooms</label>
          <input v-model.number="individual.bedrooms" type="number" min="0" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Bathrooms</label>
          <input v-model.number="individual.bathrooms" type="number" min="0" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Address</label>
        <input v-model="individual.address" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Price ($/month)</label>
        <input v-model.number="individual.price" type="number" min="0" step="0.01" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
        <textarea v-model="individual.description" rows="4" class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300"></textarea>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Images</label>
        <input type="file" accept="image/*" @change="individual.images = $event.target.files[0]" class="w-full text-sm" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Video (optional)</label>
        <input type="file" accept="video/*" @change="individual.video = $event.target.files[0]" class="w-full text-sm" />
      </div>
      <button type="submit" :disabled="submitting" class="w-full bg-primary-500 text-white py-3 rounded-lg font-medium hover:bg-primary-600 transition disabled:opacity-50">
        {{ submitting ? 'Creating...' : 'Create Listing' }}
      </button>
    </form>

    <!-- Apartment Listing Form -->
    <form v-else @submit.prevent="submitApartment" class="bg-white rounded-2xl shadow-sm p-8 space-y-5">
      <div v-if="error" class="bg-red-50 text-red-600 text-sm p-3 rounded-lg">{{ error }}</div>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
          <input v-model="apartment.first_name" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
          <input v-model="apartment.last_name" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input v-model="apartment.email" type="email" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Phone</label>
        <input v-model="apartment.phone" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Company</label>
        <input v-model="apartment.company" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div class="grid grid-cols-3 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">City</label>
          <input v-model="apartment.city" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">State</label>
          <input v-model="apartment.state" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Zip Code</label>
          <input v-model="apartment.zipCode" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
        </div>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Country</label>
        <input v-model="apartment.country" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <button type="submit" :disabled="submitting" class="w-full bg-primary-500 text-white py-3 rounded-lg font-medium hover:bg-primary-600 transition disabled:opacity-50">
        {{ submitting ? 'Submitting...' : 'Submit Application' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { listings as listingsApi, apartmentListings, propertyTypes } from '../api'

const router = useRouter()
const listingType = ref('individual')
const error = ref('')
const submitting = ref(false)
const propTypes = ref([])

const individual = reactive({
  property_type: '', title: '', bedrooms: 1, bathrooms: 1,
  address: '', price: 0, description: '', images: null, video: null,
})

const apartment = reactive({
  first_name: '', last_name: '', email: '', phone: '',
  company: '', city: '', zipCode: '', state: '', country: '',
})

onMounted(async () => {
  try {
    const { data } = await propertyTypes.list()
    propTypes.value = Array.isArray(data) ? data : data.results || []
  } catch { /* silent */ }
})

async function submitIndividual() {
  error.value = ''
  submitting.value = true
  try {
    const fd = new FormData()
    for (const [key, val] of Object.entries(individual)) {
      if (val !== null && val !== '') fd.append(key, val)
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
