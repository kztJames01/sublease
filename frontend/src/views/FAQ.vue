<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-8">Frequently Asked Questions</h1>
    <div class="space-y-4">
      <div v-for="(faq, i) in faqs" :key="i" class="bg-white rounded-xl shadow-sm overflow-hidden">
        <button @click="openIndex = openIndex === i ? -1 : i" class="w-full px-6 py-4 text-left flex items-center justify-between">
          <span class="font-medium text-gray-900">{{ faq.q }}</span>
          <svg class="w-5 h-5 text-gray-400 transition" :class="{ 'rotate-180': openIndex === i }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </button>
        <div v-if="openIndex === i" class="px-6 pb-4 text-gray-600 text-sm leading-relaxed">{{ faq.a }}</div>
      </div>
    </div>
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
