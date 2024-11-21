import { createStore } from 'vuex'
export default createStore({
    state() {
        return {
            token: null,
            isLogged: false,
            tryTimes: 0,
        }
    },
    getters: {
        getToken: state => state.token,
        isLogged: state => state.isLogged,
        getTryTimes: state => state.tryTimes,
    },
    mutations: {
        setToken: (state, token) => {
            state.token = token;
        },
        setIsLogged: (state, isLogged) => {
            state.isLogged = isLogged;
        },
        logout(state) {
            state.token = null;
            state.isLogged = false;
            state.tryTimes = 0;
        },
        addTryTimes(state) {
            state.tryTimes++;
        },
        resetTryTimes(state) {
            state.tryTimes = 0;
        }

    },
    actions: {
        updateToken: ({ commit }, token) => {
            commit('setToken', token);
        },
        updateIsLogged: ({ commit }, isLogged) => {
            commit('setIsLogged', isLogged);
        },
        logout: ({ commit }) => {
            commit('logout');
        },
        addTryTimes: ({ commit }) => {
            commit('addTryTimes');
        },
        resetTryTimes: ({ commit }) => {
            commit('resetTryTimes');
        }
    }
})