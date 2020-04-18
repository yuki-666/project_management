import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: window.localStorage.getItem('user' || '[]') == null ? '' : JSON.parse(window.localStorage.getItem('user' || '[]')).username
    },
    zuid: '' || localStorage.getItem('zuid'),
    zcareer: '' || localStorage.getItem('zcareer'),
    zprojectid: '' || localStorage.getItem('zprojectid')
  },
  getters: { uid: (state) => state.zuid, career: (state) => state.zcareer, projectid: (state) => state.zprojectid },
  mutations: {
    login (state, user) {
      state.user = user
      window.localStorage.setItem('user', JSON.stringify(user))
    },
    handleUid: (state, zuid) => {
      state.zuid = zuid
      localStorage.setItem('zuid', zuid)
    },
    handleCareer: (state, zcareer) => {
      state.zcareer = zcareer
      localStorage.setItem('zcareer', zcareer)
    },
    handleProjectid: (state, zprojectid) => {
      state.zprojectid = zprojectid
      localStorage.setItem('zprojectid', zprojectid)
    }
  }
})
