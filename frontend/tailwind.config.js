/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Roboto Slab', 'serif'],
      },
      colors: {
        primary: {
          50: 'rgb(var(--primary-background) / 0.08)',
          100: 'rgb(var(--primary-background) / 0.14)',
          200: 'rgb(var(--primary-background) / 0.22)',
          300: 'rgb(var(--primary-background) / 0.32)',
          400: 'rgb(var(--primary-background) / 0.55)',
          500: 'rgb(var(--primary-background) / 0.85)',
          600: 'rgb(var(--primary-background) / 1)',
          700: 'rgb(var(--primary-hover) / 1)',
          800: 'rgb(var(--primary-hover) / 1)',
          900: 'rgb(var(--primary-hover) / 1)',
        },
        'primary-fg': 'rgb(var(--primary-foreground) / <alpha-value>)',
        'primary-bg': 'rgb(var(--primary-background) / <alpha-value>)',
        'secondary-fg': 'rgb(var(--secondary-foreground) / <alpha-value>)',
        'secondary-bg': 'rgb(var(--secondary-background) / <alpha-value>)',
        'text-light': 'rgb(var(--text-light) / <alpha-value>)',
        'text-dark': 'rgb(var(--text-dark) / <alpha-value>)',
        destructive: 'rgb(var(--destructive) / <alpha-value>)',
        border: 'rgb(var(--border) / <alpha-value>)',
      },
    },
  },
  plugins: [],
}
