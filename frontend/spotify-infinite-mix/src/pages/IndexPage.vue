<template>
  <q-page class="row items-center justify-evenly">
    <h3>Authorizing...</h3>
  </q-page>
</template>

<script setup lang="ts">
import SpotifyModule from '../store/spotify';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getModule } from 'vuex-module-decorators';
import store from '../store';

const $route = useRoute();
let spotifyStore: SpotifyModule;

onMounted(() => {
  initStores();
  
  if (!$route.fullPath.includes('code=')) {
    getSpotifyCode(); 
  } else {
    authorizeOnSpotify($route.fullPath);
  }
});

function initStores() {
  spotifyStore = getModule(SpotifyModule, store);
  console.log(spotifyStore);
}

function getSpotifyCode() {
  const scopes = [
    'user-read-playback-state',
    'streaming',
    'user-read-playback-position',
    'user-read-currently-playing',
    'app-remote-control',
    'user-modify-playback-state'
  ]
  const params = {
    response_type: 'code',
    scope: scopes.join(','),
    client_id: process.env.SPOTIFY_CLIENT_ID,
    redirect_uri: process.env.SPOTIFY_REDIRECT_URL
  }

  let authUrl = `${process.env.SPOTIFY_AUTH_BASE_URL}/en/authorize?`;

  Object.entries(params).forEach(([key, value], index) => {
    authUrl += `${key}=${value}`;
    if (index < Object.entries(params).length - 1) {
      authUrl += '&';
    }
  });

  window.open(authUrl, '_same');
}

async function authorizeOnSpotify(routePath: string) {
  const code = routePath.split('code=')[1];
  await spotifyStore.getSpotifyAccesToken(code);
}
</script>
