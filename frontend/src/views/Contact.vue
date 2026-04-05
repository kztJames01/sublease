<template>
  <div>
    <!-- Hero banner -->
    <section class="relative pt-16 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_50%_at_30%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
      <div class="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-20 text-center">
        <span
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
          class="text-sm font-semibold text-orange uppercase tracking-widest"
        >Get in touch</span>
        <h1
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: 100, duration: 600 } }"
          class="text-4xl lg:text-5xl font-display font-bold text-white mt-3"
        >Contact Us</h1>
        <p
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: 250, duration: 500 } }"
          class="text-white/60 mt-3 text-lg"
        >Have questions or feedback? We'd love to hear from you.</p>
      </div>
    </section>

    <section class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8 relative z-10 pb-16">
      <form
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0, transition: { delay: 300, duration: 500 } }"
        @submit.prevent="handleSubmit"
        class="bg-surface rounded-3xl shadow-xl p-8 sm:p-10 space-y-5 border border-border"
      >
        <div v-if="sent" class="bg-success/10 text-success text-sm p-4 rounded-xl border border-success/20 flex items-center gap-2">
          <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
          Message sent! We'll be in touch.
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Name</label>
          <input v-model="form.name" type="text" required class="w-full px-4 py-3 border border-border rounded-xl bg-surface text-text-dark text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Email</label>
          <input v-model="form.email" type="email" required class="w-full px-4 py-3 border border-border rounded-xl bg-surface text-text-dark text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Message</label>
          <textarea v-model="form.message" rows="5" required class="w-full px-4 py-3 border border-border rounded-xl bg-surface text-text-dark text-sm focus:outline-none focus:ring-2 focus:ring-primary-bg/20 transition resize-none"></textarea>
        </div>
        <button type="submit" class="w-full bg-primary-bg text-primary-fg px-6 py-3 rounded-xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/10">
          Send Message
        </button>
      </form>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
const form = reactive({ name: '', email: '', message: '' })
const sent = ref(false)
function handleSubmit() {
  sent.value = true
  Object.assign(form, { name: '', email: '', message: '' })
}
</script>
