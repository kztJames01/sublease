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
        black: {
          DEFAULT: '#000000',
        },
        prussian_blue: {
          DEFAULT: '#14213d',
        },
        orange: {
          DEFAULT: '#fca311',
        },
        white: {
          DEFAULT: '#ffffff',
        },
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
        'text-muted': 'rgb(var(--text-muted) / <alpha-value>)',
        'text-soft': 'rgb(var(--text-soft) / <alpha-value>)',
        page: 'rgb(var(--page-background) / <alpha-value>)',
        surface: 'rgb(var(--surface) / <alpha-value>)',
        'surface-alt': 'rgb(var(--surface-alt) / <alpha-value>)',
        destructive: 'rgb(var(--destructive) / <alpha-value>)',
        success: 'rgb(var(--success) / <alpha-value>)',
        border: 'rgb(var(--border) / <alpha-value>)',
      },
    },
  },
  plugins: [],
}
