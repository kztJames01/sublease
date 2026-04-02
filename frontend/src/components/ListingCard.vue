<template>
  <div class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition group">
    <div class="relative">
      <img :src="listing.images || '/placeholder.jpg'" :alt="listing.title" class="w-full h-48 object-cover group-hover:scale-105 transition duration-300" />
      <span class="absolute top-3 left-3 bg-primary-bg text-primary-fg text-xs font-medium px-2 py-1 rounded-full">
        {{ listing.property_type_name || 'Sublease' }}
      </span>
      <button @click.prevent="toggleSave" class="absolute top-3 right-3 p-1.5 bg-white/80 rounded-full hover:bg-white transition">
        <svg class="w-5 h-5" :class="saved ? 'text-destructive fill-current' : 'text-text-dark/45'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </button>
    </div>
    <div class="p-4">
      <h3 class="font-semibold text-text-dark truncate">{{ listing.title }}</h3>
      <p class="text-sm text-text-dark/70 mt-1 truncate">{{ listing.address }}</p>
      <div class="flex items-center gap-3 mt-2 text-sm text-text-dark/75">
        <span>{{ listing.bedrooms }} bed</span>
        <span>·</span>
        <span>{{ listing.bathrooms }} bath</span>
      </div>
      <div class="flex items-center justify-between mt-3">
        <span class="text-lg font-bold text-primary-bg">${{ listing.price }}<span class="text-sm font-normal text-text-dark/55">/mo</span></span>
        <router-link :to="`/listings/${listing.id}`" class="text-sm text-primary-bg hover:text-primary-bg/80 font-medium">View →</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ listing: { type: Object, required: true } })
const saved = ref(props.listing.is_saved || false)

function toggleSave() {
  saved.value = !saved.value
}
</script>