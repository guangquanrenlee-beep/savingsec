/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./layouts/**/*.html", "./content/**/*.md"],
  theme: {
    extend: {
      colors: {
        primary: { 50:'#eff6ff',100:'#dbeafe',200:'#bfdbfe',300:'#93c5fd',400:'#60a5fa',500:'#3b82f6',600:'#2563eb',700:'#1d4ed8',800:'#1e40af',900:'#1e3a8a' },
        accent: { 50:'#f0fdf4',100:'#dcfce7',200:'#bbf7d0',300:'#86efac',400:'#4ade80',500:'#22c55e',600:'#16a34a',700:'#15803d' },
        warning: { 50:'#fefce8',100:'#fef9c3',400:'#facc15',500:'#eab308',600:'#ca8a04' },
        danger: { 50:'#fef2f2',100:'#fee2e2',400:'#f87171',500:'#ef4444',600:'#dc2626' },
      },
      fontFamily: { sans: ['Inter','system-ui','sans-serif'] },
      boxShadow: { card:'0 1px 3px rgba(0,0,0,.1), 0 1px 2px rgba(0,0,0,.06)', 'card-hover':'0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -2px rgba(0,0,0,.05)' },
    },
  },
  plugins: [],
}
