<template>
    <div id="circle"></div>
</template>
 
<script>
import { Pie } from '@antv/g2plot'
export default {
    data() {
        return {
            piePlot: "",
            data: [
                { type: "xhr成功", value: 50 },
                { type: "fecth成功", value: 25 },
                { type: "失败", value: 25 },
            ],
        };
    },
    computed: {},
    methods: {
        init() {
            this.getApiErrorCharts();
        },
        getApiErrorCharts() {
            fetch("http://127.0.0.1:8000/getApiErrorCharts/")
                .then((res) => res.json())
                .then((json) => {
                    this.data = json.data;
                })
                .catch((err) => console.log("getApiErrorCharts Failed", err))
                .finally(() => this.paint());
        },
        paint() {
            this.chartChange = new Pie("circle", {
                data: this.data,
                appendPadding: 10,
                angleField: 'value',
                colorField: 'type',
                radius: .6,
                label: {
                    type: 'outer',
                    content: '{name}-{percentage}',
                    style: {
                        fill: '#000',
                    },
                },
                // 添加 中心统计文本 交互
                interactions: [
                    { type: 'pie-legend-active' },
                    { type: 'element-active' },
                ],
            });
            this.chartChange.render();
        },
    },
    created() {
        this.init();
    },
}
</script>
<style scoped>
#circle {
    width: 100%;
    height: 100%;
    left: 2%;
    position: relative;
}
</style>