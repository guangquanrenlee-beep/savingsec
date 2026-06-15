/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./layouts/**/*.html", "./content/**/*.md"],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#192945',
          light: '#2a3f5f',
          dark: '#0f1d32',
        },
        accent: {
          DEFAULT: '#e67e22',
          light: '#f5a623',
        },
        neutral: {
          white: '#ffffff',
          light: '#f7f8fa',
          border: '#e8ebf0',
          text: '#444444',
          muted: '#888888',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        heading: ['Montserrat', 'Open Sans', 'Arial', 'sans-serif'],
        body: ['Roboto', 'Open Sans', 'Arial', 'sans-serif'],
      },
      borderRadius: { DEFAULT: '10px', lg: '10px', xl: '10px', '2xl': '10px' },
      maxWidth: { content: '1280px' },
      spacing: { '13': '3.25rem' },
      boxShadow: {
        card: '0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)',
        'card-hover': '0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04)',
        'button-brand': '0 4px 12px rgba(25,41,69,0.3)',
        'button-accent': '0 4px 12px rgba(230,126,34,0.3)',
        dropdown: '0 10px 30px rgba(0,0,0,0.12)',
      },
    },
  },
  plugins: [],
}
