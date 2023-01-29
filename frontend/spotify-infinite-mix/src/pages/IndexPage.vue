<template>
  <q-page class="index-page column items-center justify-evenly">
    <div v-if="!authorized" class="column items-center justify-evenly">
      <h3>Authorizing...</h3>
      <q-circular-progress indeterminate reverse size="75px" :thickness="0.6" font-size="50px" color="light-blue"
        center-color="grey-9" class="q-ma-md" />
    </div>
    <div class="mode-selection column items-center justify-center" v-else>
      <h3>Choose your Mode:</h3>
      <q-btn color="primary" icon="person" label="Personal" @click="setMode('private')" />
      <q-btn color="primary" icon="celebration" label="Party" @click="setMode('party')" disabled />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import SpotifyModule from '../store/spotify';
import { App, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { getModule } from 'vuex-module-decorators';
import store from '../store';
import { Notify } from 'quasar';
import PlayerModule from '../store/player';
import { AppMode } from '../model/player.model';

const $route = useRoute();
const $router = useRouter();
let spotifyStore: SpotifyModule;
let playerStore: PlayerModule;
let authorized = ref(false);

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
  playerStore = getModule(PlayerModule, store);
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
  try {
    await spotifyStore.getSpotifyAccesToken(code);
    Notify.create({
      message: 'Authorized successfully',
      type: 'positive'

    });
    authorized.value = true;
  } catch (error) {
    Notify.create({
      message: 'Authorization on Spotify failed',
      type: 'negative'
    });
  }
}

function setMode(mode: string) {
  playerStore.setAppMode(mode as AppMode);
  $router.push({
    path: '/player'
  })
}
</script>

<style lang="scss" scoped>
.index-page {
  .mode-selection {
    .q-btn {
      width: 300px;
      height: 50px;

      &:first-of-type {
        margin-bottom: 30px;
      }
    }
  }
}
</style>