import { boot } from 'quasar/wrappers';
import axios, { AxiosInstance } from 'axios';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

const spotifyAuthApi = axios.create({ baseURL: process.env.SPOTIFY_AUTH_BASE_URL });
const api = axios.create({ baseURL: process.env.API_BASE_URL });

export default boot(({ app }) => {
  app.config.globalProperties.$axios = axios;
  app.config.globalProperties.$api = api;
  app.config.globalProperties.$spotifyAuthApi = spotifyAuthApi;
});

export { api , spotifyAuthApi};
