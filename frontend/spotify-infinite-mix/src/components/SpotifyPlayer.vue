<template>
    <div class="spotify-player">
        <div class="meta-info column items-center" v-if="getCurrentSong() && !songLoading">
            <img :src="getCurrentSong()?.imageURL" />
            <h3>{{ getCurrentSong()?.name }}</h3>
            <p>{{ getCurrentSong()?.artist }}</p>
            <div class="transport row justify-center">
                <p>0:00</p>
                <q-slider :model-value="percentPlayed" color="primary" :min="0" :max="100" readonly />
                <p>{{ secondsPlayed }} / {{ getCurrentSong().durationInSeconds.toFixed(0) }} Sek</p>
            </div>

        </div>
        <q-circular-progress reverse indeterminate size="75px" :thickness="0.6" font-size="50px" color="light-blue"
            center-color="grey-9" class="q-ma-md" v-else />
        <div class="control-buttons row justify-center">
            <q-btn v-if="songPlaying" round color="primary" icon="pause" @click="pauseSong()"
                :disabled="!getCurrentSong" />
            <q-btn v-else color="primary" round icon="play_arrow" @click="startSong()" :disabled="!getCurrentSong" />
            <q-btn color="primary" round icon="skip_next" @click="nextSong()" :disabled="!getCurrentSong" />
        </div>
    </div>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue';
import { getModule } from 'vuex-module-decorators';
import { SpotifyAnalysis } from '../model/analysis-response.model';
import { SpotifySong } from '../model/spotify-song.model';
import store from '../store';
import PlayerModule from '../store/player';

let percentPlayed = ref(0);
let secondsPlayed = 0;
let songPlaying = ref(false);
let songLoading = ref(false);

let percentLoop: null | NodeJS.Timer = null;
let secondLoop: null | NodeJS.Timer = null;

let playerStore: PlayerModule;

onMounted(() => {
    initStores();
    nextSong();
});

function initStores() {
    playerStore = getModule(PlayerModule, store);
}

async function nextSong() {
    songLoading.value = true;
    await saveSongData();
    await playerStore.getRandomSongFromSpotify();
    startPlayingProgress(true);
    songPlaying.value = true;
    songLoading.value = false;
}

async function saveSongData() {
    if (playerStore.analysisDataLoaded) {
        const songData: SpotifyAnalysis = playerStore.analysisDataLoaded;
        songData.percent_listened = percentPlayed.value;
        await playerStore.sendSongData(songData);
    }
}

function startSong() {
    songPlaying.value = true;
    startPlayingProgress(false);
}

function pauseSong() {
    songPlaying.value = false;
    clearPercentLoop();
    clearSecondLoop();
}

function startPlayingProgress(reset: boolean) {
    if (reset) {
        percentPlayed.value = 0;
        secondsPlayed = 0;
        clearPercentLoop();
        clearSecondLoop();
    }
    percentLoop = setInterval(() => {
        percentPlayed.value += 1 / (getCurrentSong()!.durationInSeconds);
    }, 1000);
    secondLoop = setInterval(() => {
        secondsPlayed += 1;
    }, 1000);
}

function clearPercentLoop() {
    if (percentLoop) {
        clearInterval(percentLoop);
    }
}

function clearSecondLoop() {
    if (secondLoop) {
        clearInterval(secondLoop);
    }
}

function getCurrentSong() {
    if (playerStore) {
        return playerStore.songLoaded;
    }
    return null;
}
</script>

<style lang='scss' scoped>
.spotify-player {
    .meta-info {
        width: 100%;

        img {
            width: 200px;
            height: 200px;
        }

        h3,
        p {
            text-align: center;
        }

        h3 {
            margin-bottom: 0;
        }

        .transport {
            width: 360px;
            gap: 10px;

            .q-slider {
                width: 150px;
            }
        }
    }


    .control-buttons {
        width: 100%;
        gap: 20px;
    }
}
</style>