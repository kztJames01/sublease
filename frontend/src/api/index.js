import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,
})

api.interceptors.request.use((config) => {
  const csrfToken = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
    ?.split('=')[1]
  if (csrfToken) config.headers['X-CSRFToken'] = csrfToken
  return config
})

export const auth = {
  csrf: () => api.get('/auth/csrf/'),
  login: (credentials) => api.post('/auth/login/', credentials),
  signup: (data) => api.post('/auth/signup/', data),
  logout: () => api.post('/auth/logout/'),
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
}

export const apartmentListings = {
  list: (params) => api.get('/apartment-listings/', { params }),
  get: (id) => api.get(`/apartment-listings/${id}/`),
  create: (data) => api.post('/apartment-listings/', data),
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
}

export const messages = {
  list: (params) => api.get('/conversation-messages/', { params }),
  send: (data) => api.post('/conversation-messages/', data),
}

export default api
