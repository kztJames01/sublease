<template>
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <router-link to="/inbox" class="inline-flex lg:hidden text-primary-bg hover:text-primary-bg/80 text-sm font-medium mb-4">
      ← Back to Inbox
    </router-link>

    <div v-if="loading" class="text-center py-16 text-text-soft">Loading...</div>
    <div v-else class="grid lg:grid-cols-12 gap-6 items-start">
      <aside class="lg:col-span-4 bg-surface border border-border rounded-[1.75rem] shadow-[0_18px_50px_rgba(20,33,61,0.08)] overflow-hidden">
        <div class="px-5 py-5 border-b border-border bg-surface">
          <div class="flex items-end justify-between gap-4">
            <div>
              <p class="text-xs uppercase tracking-[0.18em] text-text-soft">Inbox</p>
              <h1 class="text-2xl font-display font-bold text-text-dark mt-1">Messages</h1>
            </div>
            <p class="text-sm text-text-soft">{{ conversations.length }} threads</p>
          </div>
        </div>

        <div class="max-h-[42rem] overflow-y-auto p-3 space-y-2 bg-white">
          <button
            v-for="conversation in conversations"
            :key="conversation.id"
            type="button"
            @click="selectConversation(conversation.id)"
            :class="conversation.id === activeConversationId
              ? 'bg-surface-alt border-primary-bg/18 shadow-[0_12px_28px_rgba(20,33,61,0.08)]'
              : 'bg-white border-border hover:border-primary-bg/12 hover:bg-surface-alt/40'"
            class="w-full text-left rounded-2xl border p-4 transition"
          >
            <div class="flex items-start gap-3">
              <div class="w-11 h-11 rounded-2xl bg-orange text-primary-bg font-bold text-sm flex items-center justify-center shrink-0">
                {{ conversation.other_member?.initials || 'DM' }}
              </div>
              <div class="min-w-0 flex-1">
                <div class="flex items-start justify-between gap-3">
                  <div class="min-w-0">
                    <p class="font-semibold text-text-dark truncate">
                      {{ conversation.other_member?.display_name || `Conversation #${conversation.id}` }}
                    </p>
                    <p class="text-xs text-text-soft mt-0.5 truncate">
                      {{ conversation.other_member?.email || 'Private conversation' }}
                    </p>
                  </div>
                  <span class="text-[11px] text-text-soft shrink-0">
                    {{ formatDate(conversation.modified_at, { month: 'short', day: 'numeric' }) }}
                  </span>
                </div>
                <p class="text-sm text-text-muted mt-2 truncate">
                  {{ conversation.latest_message?.content || 'No messages yet.' }}
                </p>
                <div class="flex items-center gap-2 mt-3 flex-wrap">
                  <span
                    v-if="conversation.is_potential_client"
                    class="inline-flex items-center rounded-full bg-primary-bg/8 text-primary-bg text-[11px] font-medium px-2.5 py-1"
                  >
                    Potential Client
                  </span>
                  <span
                    v-if="conversation.is_reported"
                    class="inline-flex items-center rounded-full bg-orange/12 text-orange text-[11px] font-medium px-2.5 py-1"
                  >
                    Reported
                  </span>
                </div>
              </div>
            </div>
          </button>
        </div>
      </aside>

      <section class="lg:col-span-8 bg-surface border border-border rounded-[1.75rem] shadow-[0_22px_60px_rgba(20,33,61,0.1)] overflow-hidden">
        <template v-if="convo">
          <header class="px-6 py-5 border-b border-border bg-white">
            <div class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-4">
              <div class="flex items-center gap-4 min-w-0">
                <div class="w-14 h-14 rounded-2xl bg-orange text-primary-bg font-bold text-base flex items-center justify-center shrink-0">
                  {{ activeMember?.initials || 'DM' }}
                </div>
                <div class="min-w-0">
                  <h2 class="text-2xl font-display font-bold text-text-dark truncate">
                    {{ activeMember?.display_name || 'Conversation' }}
                  </h2>
                  <p class="text-sm text-text-soft truncate">{{ activeMember?.email || 'Private conversation' }}</p>
                </div>
              </div>

              <div class="flex flex-wrap gap-2">
                <button
                  type="button"
                  class="px-4 py-2.5 rounded-xl border border-border bg-white text-text-muted text-sm hover:border-primary-bg/16 hover:text-primary-bg transition"
                  @click="togglePotentialClient"
                >
                  {{ convo.is_potential_client ? 'Unflag Client' : 'Flag Potential Client' }}
                </button>
                <button
                  type="button"
                  class="px-4 py-2.5 rounded-xl border border-orange/30 bg-orange/8 text-orange text-sm hover:bg-orange/14 transition"
                  @click="reportConversation"
                >
                  {{ convo.is_reported ? 'Reported' : 'Report User' }}
                </button>
              </div>
            </div>
          </header>

          <div
            ref="messagesContainer"
            class="bg-white px-6 py-6 h-[32rem] overflow-y-auto"
          >
            <div v-if="!msgList.length" class="text-center text-text-soft py-20">No messages yet. Start the conversation.</div>
            <div v-else class="space-y-5">
              <div
                v-for="msg in msgList"
                :key="msg.id"
                :class="isOwnMessage(msg) ? 'items-end' : 'items-start'"
                class="flex flex-col"
              >
                <p v-if="!isOwnMessage(msg)" class="text-xs text-text-soft mb-1.5 px-1">
                  {{ msg.author?.display_name }}
                </p>

                <div
                  :class="isOwnMessage(msg)
                    ? 'bg-orange text-primary-bg border-orange/55 rounded-[1.45rem] rounded-br-md'
                    : 'bg-primary-bg text-primary-fg border-primary-bg/25 rounded-[1.45rem] rounded-bl-md'"
                  class="max-w-[75%] border px-4 py-3 shadow-sm"
                >
                  <p v-if="msg.content" class="text-sm leading-6 whitespace-pre-line">{{ msg.content }}</p>

                  <template v-if="msg.attachment_url">
                    <img
                      v-if="msg.attachment_kind === 'image'"
                      :src="msg.attachment_url"
                      :alt="msg.attachment_name || 'Attachment'"
                      class="mt-3 rounded-xl max-h-64 w-auto object-cover border border-white/20"
                    />
                    <video
                      v-else-if="msg.attachment_kind === 'video'"
                      :src="msg.attachment_url"
                      controls
                      class="mt-3 rounded-xl max-h-64 w-full border border-white/20"
                    />
                    <a
                      v-else
                      :href="msg.attachment_url"
                      target="_blank"
                      rel="noreferrer"
                      class="mt-3 inline-flex items-center gap-2 text-sm underline underline-offset-2"
                    >
                      {{ msg.attachment_name || 'Open attachment' }}
                    </a>
                  </template>

                  <div class="flex items-center justify-between gap-3 mt-3">
                    <p :class="isOwnMessage(msg) ? 'text-primary-bg/72' : 'text-primary-fg/60'" class="text-xs">
                      {{ formatDate(msg.edited_at || msg.created_at, dateTimeFormat) }}<span v-if="msg.edited_at"> · edited</span>
                    </p>
                    <button
                      v-if="msg.can_edit"
                      type="button"
                      :class="isOwnMessage(msg) ? 'text-primary-bg/86 hover:text-primary-bg' : 'text-primary-fg/80 hover:text-primary-fg'"
                      class="text-xs font-medium transition"
                      @click="startEditing(msg)"
                    >
                      Edit
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <footer class="px-6 py-5 border-t border-border bg-white">
            <div
              v-if="editingMessageId"
              class="mb-3 flex items-center justify-between gap-4 rounded-2xl border border-orange/20 bg-orange/6 px-4 py-3"
            >
              <p class="text-sm text-text-muted">Editing your latest message</p>
              <button type="button" class="text-sm text-orange hover:text-orange/85 transition" @click="cancelEditing">Cancel</button>
            </div>

            <div
              v-if="attachmentName"
              class="mb-3 flex items-center justify-between gap-4 rounded-2xl border border-border bg-surface-alt/50 px-4 py-3"
            >
              <p class="text-sm text-text-muted truncate">{{ attachmentName }}</p>
              <button type="button" class="text-sm text-orange hover:text-orange/85 transition" @click="clearAttachment">Remove</button>
            </div>

            <form @submit.prevent="sendMessage" class="flex items-center gap-3">
              <input ref="fileInput" type="file" class="hidden" @change="handleAttachment" />
              <button
                type="button"
                class="shrink-0 px-4 py-3 rounded-2xl border border-border bg-white text-text-dark hover:border-primary-bg/16 hover:text-primary-bg transition"
                @click="openAttachmentPicker"
              >
                Attach
              </button>
              <input
                v-model="newMessage"
                type="text"
                placeholder="Type a message..."
                class="flex-1 px-4 py-3 rounded-2xl border border-border bg-white text-text-dark placeholder:text-text-soft focus:outline-none focus:ring-2 focus:ring-primary-bg/20"
              />
              <button
                type="submit"
                :disabled="sending || (!newMessage.trim() && !attachmentFile)"
                class="shrink-0 px-6 py-3 rounded-2xl bg-primary-bg text-primary-fg font-semibold hover:bg-primary-bg/92 transition disabled:opacity-50"
              >
                {{ sending ? 'Sending...' : editingMessageId ? 'Save' : 'Send' }}
              </button>
            </form>
          </footer>
        </template>

        <div v-else class="h-[32rem] flex items-center justify-center text-text-soft bg-white">
          Select a conversation to get started.
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { computed, nextTick, ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { conversations as convoApi, messages as msgApi } from '../api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const conversations = ref([])
const convo = ref(null)
const msgList = ref([])
const newMessage = ref('')
const loading = ref(true)
const sending = ref(false)
const editingMessageId = ref(null)
const attachmentFile = ref(null)
const attachmentName = ref('')
const messagesContainer = ref(null)
const fileInput = ref(null)

const dateTimeFormat = {
  month: 'numeric',
  day: 'numeric',
  year: 'numeric',
  hour: 'numeric',
  minute: '2-digit',
}

const activeConversationId = computed(() => Number(route.params.id))
const activeMember = computed(() => convo.value?.other_member || null)

function formatDate(d, options = {}) {
  return d ? new Date(d).toLocaleString(undefined, options) : ''
}

function isOwnMessage(msg) {
  return msg.created_by === authStore.user?.id
}

function scrollToBottom() {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

async function loadConversations() {
  const { data } = await convoApi.list()
  conversations.value = Array.isArray(data) ? data : data.results || []
}

async function loadActiveConversation() {
  if (!route.params.id) {
    convo.value = null
    msgList.value = []
    return
  }

  const { data } = await convoApi.get(route.params.id)
  convo.value = data

  const messagesResponse = await msgApi.list({ conversation: route.params.id })
  const all = Array.isArray(messagesResponse.data) ? messagesResponse.data : messagesResponse.data.results || []
  msgList.value = all.filter((m) => String(m.conversation) === String(route.params.id))
  scrollToBottom()
}

function selectConversation(id) {
  if (Number(id) === activeConversationId.value) return
  router.push(`/inbox/${id}`)
}

function openAttachmentPicker() {
  fileInput.value?.click()
}

function handleAttachment(event) {
  attachmentFile.value = event.target.files?.[0] || null
  attachmentName.value = attachmentFile.value?.name || ''
}

function clearAttachment() {
  attachmentFile.value = null
  attachmentName.value = ''
  if (fileInput.value) fileInput.value.value = ''
}

function startEditing(msg) {
  editingMessageId.value = msg.id
  newMessage.value = msg.content || ''
  clearAttachment()
}

function cancelEditing() {
  editingMessageId.value = null
  newMessage.value = ''
  clearAttachment()
}

async function togglePotentialClient() {
  if (!convo.value) return
  try {
    const { data } = await convoApi.togglePotentialClient(convo.value.id)
    convo.value.is_potential_client = data.is_potential_client
    const item = conversations.value.find((conversation) => conversation.id === convo.value.id)
    if (item) item.is_potential_client = data.is_potential_client
  } catch {
    alert('Failed to update potential client state.')
  }
}

async function reportConversation() {
  if (!convo.value) return
  try {
    const { data } = await convoApi.report(convo.value.id)
    convo.value.is_reported = data.is_reported
    const item = conversations.value.find((conversation) => conversation.id === convo.value.id)
    if (item) item.is_reported = data.is_reported
  } catch {
    alert('Failed to update report state.')
  }
}

async function sendMessage() {
  if (!newMessage.value.trim() && !attachmentFile.value) return

  sending.value = true
  try {
    const fd = new FormData()
    fd.append('conversation', parseInt(route.params.id, 10))
    if (newMessage.value.trim()) fd.append('content', newMessage.value)
    if (attachmentFile.value) fd.append('attachment', attachmentFile.value)

    if (editingMessageId.value) {
      await msgApi.update(editingMessageId.value, fd)
    } else {
      await msgApi.send(fd)
    }

    cancelEditing()
    await Promise.all([loadConversations(), loadActiveConversation()])
  } catch (error) {
    alert(error.response?.data?.detail || error.response?.data?.non_field_errors?.[0] || 'Failed to save message.')
  } finally {
    sending.value = false
  }
}

async function initialize() {
  loading.value = true
  try {
    await loadConversations()
    if (!route.params.id && conversations.value.length) {
      await router.replace(`/inbox/${conversations.value[0].id}`)
      return
    }
    await loadActiveConversation()
  } catch {
    conversations.value = []
    convo.value = null
    msgList.value = []
  } finally {
    loading.value = false
  }
}

watch(
  () => route.params.id,
  async (newId, oldId) => {
    if (newId && newId !== oldId) {
      await initialize()
    }
  },
)

onMounted(initialize)
</script>
