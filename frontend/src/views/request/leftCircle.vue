<template>
    <div id="circle" ref="PieChart"></div>
</template>
 
<script>
import { Pie } from '@antv/g2plot'
let chartChange
export default {
    name: 'PieChart',
    props: {
        value: {
            type: Array,
            default() {
                return [
                    { type: '成功', value: 75 },
                    { type: '失败', value: 25 },
                ]
            },
        },
        Height: {
            type: Number,
            default: 0,
        },
    },
    // 监听
    watch: {
        value: {
            handler(newVal, oldVal) {
                console.log(newVal)
                // 更新数据
                chartChange.changeData(newVal)

                // 销毁后再渲染
                // chartChange.destroy()
                // this.init()
            },
            deep: true, //深度监听
            // immediate: true,
        },
    },
    mounted() {
        this.init()
    },
    methods: {
        init() {
            chartChange = new Pie(this.$refs.PieChart, {
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
            chartChange.render()
        },
    },
}
</script>