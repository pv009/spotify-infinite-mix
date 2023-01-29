<template>
    <q-page class="player-page column items-center justify-evenly">
        <div class="player column items-center justify-evenly">
            <SpotifyPlayer />
        </div>
    </q-page>
</template>

<script setup lang="ts">
import SpotifyModule from '../store/spotify';
import { App, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { getModule } from 'vuex-module-decorators';
import store from '../store';
import PlayerModule from '../store/player';
import SpotifyPlayer from '../components/SpotifyPlayer.vue';

</script>

<style lang="scss" scoped>

</style>