/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#0E71BB",
          700: "#095D7E",
        },
        secondary: "#0FD9B6",
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

