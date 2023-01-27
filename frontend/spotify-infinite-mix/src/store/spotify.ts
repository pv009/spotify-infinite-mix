import { Action, getModule, Module, Mutation, VuexModule } from 'vuex-module-decorators'
import { SpotifyAuthData } from 'src/model/auth.model';
import { api } from '../boot/axios';

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
    }

    @Action
    public async getSpotifyAccesToken(spotifyCode: string) {
        try {
            const authResponse = await api.get('spotify-access-token', {
                params: { code: spotifyCode}
            });
            this.context.commit('setSpotifyAuthData', authResponse.data)
        } catch (e) {
            console.error('error loading spotify access token:', e);
        }
    }
}