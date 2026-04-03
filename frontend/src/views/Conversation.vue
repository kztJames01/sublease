<template>
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <router-link to="/inbox" class="text-primary-bg hover:text-primary-bg/80 text-sm font-medium mb-4 inline-block">← Back to Inbox</router-link>
    <h1 class="text-2xl font-display font-bold text-text-dark mb-6">Conversation</h1>

    <div v-if="loading" class="text-center py-16 text-text-soft">Loading...</div>
    <template v-else>
      <!-- Messages -->
      <div class="bg-surface rounded-2xl shadow-sm p-6 mb-4 space-y-4 max-h-[500px] overflow-y-auto border border-border" ref="messagesContainer">
        <div v-if="!msgList.length" class="text-center text-text-soft py-8">No messages yet. Start the conversation!</div>
        <div
          v-for="msg in msgList"
          :key="msg.id"
          :class="msg.created_by === authStore.user?.id ? 'ml-auto bg-primary-bg/10 border border-primary-bg/15' : 'mr-auto bg-surface-alt border border-border'"
          class="max-w-[75%] rounded-xl p-4"
        >
          <p class="text-sm text-text-dark">{{ msg.content }}</p>
          <p class="text-xs text-text-soft mt-1">{{ formatTime(msg.created_at) }}</p>
        </div>
      </div>

      <!-- Send Message -->
      <form @submit.prevent="sendMessage" class="flex gap-3">
        <input
          v-model="newMessage"
          type="text"
          placeholder="Type a message..."
          required
          class="flex-1 px-4 py-3 border border-border rounded-xl bg-surface text-text-dark placeholder:text-text-soft focus:outline-none focus:ring-2 focus:ring-primary-bg/35"
        />
        <button type="submit" :disabled="sending" class="bg-primary-bg text-primary-fg px-6 py-3 rounded-xl font-medium hover:bg-primary-bg/90 transition disabled:opacity-50">
          Send
        </button>
      </form>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { messages as msgApi } from '../api'

const route = useRoute()
const authStore = useAuthStore()
const msgList = ref([])
const newMessage = ref('')
const loading = ref(true)
const sending = ref(false)
const messagesContainer = ref(null)

function formatTime(d) {
  return d ? new Date(d).toLocaleString() : ''
}

function scrollToBottom() {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

async function loadMessages() {
  try {
    const { data } = await msgApi.list({ conversation: route.params.id })
    const all = Array.isArray(data) ? data : data.results || []
    msgList.value = all.filter(m => String(m.conversation) === String(route.params.id))
    scrollToBottom()
  } catch {
    msgList.value = []
  }
}

async function sendMessage() {
  if (!newMessage.value.trim()) return
  sending.value = true
  try {
    await msgApi.send({ conversation: parseInt(route.params.id), content: newMessage.value })
    newMessage.value = ''
    await loadMessages()
  } catch {
    alert('Failed to send message.')
  } finally {
    sending.value = false
  }
}

onMounted(async () => {
  await loadMessages()
  loading.value = false
})
</script>
