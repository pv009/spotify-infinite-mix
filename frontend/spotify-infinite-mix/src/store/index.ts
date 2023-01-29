import Vuex from 'vuex'
import PlayerModule from './player';
import SpotifyModule from './spotify'

const store = new Vuex.Store({
  modules: {
    spotify: SpotifyModule,
    player: PlayerModule
  }
});

export default store