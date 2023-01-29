import { Action, getModule, Module, Mutation, VuexModule } from 'vuex-module-decorators'
import { SpotifyAuthData } from 'src/model/auth.model';
import { api, spotifyApi } from '../boot/axios';
import { AppMode } from '../model/player.model';
import { SpotifySong } from '../model/spotify-song.model';
import { TrackResponse } from '../model/track-response.model';
import { SpotifyAnalysis } from '../model/analysis-response.model';

@Module({
    namespaced: true,
    stateFactory: true,
    name: 'player'
})
export default class PlayerModule extends VuexModule {
    appMode: AppMode | null = null;
    currentSong: SpotifySong | null = null;
    currentAnalysis: SpotifyAnalysis | null = null;

    @Mutation
    public setAppMode(mode: AppMode) {
        this.appMode = mode;
    }

    @Mutation
    private setCurrentSong(song: SpotifySong) {
        this.currentSong = song;
    }

    @Mutation
    private setCurrentAnalysisData(analysis: SpotifyAnalysis) {
        this.currentAnalysis = analysis;
    }

    @Action
    public async getRandomSongFromSpotify() {
        try {
            const songResponse = await api.get<TrackResponse>('spotify/random-song/');
            console.log(songResponse);
            if (songResponse.data.tracks.items?.length > 0) {
                const singleSongFromResponse = songResponse.data.tracks.items[0];
                const transFormedSong: SpotifySong = {
                    id: singleSongFromResponse.id,
                    artist: singleSongFromResponse.artists.map(artist => artist.name).join(", "),
                    name: singleSongFromResponse.name,
                    imageURL: singleSongFromResponse.album.images[0].url,
                    durationInSeconds: singleSongFromResponse.duration_ms / 1000
                };
                this.context.commit('setCurrentSong', transFormedSong);
                this.context.dispatch('getSongAnalysisFromSpotify', transFormedSong.id);
            }
        } catch (e) {
            console.error(`Error loading random song from spotiy: ${e}`)
        }
    }

    @Action
    private async getSongAnalysisFromSpotify(songId: string) {
        try {
            const analysisDataResponse = await api.get<SpotifyAnalysis>(`spotify/meta-data/${songId}`);
            this.context.commit('setCurrentAnalysisData', analysisDataResponse.data);
        } catch(e) {
            console.error('Error loading analysis data: ', e);
        }
    }

    @Action
    public async sendSongData(payload: SpotifyAnalysis) {{
        try {
            await api.post<SpotifyAnalysis>('data/song-data/', payload);
        } catch(e) {
            console.error('Error loading analysis data: ', e);
        }
    }}

    get songLoaded() {
        return this.currentSong;
    }

    get analysisDataLoaded() {
        return this.currentAnalysis;
    }
}