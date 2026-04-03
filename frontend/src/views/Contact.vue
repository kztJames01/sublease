<template>
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-display font-bold text-text-dark mb-4">Contact Us</h1>
    <p class="text-text-muted mb-8">Have questions or feedback? Reach out and we'll get back to you.</p>
    <form @submit.prevent="handleSubmit" class="bg-surface rounded-2xl shadow-sm p-8 space-y-5 border border-border">
      <div v-if="sent" class="bg-success/10 text-success text-sm p-3 rounded-lg border border-success/20">Message sent! We'll be in touch.</div>
      <div>
        <label class="block text-sm font-medium text-text-muted mb-1">Name</label>
        <input v-model="form.name" type="text" required class="w-full px-4 py-2.5 border border-border rounded-lg bg-surface text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-muted mb-1">Email</label>
        <input v-model="form.email" type="email" required class="w-full px-4 py-2.5 border border-border rounded-lg bg-surface text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-muted mb-1">Message</label>
        <textarea v-model="form.message" rows="5" required class="w-full px-4 py-2.5 border border-border rounded-lg bg-surface text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35"></textarea>
      </div>
      <button type="submit" class="bg-primary-bg text-primary-fg px-6 py-2.5 rounded-lg font-medium hover:bg-primary-bg/90 transition">Send Message</button>
    </form>
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
