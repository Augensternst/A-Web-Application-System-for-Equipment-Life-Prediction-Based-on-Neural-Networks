<script setup lang="ts">
import {CanvasRenderer} from 'echarts/renderers';
import {BarChart, PieChart} from 'echarts/charts';
import {use} from 'echarts/core';
import {ref, onMounted} from "vue";
import VChart from 'vue-echarts';
import axiosInstance from "../../axios";
import {ElMessage } from "element-plus";

use([BarChart, PieChart, CanvasRenderer]);

const jsonHeaders = {
  'Content-Type': 'application/json',
};
let pie1 = ref<any>([])
let pie2 = ref<any>([])
let line1 = ref<any>([])
let gauges = ref<any[]>([])

async function fetchPie1Data() {
  const res = axiosInstance.get("model/style", {headers: jsonHeaders});
  const response = await res
  if (response.status !== 200) {
    console.error('Error:', response.status, response.statusText);
    ElMessage.error('获取数据失败: ' + response.statusText);
    return;
  }
  if(response.data.code !== 200){
    console.error('Error:', response.data.message);
    ElMessage.error('获取数据失败: ' + response.data.message);
    return;
  }

  const data = await response.data.data
  let pieData = [];
  for (const key in data) {
    pieData.push({
      name: key,
      value: data[key].toFixed(2)
    });
  }
  pie1.value = {
    title: {
      text: '模型占比',
      left: 'center',
    },
    series: [
      {
        name: '模型',
        type: 'pie',
        radius: '50%',
        center: ['60%', '40%'],
        data: pieData
      }
    ],
    legend: {
      orient: 'vertical',
      left: 'left',
      data: pieData.map((name: { name: string }) => name.name),
    },
    emphasis: {
      itemStyle: {
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)',
      },
    },
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b} : {c} ({d}%)',
    },
  }
}



async function fetchPie2Data() {
  const res = axiosInstance.get("/component/location_count", {headers: jsonHeaders});
  const response = await res;
  if (response.status !== 200) {
    console.error('Error:', response.status, response.statusText);
    ElMessage.error('获取数据失败: ' + response.statusText);
    return;
  }
  if(response.data.code !== 200){
    console.error('Error:', response.data.code, response.data.message);
    ElMessage.error('获取数据失败: ' + response.data.message);
    return;
  }
  const data = await response.data.data;
  let pieData = [];
  for (const key in data) {
    pieData.push({
      name: key,
      value: data[key]
    });
  }
  pie2.value = {
    title: {
      text: '各位置组件分布',
      left: 'center',
    },
    series: [
      {
        name: '应用',
        type: 'pie',
        radius: '50%',
        center: ['50%', '40%'],
        data: pieData,
      }
    ],
    legend: {
      orient: 'vertical',
      left: 'left',
      data: pieData.map((item: { name: string }) => item.name),
    },
    emphasis: {
      itemStyle: {
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)',
      },
    },
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b} : {c} ({d}%)',
    },
  }
}

fetchPie1Data();
fetchPie2Data();

line1.value = {
  title: {
    text: '监控设备的数量'
  },
  tooltip: {},
  xAxis: {
    data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
  },
  yAxis: {},
  series: [
    {
      name: '2022年',
      type: 'line',
      data: Array.from({length: 12}, () => Math.floor(Math.random() * 100))
    },
    {
      name: '2023年',
      type: 'line',
      data: Array.from({length: 12}, () => Math.floor(Math.random() * 100))
    }
  ]
}
for (let i = 0; i < 3; i++) {
  gauges.value[i] = {
    title: {
      text: '指标' + i,
      left: 'center',
    },
    series: [
      {
        name: '指标' + i,
        type: 'gauge',
        detail: {
          formatter: '{value}%',
          fontSize: 8  // 设置字体大小
        },
        data: [{value: (Math.random() * 100).toFixed(2)}]
      }
    ]
  }
}


onMounted(async () => {
  await fetchPie1Data();
  await fetchPie2Data();
  window.setInterval(fetchPie1Data, 60000);
});
</script>


<template>
  <el-row :gutter="20" style="width: 100%;height: 100%">
    <el-col :span="15">
      <div style="height: 40%;">
        <v-chart class="chart" :option="line1" autoresize/>
      </div>
      <el-row :gutter="20" style="height:60%;">
        <el-col :span="10">
          <v-chart class="chart" :option="pie1" autoresize/>
        </el-col>
        <el-col :span="10">
          <v-chart class="chart" :option="pie2" autoresize/>
        </el-col>
      </el-row>
    </el-col>
    <el-col :span="5" style="height: 70%;">
      <div style="height: 47%;" v-for="gauge in gauges">
        <v-chart class="chart" :option="gauge" autoresize/>
      </div>
    </el-col>
  </el-row>
</template>
