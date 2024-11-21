import {createRouter, createWebHistory} from 'vue-router'
import {ElMessage} from "element-plus";
//@ts-ignore
import {useStore} from 'vuex'
import {useAuth} from '../composables/auth'

const _routes = [
    {
        path: '/home',
        component: () => import('../components/home/Home.vue'),
        children: [
            {
                path: '', // home的默认孩子路由
                name: 'home-default',
                component: () => import('../components/Overview/Overview.vue'),
            },
            {
                path: 'overview',
                name: 'home-overview',
                component: () => import('../components/Overview/Overview.vue'),
            }
        ],
    },
    {
        path:'/login',
        component:()=>import('../components/login/login.vue'),
        name:'login',
    },
    {
        path: '/model',
        component: () => import('../components/home/Home.vue'),
        children: [
            {
                path: 'overview',
                name: 'model-recorder',
                component: () => import('../components/modelCenter/ModelCenter.vue'),
            },
            {
                path: 'modeladd',
                name: 'model-add',
                component: () => import('../components/modelCenter/ModelAdd.vue'),
            }
        ],
    },
    {
        path: '/data',
        component: () => import('../components/home/Home.vue'),
        children: [
            {
                path: 'overview',
                name: 'data-recorder',
                component: () => import('../components/dataCenter/DataCenter.vue'),
            },
            {
                path: 'notification',
                name: 'target-notification',
                component: () => import('../components/home/Home.vue'),
            },
            { // 专门刷新页面的路由
                path: 'refreshtarget',
                name: 'target-refreshtarget',
                component: () => import('../components/home/Home.vue'),
            },
            {
                path: 'refreshnotification',
                name: 'target-refreshnotification',
                component: () => import('../components/home/Home.vue'),
            }
        ]
    },
    {
        path: '/analyse',
        component: () => import('../components/home/Home.vue'),
        children: [
            {
                path: 'trans',
                name: 'analyse-trans',
                component: () => import('../components/componentCenter/LifeForecast.vue'),
            },
            {
                path: 'componentadd',
                name: 'component-add',
                component: () => import('../components/componentCenter/ComponentAdd.vue'),
            },
        ]
    },
    {
        path: '/register',
        name: 'register',
        component: () => import('../components/register/register.vue'),
    },
    {
        path: '/resetPasswd',
        component: () => import('../components/home/Home.vue'),
    }
]
const router = createRouter({
    routes: _routes,
    history: createWebHistory(),
})
router.beforeEach(async (to, from, next) => {
    const token = useAuth().getToken()
    if(!token&&to.name!=='login'&&to.name!=='register'&&to.name!=='resetPasswd'){
        ElMessage.error('请先登录')
        return next({name:'login'})
    }
    if(token&&to.name==='login'){
        console.log(from.name)
        if(from.name&&from.name!=='register'){
            return next({name:from.name})
        }
        else{
            return next({name:'home-default'})
        }
    }
    next()
})
export default router