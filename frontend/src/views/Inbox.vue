<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-6">Inbox</h1>
    <div v-if="loading" class="text-center py-16 text-gray-400">Loading...</div>
    <div v-else-if="convos.length" class="space-y-3">
      <router-link
        v-for="convo in convos"
        :key="convo.id"
        :to="`/inbox/${convo.id}`"
        class="block bg-white rounded-xl shadow-sm p-5 hover:shadow-md transition"
      >
        <div class="flex items-center justify-between">
          <div>
            <p class="font-semibold text-gray-900">Conversation #{{ convo.id }}</p>
            <p class="text-sm text-gray-500 mt-0.5">{{ convo.members?.length || 0 }} members</p>
          </div>
          <span class="text-xs text-gray-400">{{ formatDate(convo.modified_at) }}</span>
        </div>
      </router-link>
    </div>
    <div v-else class="text-center py-16 text-gray-400">No conversations yet.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { conversations as convoApi } from '../api'

const convos = ref([])
const loading = ref(true)

function formatDate(d) {
  return d ? new Date(d).toLocaleDateString() : ''
}

onMounted(async () => {
  try {
    const { data } = await convoApi.list()
    convos.value = Array.isArray(data) ? data : data.results || []
  } catch {
    convos.value = []
  } finally {
    loading.value = false
  }
})
</script>
