import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import * as VueJsonp from 'vue-jsonp'
import echarts from 'echarts'

Vue.use(VueJsonp)
Vue.use(VueResource)
Vue.prototype.$echarts = echarts

new Vue({
    el: '#app',
    render: h => h(App)
})