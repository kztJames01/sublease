<template>
  <footer class="bg-secondary-bg text-secondary-fg/85 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <h3 class="text-xl font-display font-bold text-secondary-fg mb-3">lvSpace</h3>
          <p class="text-sm text-secondary-fg/75">Find your next sublease or list your property with ease.</p>
        </div>
        <div>
          <h4 class="font-semibold text-secondary-fg mb-3">Quick Links</h4>
          <div class="space-y-2 text-sm">
            <router-link to="/search" class="block hover:text-primary-fg transition">Search Listings</router-link>
            <router-link to="/faq" class="block hover:text-primary-fg transition">FAQ</router-link>
            <router-link to="/contact" class="block hover:text-primary-fg transition">Contact</router-link>
          </div>
        </div>
        <div>
          <h4 class="font-semibold text-secondary-fg mb-3">For Hosts</h4>
          <div class="space-y-2 text-sm">
            <router-link to="/listings/new" class="block hover:text-primary-fg transition">List Property</router-link>
            <router-link to="/dashboard" class="block hover:text-primary-fg transition">Dashboard</router-link>
          </div>
        </div>
        <div>
          <h4 class="font-semibold text-secondary-fg mb-3">Contact</h4>
          <p class="text-sm text-secondary-fg/75">support@lvspace.com</p>
        </div>
      </div>
      <div class="border-t border-secondary-fg/20 mt-8 pt-6 text-center text-sm text-secondary-fg/65">
        &copy; {{ new Date().getFullYear() }} lvSpace. All rights reserved.
      </div>
    </div>
  </footer>
</template>
