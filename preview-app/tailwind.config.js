/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          solid: "#3079ff",
          secondary: "#eaf1ff"
        },
        warning: {
          secondary: "#fff2d7"
        },
        primary: {
          DEFAULT: "white"
        },
        text: {
          primary: "#34404b",
          secondary: "#717981",
          brand: "#3079ff",
          white: "white"
        },
        border: {
          primary: "#e0e0e0",
          brand: "#3079ff"
        }
      }
    },
  },
  plugins: [],
}
