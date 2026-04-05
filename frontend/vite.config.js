import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    host: true,
    // Faster HMR
    hmr: {
      overlay: false,
    },
    // Optimize deps pre-bundling
    warmup: {
      clientFiles: ['./src/main.js', './src/App.vue'],
    },
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/media': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    // Faster builds
    reportCompressedSize: false,
    chunkSizeWarningLimit: 1000,
  },
})
