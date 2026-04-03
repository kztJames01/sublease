<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div v-if="loading" class="text-center py-16 text-text-soft">Loading...</div>
    <template v-else-if="item">
      <div class="grid lg:grid-cols-2 gap-8">
        <img :src="item.image || '/placeholder.jpg'" :alt="item.name" class="w-full rounded-2xl object-cover h-[400px]" />
        <div class="space-y-4">
          <h1 class="text-3xl font-display font-bold text-text-dark">{{ item.name }}</h1>
          <p class="text-3xl font-bold text-primary-bg">${{ item.price }}</p>
          <p v-if="item.description" class="text-text-muted leading-relaxed">{{ item.description }}</p>
          <p class="text-sm text-text-soft">Listed {{ formatDate(item.created_at) }}</p>
          <div v-if="isOwner" class="flex gap-3">
            <router-link :to="`/items/${item.id}/edit`" class="bg-primary-bg text-primary-fg px-5 py-2.5 rounded-lg font-medium hover:bg-primary-bg/90 transition">Edit</router-link>
            <button @click="deleteItem" class="bg-destructive/10 text-destructive px-5 py-2.5 rounded-lg font-medium hover:bg-destructive/15 transition border border-destructive/15">Delete</button>
          </div>
        </div>
      </div>
    </template>
    <div v-else class="text-center py-16 text-text-soft">Item not found.</div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { items as itemsApi } from '../api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const item = ref(null)
const loading = ref(true)
const isOwner = computed(() => item.value?.created_by === authStore.user?.id)

function formatDate(d) {
  return d ? new Date(d).toLocaleDateString() : ''
}

async function deleteItem() {
  if (!confirm('Delete this item?')) return
  try {
    await itemsApi.delete(item.value.id)
    router.push('/dashboard')
  } catch {
    alert('Failed to delete.')
  }
}

onMounted(async () => {
  try {
    const { data } = await itemsApi.get(route.params.id)
    item.value = data
  } catch {
    item.value = null
  } finally {
    loading.value = false
  }
})
</script>
