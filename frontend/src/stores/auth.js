import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { auth, apartmentListings } from '../api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const loading = ref(true)
  const providers = ref([])
  const apartmentPortalApproved = ref(false)

  const isAuthenticated = computed(() => !!user.value)

  async function fetchUser() {
    try {
      await auth.refresh()
      const { data } = await auth.getUser()
      user.value = data
      await fetchApartmentPortalApproval()
    } catch {
      user.value = null
      apartmentPortalApproved.value = false
    } finally {
      loading.value = false
    }
  }

  async function fetchApartmentPortalApproval() {
    if (!user.value) {
      apartmentPortalApproved.value = false
      return false
    }
    try {
      await apartmentListings.portalAccess()
      apartmentPortalApproved.value = true
    } catch {
      apartmentPortalApproved.value = false
    }
    return apartmentPortalApproved.value
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
    const { data } = await auth.login(credentials)
    user.value = data.user
    await fetchApartmentPortalApproval()
    return data
  }

  async function signup(formData) {
    const { data } = await auth.signup(formData)
    user.value = data.user
    apartmentPortalApproved.value = false
    return data
  }

  async function logout() {
    await auth.logout()
    user.value = null
    apartmentPortalApproved.value = false
  }

  function oauthLogin(providerId) {
    window.location.href = `/accounts/${providerId}/login/?process=login`
  }

  return {
    user,
    loading,
    providers,
    apartmentPortalApproved,
    isAuthenticated,
    fetchUser,
    fetchProviders,
    login,
    signup,
    logout,
    oauthLogin,
    fetchApartmentPortalApproval,
  }
})
