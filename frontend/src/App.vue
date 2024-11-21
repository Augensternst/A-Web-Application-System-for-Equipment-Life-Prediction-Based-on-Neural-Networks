<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from "vue-router";
import 'element-plus/dist/index.css'
const router = useRouter();

onMounted(() => {
    router.push({
        path: "/login",
        replace: true
    });
});
</script>

<template>
	<router-view/>
</template>

<style scoped>
.logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
}

.logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
}
</style>