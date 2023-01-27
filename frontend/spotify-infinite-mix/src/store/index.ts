import Vuex from 'vuex'
import SpotifyModule from './spotify'

const store = new Vuex.Store({
  modules: {
    spotify: SpotifyModule
  }
});

export default store