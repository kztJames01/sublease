<template>
  <footer class="relative bg-[#0a1628] text-primary-fg/85 mt-auto overflow-hidden">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_60%_40%_at_50%_-10%,rgba(26,58,107,0.5),transparent)]" />
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <h3 class="text-xl font-display font-bold text-primary-fg mb-3">lvSpace</h3>
          <p class="text-sm text-primary-fg/75">Find your next sublease or list your property with ease.</p>
        </div>
        <div>
          <h4 class="font-semibold text-primary-fg mb-3">Quick Links</h4>
          <div class="space-y-2 text-sm">
            <router-link to="/search" class="block hover:text-orange transition">Search Listings</router-link>
            <router-link to="/faq" class="block hover:text-orange transition">FAQ</router-link>
            <router-link to="/contact" class="block hover:text-orange transition">Contact</router-link>
          </div>
        </div>
        <div>
          <h4 class="font-semibold text-primary-fg mb-3">For Hosts</h4>
          <div class="space-y-2 text-sm">
            <router-link to="/listings/new" class="block hover:text-orange transition">List Property</router-link>
            <router-link to="/dashboard" class="block hover:text-orange transition">Dashboard</router-link>
          </div>
        </div>
        <div>
          <h4 class="font-semibold text-primary-fg mb-3">Contact</h4>
          <p class="text-sm text-primary-fg/75">support@lvspace.com</p>
        </div>
      </div>
      <div class="border-t border-white/10 mt-8 pt-6 text-center text-sm text-white/45">
        &copy; {{ new Date().getFullYear() }} lvSpace. All rights reserved.
      </div>
    </div>
  </footer>
</template>
