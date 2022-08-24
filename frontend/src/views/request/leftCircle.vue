<template>
    <div id="circle" ref="PieChart"></div>
</template>
 
<script>
import { Pie } from '@antv/g2plot'
let chartChange
export default {
    props: {
        value: {
            default() {
                return [
                    { type: 'xhr成功', value: 50 },
                    { type: 'fecth成功', value: 25 },
                    { type: '失败', value: 25 },
                ]
            },
        },
        Height: {
            type: Number,
            default: 0,
        },
    },
    mounted() {
        this.init()
    },
    methods: {
        async init() {
            await this.getApiErrorCharts();
            this.paint();
        },
        getApiErrorCharts() {
            fetch("http://127.0.0.1:8000/getApiErrorCharts/")
                .then((res) => res.json())
                .then((json) => {
                    this.value = json.data;
                    this.paint();
                })
                .catch((err) => console.log("getApiErrorCharts Failed", err));
        },
        paint() {
            chartChange = new Pie("circle", {
                data: this.value,
                height: this.Height,
                appendPadding: 10,
                angleField: 'value',
                colorField: 'type',
                radius: 1,
                // innerRadius: 0.64,   //圆环
                meta: {
                    value: {
                        formatter: (v) => `% ${v}`,
                    },
                },
                legend: {
                    ayout: 'vertical',
                    position: 'right',
                    flipPage: true,
                    offsetX: 0,
                    // title: {
                    //     text: '标题',
                    //     spacing: 8,
                    // },
                    itemValue: {
                        formatter: (text, item) => {
                            const items = this.value.filter((d) => d.type === item.value)
                            return items.length ? items.reduce((a, b) => a + b.value, 0) / items.length + '%' : '-'
                        },
                        style: {
                            opacity: 0.65,
                        },
                    },
                },
                label: {
                    type: 'outer',
                    content: '{name}-占比{percentage}',
                    style: {
                        fill: '#000',
                    },
                },
                // 添加 中心统计文本 交互
                interactions: [
                    { type: 'pie-legend-active' },
                    { type: 'element-active' },
                ],
            })
            chartChange.render();
        },
    },
}
</script>