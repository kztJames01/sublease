<template>
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-8">{{ isEdit ? 'Edit Item' : 'New Item' }}</h1>
    <form @submit.prevent="handleSubmit" class="bg-white rounded-2xl shadow-sm p-8 space-y-5">
      <div v-if="error" class="bg-red-50 text-red-600 text-sm p-3 rounded-lg">{{ error }}</div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Category</label>
        <select v-model="form.category" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300">
          <option value="" disabled>Select category</option>
          <option v-for="cat in cats" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
        <input v-model="form.name" type="text" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Price</label>
        <input v-model.number="form.price" type="number" min="0" step="0.01" required class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
        <textarea v-model="form.description" rows="4" class="w-full px-4 py-2.5 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-300"></textarea>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Image</label>
        <input type="file" accept="image/*" @change="form.image = $event.target.files[0]" class="w-full text-sm" />
      </div>
      <div v-if="isEdit" class="flex items-center gap-2">
        <input v-model="form.is_sold" type="checkbox" id="is_sold" class="rounded text-primary-500" />
        <label for="is_sold" class="text-sm text-gray-700">Mark as sold</label>
      </div>
      <button type="submit" :disabled="submitting" class="w-full bg-primary-500 text-white py-3 rounded-lg font-medium hover:bg-primary-600 transition disabled:opacity-50">
        {{ submitting ? 'Saving...' : (isEdit ? 'Save Changes' : 'Create Item') }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { items as itemsApi, categories } from '../api'

const route = useRoute()
const router = useRouter()
const isEdit = computed(() => !!route.params.id && route.name === 'edit-item')
const error = ref('')
const submitting = ref(false)
const cats = ref([])
const form = reactive({ category: '', name: '', price: 0, description: '', image: null, is_sold: false })

onMounted(async () => {
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
