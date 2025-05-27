/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/video_lectures/**/*.html',
    './static/**/*.js',
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
      },
      animation: {
        'spin-slow': 'spin 1s linear infinite',
        'scale-in': 'scaleIn 0.3s ease-out',
        'fade-in': 'fadeIn 0.3s ease-out'
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

