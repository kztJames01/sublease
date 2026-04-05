<template>
  <div class="auth-shell">
    <div
      v-motion
      :initial="{ opacity: 0, y: 30, scale: 0.97 }"
      :enter="{ opacity: 1, y: 0, scale: 1, transition: { duration: 700 } }"
      class="auth-card"
    >
      <!-- Left panel - hero image -->
      <div class="auth-hero">
        <div class="flex items-center justify-between z-10">
          <span class="text-primary-fg text-xl font-display font-bold tracking-wide">lvSpace</span>
          <router-link to="/" class="text-xs text-primary-fg/85 border border-primary-fg/30 rounded-full px-3 py-1.5 hover:bg-primary-fg/10 transition">
            Back to website &rarr;
          </router-link>
        </div>
        <img
          src="https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&q=80"
          alt="Hero"
          class="absolute inset-0 w-full h-full object-cover rounded-2xl opacity-20"
        />
        <div class="relative z-10">
          <h2 class="text-primary-fg text-2xl font-display leading-tight mb-6">
            Find Your Perfect<br />Sublease Today
          </h2>
          <div class="flex gap-2">
            <span class="w-6 h-1.5 bg-primary-fg/40 rounded-full"></span>
            <span class="w-8 h-1.5 bg-primary-fg rounded-full"></span>
            <span class="w-6 h-1.5 bg-primary-fg/40 rounded-full"></span>
          </div>
        </div>
      </div>

      <!-- Right panel - reset form -->
      <div class="flex-1 p-8 md:p-10 flex flex-col justify-center">
        <h1 class="text-text-dark text-3xl font-display font-bold mb-1">Reset password</h1>
        <p class="text-text-dark/70 text-sm mb-8">
          Remember your password?
          <router-link to="/login" class="text-primary-bg hover:text-primary-bg/80 underline">Log in</router-link>
        </p>

        <form v-if="!sent" @submit.prevent="handleReset" class="space-y-4">
          <div v-if="error" class="error-box">
            {{ error }}
          </div>

          <p class="text-text-dark/70 text-sm">
            Enter your email address and we'll send you a link to reset your password.
          </p>

          <div>
            <input
              v-model="email"
              type="email"
              placeholder="Email"
              required
              class="auth-input"
            />
          </div>

          <button
            type="submit"
            :disabled="submitting"
            class="btn-primary"
          >
            {{ submitting ? 'Sending...' : 'Send reset link' }}
          </button>
        </form>

        <div v-else class="text-center space-y-4">
          <div class="w-16 h-16 mx-auto bg-primary-bg/10 rounded-full flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-primary-bg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>
          <p class="text-primary-bg font-medium text-lg">Email sent!</p>
          <p class="text-text-dark/70 text-sm">Check your inbox for the reset link.</p>
          <router-link to="/login" class="inline-block text-primary-bg hover:text-primary-bg/80 font-medium mt-2">
            Back to Login
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { auth } from '../api'

const email = ref('')
const error = ref('')
const submitting = ref(false)
const sent = ref(false)

async function handleReset() {
  error.value = ''
  submitting.value = true
  try {
    await auth.resetPassword(email.value)
    sent.value = true
  } catch (e) {
    error.value = e.response?.data?.error || 'Failed to send reset email.'
  } finally {
    submitting.value = false
  }
}
</script>
