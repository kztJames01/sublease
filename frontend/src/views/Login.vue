<template>
  <div class="auth-shell">
    <div class="auth-card">
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
            <span class="w-8 h-1.5 bg-primary-fg rounded-full"></span>
            <span class="w-6 h-1.5 bg-primary-fg/40 rounded-full"></span>
            <span class="w-6 h-1.5 bg-primary-fg/40 rounded-full"></span>
          </div>
        </div>
      </div>

      <!-- Right panel - login form -->
      <div class="flex-1 p-8 md:p-10 flex flex-col justify-center">
        <h1 class="text-text-dark text-3xl font-display font-bold mb-1">Welcome back</h1>
        <p class="text-text-dark/70 text-sm mb-8">
          Don't have an account?
          <router-link to="/signup" class="text-primary-bg hover:text-primary-bg/80 underline">Sign up</router-link>
        </p>

        <form @submit.prevent="handleLogin" class="space-y-4">
          <div v-if="error" class="error-box">
            {{ error }}
          </div>

          <div>
            <input
              v-model="form.username"
              type="text"
              placeholder="Username or email"
              required
              class="auth-input"
            />
          </div>

          <div class="relative">
            <input
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Enter your password"
              required
              class="auth-input pr-12"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-3 top-1/2 -translate-y-1/2 text-text-dark/50 hover:text-text-dark/80"
            >
              <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M3 3l18 18" />
              </svg>
            </button>
          </div>

          <div class="flex justify-end">
            <router-link to="/password-reset" class="text-primary-bg hover:text-primary-bg/80 text-sm">
              Forgot password?
            </router-link>
          </div>

          <button
            type="submit"
            :disabled="submitting"
            class="btn-primary"
          >
            {{ submitting ? 'Logging in...' : 'Log in' }}
          </button>
        </form>

        <!-- OAuth divider -->
        <div class="flex items-center gap-4 my-6">
          <div class="flex-1 h-px bg-border"></div>
          <span class="text-text-dark/55 text-xs">Or continue with</span>
          <div class="flex-1 h-px bg-border"></div>
        </div>

        <!-- OAuth buttons -->
        <div class="grid grid-cols-2 gap-3">
          <button
            @click="authStore.oauthLogin('google')"
            class="btn-outline"
          >
            <svg class="w-5 h-5" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18A11.96 11.96 0 001 12c0 1.94.46 3.77 1.18 5.07l3.66-2.84V14.09z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            Google
          </button>
          <button
            @click="authStore.oauthLogin('apple')"
            class="btn-outline"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M17.05 20.28c-.98.95-2.05.88-3.08.4-1.09-.5-2.08-.48-3.24 0-1.44.62-2.2.44-3.06-.4C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
            </svg>
            Apple
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()

const form = reactive({ username: '', password: '' })
const error = ref('')
const submitting = ref(false)
const showPassword = ref(false)

onMounted(() => {
  authStore.fetchProviders()
})

async function handleLogin() {
  error.value = ''
  submitting.value = true
  try {
    await authStore.login(form)
    router.push(route.query.redirect || '/')
  } catch (e) {
    error.value = e.response?.data?.error || 'Invalid credentials. Please try again.'
  } finally {
    submitting.value = false
  }
}
</script>
