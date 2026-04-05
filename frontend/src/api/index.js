import axios from 'axios'

let accessToken = null
let refreshRequest = null

export function setAccessToken(token) {
  accessToken = token || null
}

export function clearAccessToken() {
  accessToken = null
}

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,
})

api.interceptors.request.use((config) => {
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`
  }
  return config
})

async function refreshAccessToken() {
  if (!refreshRequest) {
    refreshRequest = api.post('/auth/refresh/')
      .then(({ data }) => {
        setAccessToken(data.accessToken)
        return data.accessToken
      })
      .catch((error) => {
        clearAccessToken()
        throw error
      })
      .finally(() => {
        refreshRequest = null
      })
  }
  return refreshRequest
}

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config || {}
    const status = error.response?.status

    if (
      status === 401 &&
      !originalRequest._retry &&
      !originalRequest.url?.includes('/auth/login/') &&
      !originalRequest.url?.includes('/auth/signup/') &&
      !originalRequest.url?.includes('/auth/refresh/')
    ) {
      originalRequest._retry = true
      try {
        const token = await refreshAccessToken()
        originalRequest.headers = originalRequest.headers || {}
        originalRequest.headers.Authorization = `Bearer ${token}`
        return api(originalRequest)
      } catch {
        clearAccessToken()
      }
    }

    return Promise.reject(error)
  },
)

export const auth = {
  csrf: () => Promise.resolve({ data: { detail: 'JWT authentication enabled.' } }),
  login: async (credentials) => {
    const response = await api.post('/auth/login/', credentials)
    setAccessToken(response.data.accessToken)
    return response
  },
  signup: async (data) => {
    const response = await api.post('/auth/signup/', data)
    setAccessToken(response.data.accessToken)
    return response
  },
  refresh: refreshAccessToken,
  logout: async () => {
    try {
      await api.post('/auth/logout/')
    } finally {
      clearAccessToken()
    }
  },
  getUser: () => api.get('/auth/user/'),
  resetPassword: (email) => api.post('/auth/password-reset/', { email }),
  getProviders: () => api.get('/auth/providers/'),
}

export const listings = {
  list: (params) => api.get('/individual-listings/', { params }),
  get: (id) => api.get(`/individual-listings/${id}/`),
  create: (data) =>
    api.post('/individual-listings/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  update: (id, data) =>
    api.put(`/individual-listings/${id}/`, data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  delete: (id) => api.delete(`/individual-listings/${id}/`),
  trackClick: (id, data) => api.post(`/individual-listings/${id}/track_click/`, data),
  trackInquiry: (id) => api.post(`/individual-listings/${id}/track_inquiry/`),
  toggleLike: (id) => api.post(`/individual-listings/${id}/toggle_like/`),
}

export const apartmentListings = {
  list: (params) => api.get('/apartment-listings/', { params }),
  get: (id) => api.get(`/apartment-listings/${id}/`),
  create: (data) => api.post('/apartment-listings/', data),
  portalAccess: () => api.get('/apartment-listings/portal_access/'),
}

export const apartmentUnits = {
  list: (params) => api.get('/apartment-units/', { params }),
  create: (data) =>
    api.post('/apartment-units/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  update: (id, data) => {
    const isFormData = typeof FormData !== 'undefined' && data instanceof FormData
    return api.patch(
      `/apartment-units/${id}/`,
      data,
      isFormData ? { headers: { 'Content-Type': 'multipart/form-data' } } : undefined,
    )
  },
  delete: (id) => api.delete(`/apartment-units/${id}/`),
}

export const propertyTypes = { list: () => api.get('/property-types/') }
export const amenities = { list: () => api.get('/amenities/') }

export const items = {
  list: (params) => api.get('/items/', { params }),
  get: (id) => api.get(`/items/${id}/`),
  create: (data) =>
    api.post('/items/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  update: (id, data) =>
    api.put(`/items/${id}/`, data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  delete: (id) => api.delete(`/items/${id}/`),
}

export const categories = { list: () => api.get('/categories/') }

export const conversations = {
  list: () => api.get('/conversations/'),
  get: (id) => api.get(`/conversations/${id}/`),
  create: (data) => api.post('/conversations/', data),
  delete: (id) => api.delete(`/conversations/${id}/`),
  report: (id) => api.post(`/conversations/${id}/report/`),
  togglePotentialClient: (id) => api.post(`/conversations/${id}/toggle_potential_client/`),
}

export const messages = {
  list: (params) => api.get('/conversation-messages/', { params }),
  send: (data) =>
    api.post('/conversation-messages/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  update: (id, data) =>
    api.patch(`/conversation-messages/${id}/`, data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
}

export default api
