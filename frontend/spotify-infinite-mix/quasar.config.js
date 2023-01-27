const { configure } = require('quasar/wrappers');


module.exports = configure(function () {
  return {
    eslint: {
      warnings: true,
      errors: true
    },
    boot: [
      
      'axios',
    ],
    css: [
      'app.scss'
    ],
    extras: [
      'roboto-font',
      'material-icons',
    ],
    build: {
      target: {
        browser: [ 'es2019', 'edge88', 'firefox78', 'chrome87', 'safari13.1' ],
        node: 'node16'
      },
      env: require('dotenv').config().parsed,
      vueRouterMode: 'history',
    },
    devServer: {
      open: true
    },

    framework: {
      config: {},
      plugins: []
    },
    animations: [],
    ssr: {
      pwa: false,
      prodPort: 3000,

      middlewares: [
        'render' // keep this as last one
      ]
    },
    pwa: {
      workboxMode: 'generateSW',
      injectPwaMetaTags: true,
      swFilename: 'sw.js',
      manifestFilename: 'manifest.json',
      useCredentialsForManifestTag: false,
    },
    cordova: {
    },
    capacitor: {
      hideSplashscreen: true
    },
    electron: {
      inspectPort: 5858,
      bundler: 'packager', // 'packager' or 'builder'
      packager: {
      },
      builder: {

        appId: 'spotify-infinite-mix'
      }
    },
    bex: {
      contentScripts: [
        'my-content-script'
      ],
    }
  }
});
