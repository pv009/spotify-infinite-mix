import { Action, Module, Mutation, VuexModule } from 'vuex-module-decorators'
import { SpotifyAuthData } from 'src/model/auth.model';
import { api, spotifyApi } from '../boot/axios';

@Module({
    namespaced: true,
    stateFactory: true,
    name: 'spotify'
})
export default class SpotifyModule extends VuexModule {
    auth: SpotifyAuthData | null = null;

    @Mutation
    public setSpotifyAuthData(authResponse: SpotifyAuthData) {
        this.auth = authResponse;
        api.interceptors.request.use(config => {
            config.headers.spotify_access = authResponse.access_token;
            return config;
        });
    }

    @Mutation
    private setSpotifyAccessToken(token: string) {
        if (this.auth) {
            this.auth.access_token = token;
            api.interceptors.request.use(config => {
                config.headers.spotify_access = token;
            });
        }
    }

    @Action
    public async getSpotifyAccesToken(spotifyCode: string) {
        try {
            const authResponse = await api.get<SpotifyAuthData>('spotify/access-token/', {
                params: { code: spotifyCode }
            });
            this.context.commit('setSpotifyAuthData', authResponse.data);
            this.context.dispatch('refreshTokenPeriodically');
        } catch (e) {
            console.error('error loading spotify access token:', e);
        }
    }

    @Action
    private async refreshTokenPeriodically() {
        setInterval(async () => {
            try {
                const authResponse = await api.get<SpotifyAuthData>('spotify/refresh-token/', {
                    params: { refresh_token: this.auth?.refresh_token }
                });
                this.context.commit('setSpotifyAccessToken', authResponse.data.access_token);
            } catch (e) {
                console.error('error refreshing spotify access token:', e);
            }
        }, 30000);
    }
}