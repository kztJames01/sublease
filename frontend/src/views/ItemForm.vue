<template>
  <div class="min-h-screen bg-page">
    <!-- Top bar: back + help -->
    <div :class="scrolled ? 'bg-primary-bg/95 backdrop-blur shadow-lg' : 'bg-transparent'"
      class="fixed top-0 left-0 right-0 z-50 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
        <button @click="goBack"
          class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back to Dashboard
        </button>
        <button @click="showHelp = !showHelp"
          class="flex items-center gap-2 text-white hover:text-orange transition text-sm font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Help
        </button>
      </div>
    </div>

    <Transition enter-active-class="transition duration-200" enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150"
      leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="showHelp"
        class="fixed top-14 right-4 z-50 w-80 bg-white rounded-2xl shadow-2xl border border-border p-5">
        <h3 class="font-semibold text-text-dark mb-2">Need help?</h3>
        <p class="text-sm text-text-muted leading-relaxed">Choose "Individual Sublease" to list your own place, or
          "Apartment Complex" to register a property management listing. Visit our <router-link to="/faq"
            class="text-orange hover:underline">FAQ</router-link> for more info.</p>
      </div>
    </Transition>

    <!-- Dark hero -->
    <div class="relative bg-gradient-to-r from-[#0a1628] via-primary-bg to-[#1a3a6b] pt-20 pb-10 px-4 sm:px-6 lg:px-8">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="relative max-w-2xl mx-auto">
        <span class="text-sm font-semibold text-orange uppercase tracking-widest">{{ isEdit ? 'Edit' : 'New' }}</span>
        <h1 class="text-3xl lg:text-4xl font-display font-bold text-white mt-1">{{ isEdit ? 'Edit Item' : 'Create Item' }}</h1>
      </div>
    </div>

    <!-- Form -->
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 relative z-10 pb-16">
      <form
        @submit.prevent="handleSubmit"
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
        class="bg-white rounded-3xl shadow-xl p-8 space-y-5 border border-border/50"
      >
        <div v-if="error" class="bg-destructive/8 text-destructive text-sm rounded-xl px-4 py-3 border border-destructive/15">{{ error }}</div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Category</label>
          <select v-model="form.category" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
            <option value="" disabled>Select category</option>
            <option v-for="cat in cats" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Name</label>
          <input v-model="form.name" type="text" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Price</label>
          <input v-model.number="form.price" type="number" min="0" step="0.01" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Description</label>
          <textarea v-model="form.description" rows="4" class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition"></textarea>
        </div>
        <div>
          <label class="block text-sm font-medium text-text-muted mb-1.5">Image</label>
          <input type="file" accept="image/*" @change="form.image = $event.target.files[0]" class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
        </div>
        <div v-if="isEdit" class="flex items-center gap-2">
          <input v-model="form.is_sold" type="checkbox" id="is_sold" class="rounded border-border text-primary-bg focus:ring-primary-bg/35" />
          <label for="is_sold" class="text-sm text-text-muted">Mark as sold</label>
        </div>
        <button type="submit" :disabled="submitting" class="w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20 disabled:opacity-50">
          {{ submitting ? 'Saving...' : (isEdit ? 'Save Changes' : 'Create Item') }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { items as itemsApi, categories } from '../api'

const route = useRoute()
const router = useRouter()
const isEdit = computed(() => !!route.params.id && route.name === 'edit-item')
const error = ref('')
const submitting = ref(false)
const showHelp = ref(false)
const cats = ref([])
const form = reactive({ category: '', name: '', price: 0, description: '', image: null, is_sold: false })
const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 20
}


function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/dashboard')
}

onMounted(async () => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
  try {
    const { data } = await categories.list()
    cats.value = Array.isArray(data) ? data : data.results || []
  } catch { /* silent */ }

  if (isEdit.value) {
    try {
      const { data } = await itemsApi.get(route.params.id)
      Object.assign(form, { category: data.category, name: data.name, price: data.price, description: data.description || '', is_sold: data.is_sold })
    } catch {
      error.value = 'Failed to load item.'
    }
  }
})
onUnmounted(async() => {
  window.removeEventListener('scroll', onScroll)
})
async function handleSubmit() {
  error.value = ''
  submitting.value = true
  try {
    const fd = new FormData()
    fd.append('category', form.category)
    fd.append('name', form.name)
    fd.append('price', form.price)
    fd.append('description', form.description)
    if (form.image) fd.append('image', form.image)
    if (isEdit.value) fd.append('is_sold', form.is_sold)

    if (isEdit.value) {
      await itemsApi.update(route.params.id, fd)
      router.push(`/items/${route.params.id}`)
    } else {
      const { data } = await itemsApi.create(fd)
      router.push(`/items/${data.id}`)
    }
  } catch (e) {
    error.value = typeof e.response?.data === 'object' ? Object.values(e.response.data).flat().join(' ') : 'Failed to save.'
  } finally {
    submitting.value = false
  }
}
</script>
