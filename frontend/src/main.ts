import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routers/router.ts'
import ECharts from 'vue-echarts'
import VueECharts from 'vue-echarts'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import store from './store'
import 'echarts'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.use(router).use(store).use(ElementPlus)
app.component('v-chart', VueECharts).component('e-chart', ECharts)
app.mount('#app')