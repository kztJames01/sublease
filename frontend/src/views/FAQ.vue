<template>
  <div>
    <!-- Hero banner -->
    <section class="relative pt-16 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-[#0a1628] via-primary-bg to-[#1a3a6b]" />
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_50%_50%_at_70%_-10%,rgba(252,163,17,0.1),transparent)]" />
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-page to-transparent" />
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-20 text-center">
        <span
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
          class="text-sm font-semibold text-orange uppercase tracking-widest"
        >Support</span>
        <h1
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: 100, duration: 600 } }"
          class="text-4xl lg:text-5xl font-display font-bold text-white mt-3"
        >Frequently Asked Questions</h1>
        <p
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :enter="{ opacity: 1, y: 0, transition: { delay: 250, duration: 500 } }"
          class="text-white/60 mt-3 text-lg"
        >Everything you need to know about lvSpace</p>
      </div>
    </section>

    <section class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 relative z-10 pb-16">
      <div class="space-y-3">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          v-motion
          :initial="{ opacity: 0, y: 15 }"
          :visibleOnce="{ opacity: 1, y: 0, transition: { delay: i * 60, duration: 400 } }"
          class="bg-surface rounded-2xl shadow-sm overflow-hidden border border-border hover:shadow-md transition-shadow duration-300"
        >
          <button @click="openIndex = openIndex === i ? -1 : i" class="w-full px-6 py-5 text-left flex items-center justify-between gap-4">
            <span class="font-semibold text-text-dark">{{ faq.q }}</span>
            <svg
              class="w-5 h-5 text-text-soft transition-transform duration-300 shrink-0"
              :class="{ 'rotate-180': openIndex === i }"
              fill="none" stroke="currentColor" viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <Transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="max-h-0 opacity-0"
            enter-to-class="max-h-40 opacity-100"
            leave-active-class="transition-all duration-200 ease-in"
            leave-from-class="max-h-40 opacity-100"
            leave-to-class="max-h-0 opacity-0"
          >
            <div v-if="openIndex === i" class="px-6 pb-5 text-text-muted text-sm leading-relaxed overflow-hidden">{{ faq.a }}</div>
          </Transition>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const openIndex = ref(-1)
const faqs = [
  { q: 'What is lvSpace?', a: 'lvSpace is a platform that helps students find and list subleases near their campus.' },
  { q: 'How do I list my property?', a: 'Create an account, then click "List Property" in the navigation bar. Fill out the form with your property details.' },
  { q: 'Is it free to use?', a: 'Yes! Listing and searching are completely free for all users.' },
  { q: 'How do I contact a host?', a: 'Click on a listing and use the "Message Host" button to start a conversation.' },
  { q: 'Can I list an apartment complex?', a: 'Yes, we have a dedicated form for apartment complexes with bulk listing capabilities.' },
  { q: 'How do I reset my password?', a: 'Click "Forgot password?" on the login page and follow the instructions sent to your email.' },
  { q: 'Is my information secure?', a: 'We use industry-standard encryption and never share your personal data with third parties.' },
  { q: 'Can I save listings?', a: 'Yes, click the heart icon on any listing to save it to your favorites.' },
  { q: 'How do I report a listing?', a: 'Contact our support team through the Contact page with the listing details.' },
  { q: 'What areas do you cover?', a: 'We cover all major college towns and cities across the United States.' },
]
</script>
