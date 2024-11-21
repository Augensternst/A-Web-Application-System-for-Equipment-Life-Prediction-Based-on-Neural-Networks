<script setup lang="ts">
import { ElMenu, ElSubMenu, ElIcon, ElMenuItem, ElText } from 'element-plus'
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()
const MenuList = ref([
    {
        index: '1',
        title: '首页看板',
        icon: 'HomeFilled',
        children: [
            {
                index: '1-1',
                title: '首页看板',
            },
        ]
    },
    {
        index: '2',
        title: '模型中心',
        icon: 'Menu',
        children: [
            {
                index: '2-1',
                title: '模型中心',
            },
        ]
    },
    {
        index: '3',
        title: '数据中心',
        icon: 'Histogram',
        children: [
            {
                index: '3-1',
                title: '数据中心',
            }
        ]
    },
    {
        index: '4',
        title: '组件中心',
        icon: 'HelpFilled',
        children: [
            {
                index: '4-1',
                title: '组件列表',
            },
            {
                index: '4-2',
                title: '添加组件',
            }
        ]
    }
])
//@ts-ignore
const handleSelect = (index, indexPath) => {
    // 上级html路由为：<el-main><router-view name = "home-main" /></el-main>，我们只对home-main部分进行路由跳转
    console.log(index, indexPath)
    switch (index) {
        case '1-1':
            router.push({ name: 'home-overview'});
            break;
        case '2-1':
            router.push({ name: 'model-recorder' });
            break;
        case '3-1':
            router.push({ name: 'data-recorder' });
            break;
        case '3-2':
            router.push({ name: 'target-notification' });
            break;
        case '4-1':
            router.push({ name: 'analyse-trans' });
            break;
        case '4-2':
            router.push({ name: 'component-add' });
            break;
        default:
            break;
    }
}

</script>

<template>
    <el-menu default-active="1" @select="handleSelect">
        <el-sub-menu v-for="(item, i) in MenuList" :key="i" :index="item.title" :icon="item.icon">
            <template #title>
                <el-icon size="32">
                    <!--这里插入的标签名称对应于item.icon-->
                    <component :is="item.icon"></component>
                </el-icon>
                <h3>{{ item.title }}</h3><!--父菜单名称-->
            </template>
            <el-menu-item v-for="(child, j) in item.children" :key="j" :index="child.index">
                <el-text size="large">
                        <h4>{{ child.title }}</h4>
                </el-text>
            </el-menu-item>
        </el-sub-menu>
    </el-menu>
</template>