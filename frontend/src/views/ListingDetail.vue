<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div v-if="loading" class="text-center py-16 text-gray-400">Loading...</div>
    <template v-else-if="listing">
      <!-- Hero Image -->
      <div class="relative rounded-2xl overflow-hidden mb-8">
        <img :src="listing.images || '/placeholder.jpg'" :alt="listing.title" class="w-full h-[400px] object-cover" />
        <span class="absolute top-4 left-4 bg-primary-500 text-white text-sm font-medium px-3 py-1 rounded-full">
          {{ listing.property_type_name || 'Sublease' }}
        </span>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <!-- Details -->
        <div class="lg:col-span-2 space-y-6">
          <div>
            <h1 class="text-3xl font-display font-bold text-gray-900">{{ listing.title }}</h1>
            <p class="text-gray-500 mt-1">{{ listing.address }}</p>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div class="bg-gray-50 rounded-xl p-4 text-center">
              <p class="text-2xl font-bold text-gray-900">{{ listing.bedrooms }}</p>
              <p class="text-sm text-gray-500">Bedrooms</p>
            </div>
            <div class="bg-gray-50 rounded-xl p-4 text-center">
              <p class="text-2xl font-bold text-gray-900">{{ listing.bathrooms }}</p>
              <p class="text-sm text-gray-500">Bathrooms</p>
            </div>
            <div class="bg-gray-50 rounded-xl p-4 text-center">
              <p class="text-2xl font-bold text-gray-900">{{ listing.is_sold ? 'Sold' : 'Active' }}</p>
              <p class="text-sm text-gray-500">Status</p>
            </div>
            <div class="bg-gray-50 rounded-xl p-4 text-center">
              <p class="text-2xl font-bold text-gray-900">{{ formatDate(listing.created_at) }}</p>
              <p class="text-sm text-gray-500">Listed</p>
            </div>
          </div>

          <div v-if="listing.description">
            <h2 class="text-xl font-semibold mb-3">Description</h2>
            <p class="text-gray-600 leading-relaxed whitespace-pre-line">{{ listing.description }}</p>
          </div>

          <!-- Video -->
          <div v-if="listing.video">
            <h2 class="text-xl font-semibold mb-3">Video Tour</h2>
            <video :src="listing.video" controls class="w-full rounded-xl"></video>
          </div>
        </div>

        <!-- Sidebar -->
        <div class="space-y-4">
          <div class="bg-white rounded-xl shadow-sm p-6 sticky top-24">
            <p class="text-3xl font-bold text-primary-600">${{ listing.price }}<span class="text-base font-normal text-gray-400">/mo</span></p>
            <p class="text-gray-500 text-sm mt-1">{{ listing.address }}</p>

            <div class="mt-6 space-y-3">
              <button
                v-if="authStore.isAuthenticated && listing.created_by !== authStore.user?.id"
                @click="contactHost"
                class="w-full bg-primary-500 text-white py-3 rounded-lg font-medium hover:bg-primary-600 transition"
              >
                Message Host
              </button>
              <template v-if="authStore.isAuthenticated && listing.created_by === authStore.user?.id">
                <button @click="deleteListing" class="w-full bg-red-50 text-red-600 py-3 rounded-lg font-medium hover:bg-red-100 transition">
                  Delete Listing
                </button>
              </template>
              <router-link v-if="!authStore.isAuthenticated" to="/login" class="block text-center w-full bg-primary-500 text-white py-3 rounded-lg font-medium hover:bg-primary-600 transition">
                Log in to Contact
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </template>
    <div v-else class="text-center py-16 text-gray-400">Listing not found.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { listings as listingsApi, conversations as convoApi } from '../api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const listing = ref(null)
const loading = ref(true)

function formatDate(d) {
  return d ? new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) : ''
}

async function contactHost() {
  try {
    const { data } = await convoApi.create({ item: null, members: [listing.value.created_by, authStore.user.id] })
    router.push(`/inbox/${data.id}`)
  } catch {
    alert('Could not start conversation.')
  }
}

async function deleteListing() {
  if (!confirm('Are you sure you want to delete this listing?')) return
  try {
    await listingsApi.delete(listing.value.id)
    router.push('/dashboard')
  } catch {
    alert('Failed to delete listing.')
  }
}

onMounted(async () => {
  try {
    const { data } = await listingsApi.get(route.params.id)
    listing.value = data
  } catch {
    listing.value = null
  } finally {
    loading.value = false
  }
})
</script>
