<template>
  <div class="min-h-screen bg-page">
    <section class="relative pt-16 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-24">
        <span class="text-sm font-semibold text-orange uppercase tracking-widest">Approved Management</span>
        <h1 class="text-4xl lg:text-5xl font-display font-bold text-white mt-2">Apartment Portal</h1>
        <p class="text-white/80 mt-3 max-w-3xl">Bulk list apartment units and manage your available inventory with your own photos and videos.</p>
      </div>
    </section>

    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-14 relative z-10 pb-16 space-y-8">
      <div v-if="portalLoading" class="bg-white rounded-2xl border border-border p-6 text-text-muted shadow-sm">Loading portal...</div>
      <div v-else-if="accessError" class="bg-destructive/8 text-destructive rounded-2xl border border-destructive/20 p-6 shadow-sm">{{ accessError }}</div>
      <template v-else>
        <div class="bg-white rounded-3xl shadow-xl border border-border/60 p-6 sm:p-8">
          <div class="flex flex-wrap items-center justify-between gap-3">
            <div>
              <h2 class="text-2xl font-display font-bold text-text-dark">{{ portal?.company }}</h2>
              <p class="text-sm text-text-soft">Approved apartment account</p>
            </div>
            <span class="inline-flex items-center px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold border border-emerald-200">Approved</span>
          </div>
        </div>

        <div class="grid grid-cols-1 xl:grid-cols-5 gap-6">
          <div class="xl:col-span-2 bg-white rounded-3xl shadow-xl border border-border/60 p-6 sm:p-8">
            <h3 class="text-xl font-display font-bold text-text-dark">{{ editingId ? 'Edit Unit' : 'Add Unit' }}</h3>
            <p class="text-sm text-text-soft mt-1">Add as many units as needed. Each submit creates one listing.</p>

            <div v-if="formError" class="mt-4 bg-destructive/8 text-destructive text-sm rounded-xl px-4 py-3 border border-destructive/20">{{ formError }}</div>

            <form class="mt-5 space-y-4" @submit.prevent="saveUnit">
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Unit Title</label>
                <input v-model.trim="form.title" type="text" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Unit Code</label>
                <input v-model.trim="form.unit_code" type="text" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-text-muted mb-1.5">Bedrooms</label>
                  <input v-model.number="form.bedrooms" type="number" min="0" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-text-muted mb-1.5">Bathrooms</label>
                  <input v-model.number="form.bathrooms" type="number" min="0" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Price ($/month)</label>
                <input v-model.number="form.price" type="number" min="0" step="0.01" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Unit Website</label>
                <input v-model.trim="form.website_url" type="url" required placeholder="https://example.com/unit" class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Description</label>
                <textarea v-model.trim="form.description" rows="4" required class="w-full px-4 py-3 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Cover Image</label>
                <input type="file" accept="image/*" :required="!editingId" @change="onCoverChange" class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Gallery Images (optional)</label>
                <input type="file" accept="image/*" multiple @change="onGalleryChange" class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
              </div>
              <div>
                <label class="block text-sm font-medium text-text-muted mb-1.5">Video (optional)</label>
                <input type="file" accept="video/*" @change="onVideoChange" class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-4 file:py-2.5 file:text-sm file:font-medium file:text-white" />
              </div>
              <div class="flex gap-3 pt-1">
                <button type="submit" :disabled="saving" class="flex-1 bg-primary-bg text-white py-3 rounded-xl font-semibold hover:bg-primary-bg/90 transition disabled:opacity-50">
                  {{ saving ? 'Saving...' : (editingId ? 'Update Unit' : 'Add Unit') }}
                </button>
                <button v-if="editingId" type="button" @click="resetForm" class="px-4 py-3 rounded-xl border border-border text-text-muted hover:text-text-dark transition">Cancel</button>
              </div>
            </form>
          </div>

          <div class="xl:col-span-3 bg-white rounded-3xl shadow-xl border border-border/60 p-6 sm:p-8">
            <div class="flex items-center justify-between mb-5">
              <h3 class="text-xl font-display font-bold text-text-dark">Your Units</h3>
              <span class="text-sm text-text-soft">{{ units.length }} total</span>
            </div>
            <div v-if="!units.length" class="text-text-soft border border-dashed border-border rounded-2xl p-6">No units yet. Use the form to add your first unit.</div>
            <div v-else class="space-y-4">
              <article v-for="unit in units" :key="unit.id" class="border border-border rounded-2xl p-4 sm:p-5 shadow-sm bg-white">
                <div class="flex flex-col sm:flex-row sm:items-start gap-4">
                  <img :src="unit.cover_image || '/placeholder.jpg'" alt="" class="w-full sm:w-36 h-28 rounded-xl object-cover border border-border" />
                  <div class="flex-1 min-w-0">
                    <div class="flex flex-wrap items-center justify-between gap-2">
                      <h4 class="font-semibold text-text-dark truncate">{{ unit.title }}</h4>
                      <span :class="unit.is_active ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-slate-100 text-slate-600 border-slate-200'" class="text-xs font-semibold px-2.5 py-1 rounded-full border">
                        {{ unit.is_active ? 'Active' : 'Inactive' }}
                      </span>
                    </div>
                    <p class="text-sm text-text-soft mt-1">{{ unit.unit_code }} • {{ unit.bedrooms }} bed • {{ unit.bathrooms }} bath</p>
                    <p class="text-sm text-orange font-semibold mt-1">${{ Number(unit.price).toLocaleString() }}/month</p>
                    <p class="text-sm text-text-muted mt-2 line-clamp-2">{{ unit.description }}</p>
                    <div class="mt-3 flex flex-wrap gap-2">
                      <button type="button" @click="beginEdit(unit)" class="px-3 py-1.5 rounded-lg border border-border text-text-muted hover:text-text-dark transition">Edit</button>
                      <button type="button" @click="toggleUnitStatus(unit)" class="px-3 py-1.5 rounded-lg border border-border text-text-muted hover:text-text-dark transition">
                        {{ unit.is_active ? 'Set Inactive' : 'Set Active' }}
                      </button>
                      <button type="button" @click="deleteUnit(unit.id)" class="px-3 py-1.5 rounded-lg border border-destructive/30 text-destructive hover:bg-destructive/5 transition">Delete</button>
                    </div>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
      </template>
    </section>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import { apartmentListings, apartmentUnits } from '../api'

const portalLoading = ref(true)
const accessError = ref('')
const formError = ref('')
const saving = ref(false)
const editingId = ref(null)
const portal = ref(null)
const units = ref([])

const form = reactive({
  title: '',
  unit_code: '',
  bedrooms: 1,
  bathrooms: 1,
  price: 0,
  website_url: '',
  description: '',
  cover_image: null,
  gallery: [],
  video: null,
})

function resetForm() {
  editingId.value = null
  form.title = ''
  form.unit_code = ''
  form.bedrooms = 1
  form.bathrooms = 1
  form.price = 0
  form.website_url = ''
  form.description = ''
  form.cover_image = null
  form.gallery = []
  form.video = null
  formError.value = ''
}

function onCoverChange(event) {
  form.cover_image = event.target.files?.[0] || null
}

function onGalleryChange(event) {
  form.gallery = [...(event.target.files || [])]
}

function onVideoChange(event) {
  form.video = event.target.files?.[0] || null
}

function buildFormData() {
  const fd = new FormData()
  fd.append('title', form.title)
  fd.append('unit_code', form.unit_code)
  fd.append('bedrooms', String(form.bedrooms))
  fd.append('bathrooms', String(form.bathrooms))
  fd.append('price', String(form.price))
  fd.append('website_url', form.website_url)
  fd.append('description', form.description)
  if (form.cover_image) fd.append('cover_image', form.cover_image)
  if (form.video) fd.append('video', form.video)
  for (const image of form.gallery) {
    fd.append('gallery_images', image)
  }
  return fd
}

function parseError(error, fallback) {
  if (typeof error?.response?.data === 'object') {
    return Object.values(error.response.data).flat().join(' ')
  }
  return fallback
}

async function loadPortal() {
  portalLoading.value = true
  accessError.value = ''
  try {
    const [portalRes, unitsRes] = await Promise.all([
      apartmentListings.portalAccess(),
      apartmentUnits.list(),
    ])
    portal.value = portalRes.data
    units.value = Array.isArray(unitsRes.data) ? unitsRes.data : unitsRes.data.results || []
  } catch {
    accessError.value = 'Only approved apartment listers can access this portal.'
  } finally {
    portalLoading.value = false
  }
}

async function saveUnit() {
  saving.value = true
  formError.value = ''
  try {
    const payload = buildFormData()
    if (editingId.value) {
      await apartmentUnits.update(editingId.value, payload)
    } else {
      await apartmentUnits.create(payload)
    }
    await loadPortal()
    resetForm()
  } catch (error) {
    formError.value = parseError(error, 'Failed to save unit.')
  } finally {
    saving.value = false
  }
}

function beginEdit(unit) {
  editingId.value = unit.id
  form.title = unit.title || ''
  form.unit_code = unit.unit_code || ''
  form.bedrooms = unit.bedrooms ?? 1
  form.bathrooms = unit.bathrooms ?? 1
  form.price = unit.price ?? 0
  form.website_url = unit.website_url || ''
  form.description = unit.description || ''
  form.cover_image = null
  form.gallery = []
  form.video = null
  formError.value = ''
}

async function toggleUnitStatus(unit) {
  try {
    await apartmentUnits.update(unit.id, { is_active: !unit.is_active })
    await loadPortal()
  } catch (error) {
    formError.value = parseError(error, 'Failed to update unit status.')
  }
}

async function deleteUnit(unitId) {
  try {
    await apartmentUnits.delete(unitId)
    if (editingId.value === unitId) {
      resetForm()
    }
    await loadPortal()
  } catch (error) {
    formError.value = parseError(error, 'Failed to delete unit.')
  }
}

onMounted(loadPortal)
</script>
