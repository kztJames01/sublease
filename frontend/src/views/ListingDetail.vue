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

    <!-- Help panel -->
    <Transition enter-active-class="transition duration-200" enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150"
      leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="showHelp"
        class="fixed top-14 right-4 z-50 w-80 bg-white rounded-2xl shadow-2xl border border-border p-5">
        <h3 class="font-semibold text-text-dark mb-2">Need help?</h3>
        <p class="text-sm text-text-muted leading-relaxed">If you have questions about this listing, use the "Message
          Host" button to contact the owner directly. For platform issues, visit our <router-link to="/contact"
            class="text-orange hover:underline">Contact</router-link> page or <router-link to="/faq"
            class="text-orange hover:underline">FAQ</router-link>.</p>
      </div>
    </Transition>

    <div>
      <div v-if="loading" class="flex items-center justify-center min-h-[60vh]">
        <div class="w-8 h-8 border-2 border-orange border-t-transparent rounded-full animate-spin" />
      </div>

      <template v-else-if="listing">
        <!-- Image Carousel -->
        <div class="relative bg-primary-bg">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-6">
            <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
            <div
              class="absolute inset-0 bg-[radial-gradient(ellipse_50%_40%_at_20%_-10%,rgba(252,163,17,0.1),transparent)]" />
            <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
            <div class="absolute top-20 right-[10%] w-72 h-72 rounded-full bg-orange/10 blur-3xl" />
            <div class="absolute bottom-20 left-[5%] w-96 h-96 rounded-full bg-primary-bg/40 blur-3xl" />
            <div class="relative overflow-hidden rounded-2xl">
              <div class="flex gap-4 overflow-x-auto snap-x snap-mandatory scroll-smooth pb-2 no-scrollbar"
                ref="carouselRef">
                <div v-for="(img, i) in allImages" :key="i"
                  class="snap-start shrink-0 w-full sm:w-[calc(50%-0.5rem)] lg:w-[calc(33.333%-0.67rem)] rounded-2xl overflow-hidden">
                  <img :src="img" :alt="`${listing.title} photo ${i + 1}`"
                    class="w-full h-[320px] object-cover hover:scale-105 transition-transform duration-500" />
                </div>
              </div>
              <!-- Carousel controls -->
              <button v-if="allImages.length > 1" @click="scrollCarousel(-1)"
                class="absolute left-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/90 backdrop-blur shadow-lg flex items-center justify-center hover:bg-white transition z-10">
                <svg class="w-5 h-5 text-text-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                </svg>
              </button>
              <button v-if="allImages.length > 1" @click="scrollCarousel(1)"
                class="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/90 backdrop-blur shadow-lg flex items-center justify-center hover:bg-white transition z-10">
                <svg class="w-5 h-5 text-text-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>

            </div>
            <!-- Image counter -->
            <div class="flex items-center justify-center gap-1.5 mt-4">
              <span v-for="(_, i) in allImages" :key="i" class="w-2 h-2 rounded-full transition"
                :class="i === activeImageIndex ? 'bg-orange' : 'bg-white/30'" />
            </div>
          </div>
        </div>

        <!-- Content -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Stats bar -->
          <div v-motion :initial="{ opacity: 0, y: 20 }" :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
            class="grid grid-cols-2 sm:grid-cols-4 gap-4 -mt-16 relative z-10 mb-10">
            <div class="bg-white rounded-2xl shadow-lg border border-border/50 p-5 text-center">
              <div class="w-10 h-10 mx-auto mb-2 rounded-xl bg-orange/10 flex items-center justify-center">
                <svg class="w-5 h-5 text-orange" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" />
                </svg>
              </div>
              <p class="text-2xl font-bold text-text-dark">{{ listing.likes_count || 0 }}</p>
              <p class="text-xs text-text-muted mt-0.5">Likes</p>
            </div>
            <div class="bg-white rounded-2xl shadow-lg border border-border/50 p-5 text-center">
              <div class="w-10 h-10 mx-auto mb-2 rounded-xl bg-primary-bg/10 flex items-center justify-center">
                <svg class="w-5 h-5 text-primary-bg" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </div>
              <p class="text-2xl font-bold text-text-dark">{{ listing.clicks_count || 0 }}</p>
              <p class="text-xs text-text-muted mt-0.5">Views</p>
            </div>
            <div class="bg-white rounded-2xl shadow-lg border border-border/50 p-5 text-center">
              <div class="w-10 h-10 mx-auto mb-2 rounded-xl bg-green-500/10 flex items-center justify-center">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
              </div>
              <p class="text-2xl font-bold text-text-dark">{{ listing.inquiries_count || 0 }}</p>
              <p class="text-xs text-text-muted mt-0.5">Inquiries</p>
            </div>
            <div class="bg-white rounded-2xl shadow-lg border border-border/50 p-5 text-center">
              <div class="w-10 h-10 mx-auto mb-2 rounded-xl flex items-center justify-center"
                :class="listing.offer_status === 'accepting' ? 'bg-green-500/10' : listing.offer_status === 'pending' ? 'bg-yellow-500/10' : 'bg-red-500/10'">
                <svg class="w-5 h-5"
                  :class="listing.offer_status === 'accepting' ? 'text-green-500' : listing.offer_status === 'pending' ? 'text-yellow-500' : 'text-red-500'"
                  fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <p class="text-lg font-bold text-text-dark capitalize">{{ offerStatusLabel }}</p>
              <p class="text-xs text-text-muted mt-0.5">Status</p>
            </div>
          </div>

          <div class="grid lg:grid-cols-3 gap-10">
            <!-- Main details -->
            <div class="lg:col-span-2 space-y-8">
              <div v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 100, duration: 500 } }">
                <div class="flex items-start justify-between gap-4">
                  <div>
                    <span class="inline-block px-3 py-1 rounded-full text-xs font-medium bg-primary-bg text-white mb-3">
                      {{ listing.property_type_name || 'Sublease' }}
                    </span>
                    <h1 class="text-3xl lg:text-4xl font-display font-bold text-text-dark">{{ listing.title }}</h1>
                    <p class="text-text-muted mt-1 flex items-center gap-1.5">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                      </svg>
                      {{ listing.address }}
                    </p>
                  </div>
                  <button v-if="!isOwner" @click="handleLike"
                    class="shrink-0 w-12 h-12 rounded-2xl border border-border hover:border-orange/30 hover:bg-orange/5 flex items-center justify-center transition group">
                    <svg class="w-6 h-6 text-text-muted group-hover:text-orange transition" fill="none"
                      stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- Property specs -->
              <div v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 200, duration: 500 } }"
                class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div class="bg-surface rounded-2xl p-4 text-center border border-border">
                  <p class="text-2xl font-bold text-text-dark">{{ listing.bedrooms }}</p>
                  <p class="text-xs text-text-muted mt-0.5">Bedrooms · {{ listing.bedroom_privacy }}</p>
                </div>
                <div class="bg-surface rounded-2xl p-4 text-center border border-border">
                  <p class="text-2xl font-bold text-text-dark">{{ listing.bathrooms }}</p>
                  <p class="text-xs text-text-muted mt-0.5">Bathrooms · {{ listing.bathroom_privacy }}</p>
                </div>
                <div class="bg-surface rounded-2xl p-4 text-center border border-border">
                  <p class="text-2xl font-bold text-text-dark">{{ listing.is_sold ? 'Sold' : 'Active' }}</p>
                  <p class="text-xs text-text-muted mt-0.5">Availability</p>
                </div>
                <div class="bg-surface rounded-2xl p-4 text-center border border-border">
                  <p class="text-2xl font-bold text-text-dark">{{ formatDate(listing.created_at) }}</p>
                  <p class="text-xs text-text-muted mt-0.5">Listed</p>
                </div>
              </div>

              <!-- Description -->
              <div v-if="listing.description" v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 300, duration: 500 } }">
                <h2 class="text-xl font-semibold text-text-dark mb-3">About this place</h2>
                <p class="text-text-muted leading-relaxed whitespace-pre-line">{{ listing.description }}</p>
              </div>

              <!-- Amenities -->
              <div v-if="listingAmenities.length" v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 400, duration: 500 } }">
                <h2 class="text-xl font-semibold text-text-dark mb-4">Amenities</h2>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
                  <div v-for="a in listingAmenities" :key="a.id"
                    class="flex items-center gap-3 bg-surface rounded-xl p-3 border border-border">
                    <div class="w-9 h-9 rounded-lg bg-orange/10 flex items-center justify-center shrink-0">
                      <span class="text-lg">{{ amenityIcon(a.name) }}</span>
                    </div>
                    <span class="text-sm text-text-dark font-medium">{{ a.name }}</span>
                  </div>
                </div>
              </div>

              <div v-if="isOwner && editingListing" v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 450, duration: 500 } }"
                class="rounded-3xl border border-border/70 bg-white p-6">
                <div class="mb-4">
                  <h2 class="text-xl font-semibold text-text-dark">Edit Listing</h2>
                </div>

                <form @submit.prevent="saveListingEdits" class="space-y-4">
                  <div v-if="editError" class="bg-destructive/8 text-destructive text-sm rounded-xl px-4 py-3 border border-destructive/15">{{ editError }}</div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Property Type</label>
                    <select v-model="editForm.property_type" required
                      class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
                      <option value="" disabled>Select type</option>
                      <option v-for="pt in propTypes" :key="pt.id" :value="pt.id">{{ pt.name }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Title</label>
                    <input v-model="editForm.title" type="text" required
                      class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Bedrooms</label>
                      <input v-model.number="editForm.bedrooms" type="number" min="0" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Bedroom Setup</label>
                      <select v-model="editForm.bedroom_privacy" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
                        <option value="private">Private</option>
                        <option value="shared">Shared</option>
                      </select>
                    </div>
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Bathrooms</label>
                      <input v-model.number="editForm.bathrooms" type="number" min="0" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Bathroom Setup</label>
                      <select v-model="editForm.bathroom_privacy" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition">
                        <option value="private">Private</option>
                        <option value="shared">Shared</option>
                      </select>
                    </div>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Address</label>
                    <input v-model="editForm.address" type="text" required
                      class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Website</label>
                      <input v-model="editForm.website_url" type="url" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-text-muted mb-1.5">Price ($/month)</label>
                      <input v-model.number="editForm.price" type="number" min="0" step="0.01" required
                        class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition" />
                    </div>
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Description</label>
                    <textarea v-model="editForm.description" rows="4" required
                      class="w-full px-4 py-2.5 border border-border rounded-xl bg-white text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/35 transition"></textarea>
                  </div>

                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-2">Amenities</label>
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                      <button
                        v-for="a in allAmenities"
                        :key="a.id"
                        type="button"
                        @click="toggleEditAmenity(a.name)"
                        :class="editAmenities.has(a.name) ? 'border-orange bg-orange/10 text-orange' : 'border-border bg-white text-text-muted'"
                        class="px-3 py-2 rounded-xl border text-sm font-medium transition"
                      >
                        {{ a.name }}
                      </button>
                    </div>
                  </div>

                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Replace Cover Image (optional)</label>
                    <input type="file" accept="image/*" @change="editForm.images = $event.target.files[0]"
                      class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-3 file:py-2 file:text-sm file:font-medium file:text-white" />
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Replace Gallery Images (optional)</label>
                    <input type="file" accept="image/*" multiple @change="editForm.gallery = [...$event.target.files]"
                      class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-3 file:py-2 file:text-sm file:font-medium file:text-white" />
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-text-muted mb-1.5">Replace Video (optional)</label>
                    <input type="file" accept="video/*" @change="editForm.video = $event.target.files[0]"
                      class="w-full text-sm text-text-muted file:mr-4 file:rounded-xl file:border-0 file:bg-primary-bg file:px-3 file:py-2 file:text-sm file:font-medium file:text-white" />
                  </div>

                  <div class="flex items-center gap-2 pt-1">
                    <button type="submit" :disabled="editSaving"
                      class="px-4 py-2.5 rounded-xl bg-primary-bg text-white text-sm font-medium hover:bg-primary-bg/90 disabled:opacity-50 transition">
                      {{ editSaving ? 'Saving...' : 'Save Changes' }}
                    </button>
                    <button type="button" @click="cancelEditing"
                      class="px-4 py-2.5 rounded-xl border border-border text-sm text-text-muted hover:text-text-dark transition">
                      Cancel
                    </button>
                  </div>
                </form>
              </div>

              <!-- Video -->
              <div v-if="listing.video" v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 500, duration: 500 } }">
                <h2 class="text-xl font-semibold text-text-dark mb-3">Video Tour</h2>
                <video :src="listing.video" controls class="w-full rounded-2xl shadow-sm" />
              </div>
            </div>

            <!-- Sidebar -->
            <div>
              <div v-motion :initial="{ opacity: 0, y: 20 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: 200, duration: 500 } }"
                class="bg-white rounded-3xl shadow-xl p-7 sticky top-20 border border-border/50">
                <p class="text-4xl font-bold text-primary-bg">${{ listing.price }}<span
                    class="text-base font-normal text-text-soft">/mo</span></p>
                <p class="text-text-muted text-sm mt-1">{{ listing.address }}</p>

                <div class="mt-6 space-y-3">
                  <button v-if="authStore.isAuthenticated && listing.created_by !== authStore.user?.id"
                    @click="contactHost"
                    class="w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20">
                    Message Host
                  </button>
                  <a v-if="listing.website_url" :href="listing.website_url" target="_blank" rel="noreferrer"
                    class="block w-full text-center bg-orange/10 text-orange py-3.5 rounded-2xl font-semibold hover:bg-orange/15 transition">
                    Visit Listing Website
                  </a>
                  <template v-if="authStore.isAuthenticated && listing.created_by === authStore.user?.id">
                    <div class="rounded-2xl border border-border/70 bg-surface-alt p-3.5">
                      <label class="block text-xs uppercase tracking-wide text-text-soft mb-1.5">Offer Status</label>
                      <div class="flex items-center gap-2">
                        <select v-model="offerStatusDraft"
                          class="flex-1 px-3 py-2.5 rounded-xl border border-border bg-white text-sm text-text-dark focus:outline-none focus:ring-2 focus:ring-primary-bg/20">
                          <option value="accepting">Accepting Offers</option>
                          <option value="pending">Pending</option>
                          <option value="closed">Closed</option>
                        </select>
                        <button type="button" @click="updateOfferStatus"
                          :disabled="savingOfferStatus || offerStatusDraft === listing.offer_status"
                          class="px-3.5 py-2.5 rounded-xl bg-primary-bg text-white text-sm font-medium hover:bg-primary-bg/90 disabled:opacity-50 transition">
                          {{ savingOfferStatus ? 'Saving' : 'Save' }}
                        </button>
                      </div>
                    </div>
                    <button @click="deleteListing"
                      class="w-full bg-destructive/8 text-destructive py-3.5 rounded-2xl font-semibold hover:bg-destructive/12 transition border border-destructive/15">
                      Delete Listing
                    </button>
                    <button type="button" @click="startEditing"
                      class="w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20">
                      Edit Listing
                    </button>
                  </template>
                  <router-link v-if="!authStore.isAuthenticated" to="/login"
                    class="block text-center w-full bg-primary-bg text-white py-3.5 rounded-2xl font-semibold hover:bg-primary-bg/90 transition shadow-lg shadow-primary-bg/20">
                    Log in to Contact
                  </router-link>
                </div>

                <div class="mt-6 pt-6 border-t border-border/50">
                  <p class="text-xs text-text-soft">Listed {{ timeAgo(listing.created_at) }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <div v-else class="flex flex-col items-center justify-center min-h-[60vh] text-text-soft gap-3">
        <svg class="w-16 h-16 text-border" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
            d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
        </svg>
        <p>Listing not found.</p>
        <button @click="goBack" class="mt-2 text-sm text-orange hover:underline">Go back</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { listings as listingsApi, amenities as amenitiesApi, propertyTypes, conversations as convoApi } from '../api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const listing = ref(null)
const loading = ref(true)
const showHelp = ref(false)
const allAmenities = ref([])
const propTypes = ref([])
const carouselRef = ref(null)
const activeImageIndex = ref(0)
const scrolled = ref(false)
const savingOfferStatus = ref(false)
const offerStatusDraft = ref('accepting')
const editingListing = ref(false)
const editSaving = ref(false)
const editError = ref('')
const editAmenities = ref(new Set())
const editForm = ref({
  property_type: '',
  title: '',
  bedrooms: 1,
  bedroom_privacy: 'private',
  bathrooms: 1,
  bathroom_privacy: 'private',
  address: '',
  website_url: '',
  price: 0,
  description: '',
  images: null,
  gallery: [],
  video: null,
})

function onScroll() {
  scrolled.value = window.scrollY > 20
}


const allImages = computed(() => {
  if (!listing.value) return []
  const imgs = []
  if (listing.value.images) imgs.push(listing.value.images)
  if (listing.value.gallery_images?.length) {
    imgs.push(...listing.value.gallery_images.map(g => g.image))
  }
  return imgs.length ? imgs : ['/placeholder.jpg']
})

const listingAmenities = computed(() => {
  if (!listing.value?.amenity_ids?.length || !allAmenities.value.length) return []
  return allAmenities.value.filter(a => listing.value.amenity_ids.includes(a.id))
})

const offerStatusLabel = computed(() => {
  const s = offerStatusDraft.value || listing.value?.offer_status
  if (s === 'accepting') return 'Accepting Offers'
  if (s === 'pending') return 'Pending'
  if (s === 'closed') return 'Closed'
  return 'Unknown'
})

const isOwner = computed(() => !!(authStore.user?.id && listing.value?.created_by === authStore.user.id))

function formatDate(d) {
  return d ? new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) : ''
}

function timeAgo(d) {
  if (!d) return ''
  const diff = Date.now() - new Date(d).getTime()
  const days = Math.floor(diff / 86400000)
  if (days === 0) return 'today'
  if (days === 1) return 'yesterday'
  if (days < 30) return `${days} days ago`
  return formatDate(d)
}

function amenityIcon(name) {
  const n = name.toLowerCase()
  if (n.includes('laundry')) return '🧺'
  if (n.includes('pool') || n.includes('swim')) return '🏊'
  if (n.includes('parking')) return '🅿️'
  if (n.includes('gym') || n.includes('fitness')) return '🏋️'
  if (n.includes('wifi') || n.includes('internet')) return '📶'
  if (n.includes('air') || n.includes('ac')) return '❄️'
  if (n.includes('heat')) return '🔥'
  if (n.includes('garbage') || n.includes('trash')) return '🗑️'
  if (n.includes('pet')) return '🐾'
  if (n.includes('balcon') || n.includes('patio')) return '🌿'
  if (n.includes('dishwash')) return '🍽️'
  if (n.includes('elevator')) return '🛗'
  if (n.includes('security')) return '🔒'
  if (n.includes('storage')) return '📦'
  return '✨'
}

function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/dashboard')
}

function scrollCarousel(dir) {
  if (!carouselRef.value) return
  const container = carouselRef.value
  const cardWidth = container.firstElementChild?.offsetWidth || 300
  container.scrollBy({ left: dir * (cardWidth + 16), behavior: 'smooth' })
  activeImageIndex.value = Math.max(0, Math.min(allImages.value.length - 1, activeImageIndex.value + dir))
}

async function handleLike() {
  if (isOwner.value) return
  try {
    await listingsApi.toggleLike(listing.value.id)
    listing.value.likes_count = (listing.value.likes_count || 0) + 1
  } catch { /* silent */ }
}

async function contactHost() {
  try {
    await listingsApi.trackInquiry(listing.value.id)
    const { data } = await convoApi.create({ item: null, members: [listing.value.created_by, authStore.user.id] })
    router.push(`/inbox/${data.id}`)
  } catch {
    alert('Could not start conversation.')
  }
}

async function deleteListing() {
  if (!confirm('Are you sure you want to delete this listing?')) return
  try {
    await listingsApi.delete(listing.value.id)
    router.push('/dashboard')
  } catch {
    alert('Failed to delete listing.')
  }
}

async function updateOfferStatus() {
  if (!listing.value || listing.value.created_by !== authStore.user?.id) return
  if (offerStatusDraft.value === listing.value.offer_status) return
  savingOfferStatus.value = true
  try {
    const fd = new FormData()
    fd.append('offer_status', offerStatusDraft.value)
    await listingsApi.update(listing.value.id, fd)
    listing.value.offer_status = offerStatusDraft.value
  } catch {
    offerStatusDraft.value = listing.value.offer_status
    alert('Failed to update offer status.')
  } finally {
    savingOfferStatus.value = false
  }
}

function startEditing() {
  if (!listing.value) return
  editError.value = ''
  editingListing.value = true
  editForm.value = {
    property_type: listing.value.property_type,
    title: listing.value.title || '',
    bedrooms: listing.value.bedrooms ?? 1,
    bedroom_privacy: listing.value.bedroom_privacy || 'private',
    bathrooms: listing.value.bathrooms ?? 1,
    bathroom_privacy: listing.value.bathroom_privacy || 'private',
    address: listing.value.address || '',
    website_url: listing.value.website_url || '',
    price: listing.value.price ?? 0,
    description: listing.value.description || '',
    images: null,
    gallery: [],
    video: null,
  }
  const selectedNames = allAmenities.value
    .filter((a) => listing.value.amenity_ids?.includes(a.id))
    .map((a) => a.name)
  editAmenities.value = new Set(selectedNames)
}

function cancelEditing() {
  editingListing.value = false
  editSaving.value = false
  editError.value = ''
  editAmenities.value = new Set()
}

function toggleEditAmenity(name) {
  const next = new Set(editAmenities.value)
  if (next.has(name)) next.delete(name)
  else next.add(name)
  editAmenities.value = next
}

async function saveListingEdits() {
  if (!listing.value) return
  editSaving.value = true
  editError.value = ''
  try {
    const fd = new FormData()
    fd.append('property_type', editForm.value.property_type)
    fd.append('title', editForm.value.title)
    fd.append('bedrooms', String(editForm.value.bedrooms))
    fd.append('bedroom_privacy', editForm.value.bedroom_privacy)
    fd.append('bathrooms', String(editForm.value.bathrooms))
    fd.append('bathroom_privacy', editForm.value.bathroom_privacy)
    fd.append('address', editForm.value.address)
    fd.append('website_url', editForm.value.website_url)
    fd.append('price', String(editForm.value.price))
    fd.append('description', editForm.value.description)
    fd.append('offer_status', listing.value.offer_status || 'accepting')
    if (editForm.value.images) fd.append('images', editForm.value.images)
    if (editForm.value.video) fd.append('video', editForm.value.video)
    for (const image of editForm.value.gallery || []) {
      fd.append('gallery_images', image)
    }
    if (editAmenities.value.size) {
      for (const name of editAmenities.value) fd.append('amenity_names', name)
    } else {
      fd.append('amenity_names', '')
    }
    const { data } = await listingsApi.update(listing.value.id, fd)
    listing.value = data
    editingListing.value = false
  } catch (e) {
    editError.value = typeof e.response?.data === 'object'
      ? Object.values(e.response.data).flat().join(' ')
      : 'Failed to update listing.'
  } finally {
    editSaving.value = false
  }
}

function getOrCreateVisitorToken() {
  const key = 'lvspace_visitor_token'
  let token = localStorage.getItem(key)
  if (!token) {
    token = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`
    localStorage.setItem(key, token)
  }
  return token
}

onMounted(async () => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
  try {
    const [listingRes, amenitiesRes, propertyTypesRes] = await Promise.all([
      listingsApi.get(route.params.id),
      amenitiesApi.list(),
      propertyTypes.list(),
    ])
    listing.value = listingRes.data
    offerStatusDraft.value = listingRes.data.offer_status || 'accepting'
    allAmenities.value = Array.isArray(amenitiesRes.data) ? amenitiesRes.data : amenitiesRes.data.results || []
    propTypes.value = Array.isArray(propertyTypesRes.data) ? propertyTypesRes.data : propertyTypesRes.data.results || []
    const visitorToken = getOrCreateVisitorToken()
    listingsApi.trackClick(route.params.id, { visitor_token: visitorToken }).catch(() => { })
  } catch {
    listing.value = null
  } finally {
    loading.value = false
  }
})


onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
