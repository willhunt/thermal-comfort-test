const path = require("path")

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],

  devServer: {
    proxy: 'http://127.0.0.1:8000/'
  },

  outputDir: path.resolve(__dirname, "../backend/subjectivetest/static/subjectivetest/vue"),
}