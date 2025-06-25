const colors = require('tailwindcss/colors')

module.exports = {
  darkMode: 'class',
  content: [
  './core/templates/**/*.html',
  './core/templates/core/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        gray: colors.gray,
        teal: colors.teal,
      },
    },
  },
  plugins: [],
}