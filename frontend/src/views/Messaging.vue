<template>
    <div>
        <section class="relative pt-16 overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
            <div
                class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
            <div class="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-page to-transparent" />
            <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 flex items-center justify-between pb-16">
                <div v-motion :initial="{ opacity: 0, y: 20 }"
                    :enter="{ opacity: 1, y: 0, transition: { duration: 600 } }">
                    <span class="text-sm font-semibold text-orange uppercase tracking-widest">Inbox</span>
                    <h1 class="text-4xl lg:text-5xl font-display font-bold text-white mt-2">Messages</h1>
                </div>
                <span class="text-sm text-white/50">{{ conversations.length }} conversations</span>
            </div>
        </section>
        <div class="h-screen flex relative flex-col overflow-hidden">
            <!-- Main content -->
            <div class="flex flex-1 overflow-hidden">
                <!-- Mobile overlay -->
                <div v-if="sidebarOpen" class="fixed inset-0 bg-black/40 z-30 lg:hidden" @click="sidebarOpen = false" />

                <!-- Left sidebar: conversation list -->
                <aside :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'"
                    class="fixed lg:static inset-y-0 left-0 z-40 w-80 lg:w-[22rem] shrink-0 bg-surface border-r border-border flex flex-col transition-transform duration-200">
                    <!-- Conversation list -->
                    <div class="flex-1 overflow-y-auto p-2 space-y-1">
                        <div v-if="loadingList" class="text-center py-12 text-text-soft text-sm">Loading...</div>
                        <div v-else-if="!conversations.length" class="text-center py-12 text-text-soft text-sm">No
                            conversations yet.</div>
                        <button v-else v-for="c in conversations" :key="c.id" type="button"
                            @click="selectConversation(c.id)" :class="c.id === activeConversationId
                                ? 'bg-primary-bg text-white border-primary-bg'
                                : 'bg-transparent border-transparent hover:bg-surface-alt'"
                            class="w-full text-left rounded-2xl border p-3 transition group">
                            <div class="flex items-start gap-3">
                                <div
                                    class="w-10 h-10 rounded-xl bg-orange text-primary-bg font-bold text-xs flex items-center justify-center shrink-0">
                                    {{ c.other_member?.initials || 'DM' }}
                                </div>
                                <div class="min-w-0 flex-1">
                                    <div class="flex items-baseline justify-between gap-2">
                                        <p :class="c.id === activeConversationId ? 'text-white' : 'text-text-dark'"
                                            class="font-semibold text-sm truncate">
                                            {{ c.other_member?.display_name || `Conversation #${c.id}` }}
                                        </p>
                                        <span
                                            :class="c.id === activeConversationId ? 'text-white/60' : 'text-text-soft'"
                                            class="text-[10px] shrink-0">
                                            {{ formatShortDate(c.modified_at) }}
                                        </span>
                                    </div>
                                    <p :class="c.id === activeConversationId ? 'text-white/70' : 'text-text-muted'"
                                        class="text-xs mt-0.5 truncate">
                                        {{ c.latest_message?.content || 'No messages yet.' }}
                                    </p>
                                    <div v-if="c.is_potential_client || c.is_reported" class="flex gap-1 mt-1.5">
                                        <span v-if="c.is_potential_client"
                                            :class="c.id === activeConversationId ? 'bg-white/20 text-white' : 'bg-primary-bg/10 text-primary-bg'"
                                            class="text-[10px] px-2 py-0.5 rounded-full font-medium">Client</span>
                                        <span v-if="c.is_reported"
                                            :class="c.id === activeConversationId ? 'bg-white/20 text-white' : 'bg-orange/12 text-orange'"
                                            class="text-[10px] px-2 py-0.5 rounded-full font-medium">Reported</span>
                                    </div>
                                </div>
                            </div>
                        </button>
                    </div>
                </aside>

                <!-- Right panel: active conversation -->
                <main class="flex-1 flex flex-col min-w-0 bg-white">
                    <!-- No conversation selected -->
                    <div v-if="!activeConversationId"
                        class="flex-1 flex flex-col items-center justify-center text-text-soft gap-3">
                        <button type="button"
                            class="lg:hidden mb-4 px-4 py-2 rounded-xl border border-border text-sm text-text-muted hover:bg-surface-alt transition"
                            @click="sidebarOpen = true">
                            Open Inbox
                        </button>
                        <svg class="w-16 h-16 text-border" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                        <p class="text-sm">Select a conversation to get started</p>
                    </div>

                    <!-- Conversation loaded -->
                    <template v-else-if="convo">
                        <!-- Chat header -->
                        <header
                            class="px-4 sm:px-6 lg:px-8 py-3 border-b border-border bg-white flex items-center gap-3 shrink-0">
                            <button type="button"
                                class="lg:hidden p-2 -ml-2 rounded-xl text-text-muted hover:bg-surface-alt transition"
                                @click="sidebarOpen = true">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 6h16M4 12h16M4 18h16" />
                                </svg>
                            </button>

                            <div
                                class="w-10 h-10 rounded-xl bg-orange text-primary-bg font-bold text-xs flex items-center justify-center shrink-0">
                                {{ activeMember?.initials || 'DM' }}
                            </div>
                            <div class="min-w-0 flex-1">
                                <h2 class="font-semibold text-text-dark truncate">{{ activeMember?.display_name ||
                                    'Conversation' }}</h2>
                                <p class="text-xs text-text-soft truncate">{{ activeMember?.email || '' }}</p>
                            </div>

                            <!-- Action buttons -->
                            <div class="flex items-center gap-1.5 shrink-0">
                                <button type="button"
                                    class="px-3 py-1.5 rounded-lg border border-border text-xs text-text-muted hover:border-primary-bg/20 hover:text-primary-bg transition hidden sm:inline-flex"
                                    @click="togglePotentialClient">
                                    {{ convo.is_potential_client ? 'Unflag Client' : 'Flag Potential Client' }}
                                </button>
                                <button type="button"
                                    class="px-3 py-1.5 rounded-lg border border-orange/30 text-xs text-orange hover:bg-orange/8 transition hidden sm:inline-flex"
                                    @click="reportConversation">
                                    {{ convo.is_reported ? 'Reported' : 'Report' }}
                                </button>
                                <button type="button"
                                    class="px-3 py-1.5 rounded-lg border border-destructive/30 text-xs text-destructive hover:bg-destructive/8 transition hidden sm:inline-flex"
                                    @click="deleteConversation">
                                    Delete
                                </button>
                                <!-- Mobile dropdown -->
                                <div class="relative sm:hidden">
                                    <button type="button"
                                        class="p-2 rounded-xl text-text-muted hover:bg-surface-alt transition"
                                        @click="mobileMenuOpen = !mobileMenuOpen">
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M12 5v.01M12 12v.01M12 19v.01" />
                                        </svg>
                                    </button>
                                    <div v-if="mobileMenuOpen"
                                        class="absolute right-0 top-full mt-1 w-48 bg-white border border-border rounded-xl shadow-lg z-50 py-1">
                                        <button type="button"
                                            class="w-full text-left px-4 py-2.5 text-sm text-text-dark hover:bg-surface-alt"
                                            @click="togglePotentialClient(); mobileMenuOpen = false">
                                            {{ convo.is_potential_client ? 'Unflag Client' : 'Flag Potential Client' }}
                                        </button>
                                        <button type="button"
                                            class="w-full text-left px-4 py-2.5 text-sm text-orange hover:bg-surface-alt"
                                            @click="reportConversation(); mobileMenuOpen = false">
                                            {{ convo.is_reported ? 'Reported' : 'Report User' }}
                                        </button>
                                        <button type="button"
                                            class="w-full text-left px-4 py-2.5 text-sm text-destructive hover:bg-surface-alt"
                                            @click="deleteConversation(); mobileMenuOpen = false">
                                            Delete Conversation
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </header>

                        <!-- Messages area -->
                        <div ref="messagesContainer" class="flex-1 overflow-y-auto px-4 sm:px-6 lg:px-8 py-4">
                            <div v-if="!msgList.length"
                                class="flex items-center justify-center h-full text-text-soft text-sm">
                                No messages yet. Start the conversation.
                            </div>
                            <div v-else class="space-y-3 max-w-3xl mx-auto">
                                <div v-for="msg in msgList" :key="msg.id"
                                    :class="isOwnMessage(msg) ? 'justify-end' : 'justify-start'" class="flex">
                                    <div class="max-w-[75%] flex flex-col"
                                        :class="isOwnMessage(msg) ? 'items-end' : 'items-start'">
                                        <p v-if="!isOwnMessage(msg)" class="text-[11px] text-text-soft mb-1 px-1">
                                            {{ msg.author?.display_name }}
                                        </p>
                                        <div :class="isOwnMessage(msg)
                                            ? 'bg-orange text-primary-bg rounded-2xl rounded-br-sm'
                                            : 'bg-primary-bg text-primary-fg rounded-2xl rounded-bl-sm'"
                                            class="px-4 py-2.5 shadow-sm">
                                            <p v-if="msg.content" class="text-sm leading-relaxed whitespace-pre-line">{{
                                                msg.content }}</p>

                                            <template v-if="msg.attachment_url">
                                                <img v-if="msg.attachment_kind === 'image'" :src="msg.attachment_url"
                                                    :alt="msg.attachment_name || 'Attachment'"
                                                    class="mt-2 rounded-lg max-h-52 w-auto object-cover" />
                                                <video v-else-if="msg.attachment_kind === 'video'"
                                                    :src="msg.attachment_url" controls
                                                    class="mt-2 rounded-lg max-h-52 w-full" />
                                                <a v-else :href="msg.attachment_url" target="_blank" rel="noreferrer"
                                                    class="mt-2 inline-flex items-center gap-1 text-xs underline underline-offset-2">
                                                    {{ msg.attachment_name || 'Open attachment' }}
                                                </a>
                                            </template>
                                        </div>
                                        <div class="flex items-center gap-2 mt-1 px-1">
                                            <span :class="isOwnMessage(msg) ? 'text-text-soft' : 'text-text-soft'"
                                                class="text-[10px]">
                                                {{ formatDate(msg.edited_at || msg.created_at) }}<span
                                                    v-if="msg.edited_at"> · edited</span>
                                            </span>
                                            <button v-if="msg.can_edit" type="button"
                                                class="text-[10px] text-primary-bg hover:text-primary-bg/80 font-medium transition"
                                                @click="startEditing(msg)">
                                                Edit
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Compose bar -->
                        <footer class="px-4 sm:px-6 lg:px-8 py-3 border-t border-border bg-white shrink-0">
                            <div v-if="editingMessageId"
                                class="mb-2 flex items-center justify-between rounded-xl bg-orange/8 px-3 py-2 text-sm">
                                <span class="text-text-muted">Editing message</span>
                                <button type="button" class="text-orange text-xs font-medium"
                                    @click="cancelEditing">Cancel</button>
                            </div>

                            <div v-if="attachmentName"
                                class="mb-2 flex items-center justify-between rounded-xl bg-surface-alt px-3 py-2 text-sm">
                                <span class="text-text-muted truncate">{{ attachmentName }}</span>
                                <button type="button" class="text-orange text-xs font-medium"
                                    @click="clearAttachment">Remove</button>
                            </div>

                            <form @submit.prevent="sendMessage" class="flex items-center gap-2">
                                <input ref="fileInput" type="file" class="hidden" @change="handleAttachment" />
                                <button type="button"
                                    class="shrink-0 p-2.5 rounded-xl border border-border text-text-muted hover:text-primary-bg hover:border-primary-bg/20 transition"
                                    title="Attach file" @click="openAttachmentPicker">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                                    </svg>
                                </button>
                                <input v-model="newMessage" type="text" placeholder="Type a message..."
                                    class="flex-1 px-4 py-2.5 rounded-xl border border-border bg-white text-text-dark text-sm placeholder:text-text-soft focus:outline-none focus:ring-2 focus:ring-primary-bg/20" />
                                <button type="submit" :disabled="sending || (!newMessage.trim() && !attachmentFile)"
                                    class="shrink-0 px-5 py-2.5 rounded-xl bg-primary-bg text-primary-fg text-sm font-semibold hover:bg-primary-bg/90 transition disabled:opacity-40">
                                    {{ sending ? '...' : editingMessageId ? 'Save' : 'Send' }}
                                </button>
                            </form>
                        </footer>
                    </template>

                    <!-- Loading state for conversation -->
                    <div v-else-if="loadingConvo"
                        class="flex-1 flex items-center justify-center text-text-soft text-sm">
                        Loading conversation...
                    </div>
                </main>

                <!-- Close mobile menu on outside click -->
                <div v-if="mobileMenuOpen" class="fixed inset-0 z-40" @click="mobileMenuOpen = false" />
            </div>
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
const loadingList = ref(true)
const loadingConvo = ref(false)
const sending = ref(false)
const editingMessageId = ref(null)
const attachmentFile = ref(null)
const attachmentName = ref('')
const messagesContainer = ref(null)
const fileInput = ref(null)
const sidebarOpen = ref(false)
const mobileMenuOpen = ref(false)

const activeConversationId = computed(() => route.params.id ? Number(route.params.id) : null)
const activeMember = computed(() => convo.value?.other_member || null)

function formatDate(d) {
    if (!d) return ''
    return new Date(d).toLocaleString(undefined, { month: 'numeric', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' })
}

function formatShortDate(d) {
    if (!d) return ''
    const date = new Date(d)
    const now = new Date()
    const diffDays = Math.floor((now - date) / 86400000)
    if (diffDays === 0) return date.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' })
    if (diffDays < 7) return date.toLocaleDateString(undefined, { weekday: 'short' })
    return date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })
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
    try {
        const { data } = await convoApi.list()
        conversations.value = Array.isArray(data) ? data : data.results || []
    } catch {
        conversations.value = []
    } finally {
        loadingList.value = false
    }
}

async function loadActiveConversation() {
    if (!route.params.id) {
        convo.value = null
        msgList.value = []
        return
    }
    loadingConvo.value = true
    try {
        const { data } = await convoApi.get(route.params.id)
        convo.value = data
        const messagesResponse = await msgApi.list({ conversation: route.params.id })
        const all = Array.isArray(messagesResponse.data) ? messagesResponse.data : messagesResponse.data.results || []
        msgList.value = all.filter((m) => String(m.conversation) === String(route.params.id))
        scrollToBottom()
    } catch {
        convo.value = null
        msgList.value = []
    } finally {
        loadingConvo.value = false
    }
}

function selectConversation(id) {
    if (Number(id) === activeConversationId.value) return
    sidebarOpen.value = false
    router.push(`/inbox/${id}`)
}

function openAttachmentPicker() { fileInput.value?.click() }

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
        const item = conversations.value.find((c) => c.id === convo.value.id)
        if (item) item.is_potential_client = data.is_potential_client
    } catch { alert('Failed to update.') }
}

async function reportConversation() {
    if (!convo.value) return
    try {
        const { data } = await convoApi.report(convo.value.id)
        convo.value.is_reported = data.is_reported
        const item = conversations.value.find((c) => c.id === convo.value.id)
        if (item) item.is_reported = data.is_reported
    } catch { alert('Failed to update.') }
}

async function deleteConversation() {
    if (!convo.value) return
    if (!confirm(`Delete conversation with ${activeMember.value?.display_name || 'this user'}?`)) return
    try {
        await convoApi.delete(convo.value.id)
        conversations.value = conversations.value.filter((c) => c.id !== convo.value.id)
        convo.value = null
        msgList.value = []
        if (conversations.value.length) {
            router.replace(`/inbox/${conversations.value[0].id}`)
        } else {
            router.replace('/inbox')
        }
    } catch { alert('Failed to delete.') }
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

watch(
    () => route.params.id,
    async (newId, oldId) => {
        if (newId !== oldId) {
            await loadActiveConversation()
        }
    },
)

onMounted(async () => {
    await loadConversations()
    if (route.params.id) {
        await loadActiveConversation()
    }
})
</script>
