import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { auth } from '../api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const loading = ref(true)
  const providers = ref([])

  const isAuthenticated = computed(() => !!user.value)

  async function fetchUser() {
    try {
      await auth.csrf()
      const { data } = await auth.getUser()
      user.value = data
    } catch {
      user.value = null
    } finally {
      loading.value = false
    }
  }

  async function fetchProviders() {
    try {
      const { data } = await auth.getProviders()
      providers.value = data.providers
    } catch {
      providers.value = []
    }
  }

  async function login(credentials) {
    await auth.csrf()
    const { data } = await auth.login(credentials)
    user.value = data.user
    return data
  }

  async function signup(formData) {
    await auth.csrf()
    const { data } = await auth.signup(formData)
    user.value = data.user
    return data
  }

  async function logout() {
    await auth.logout()
    user.value = null
  }

  function oauthLogin(providerId) {
    window.location.href = `/accounts/${providerId}/login/?process=login`
  }

  return {
    user,
    loading,
    providers,
    isAuthenticated,
    fetchUser,
    fetchProviders,
    login,
    signup,
    logout,
    oauthLogin,
  }
})
