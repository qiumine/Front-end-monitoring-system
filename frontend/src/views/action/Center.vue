<template>
  <div id="center"></div>
</template>

<script>
import { Pie } from "@antv/g2plot";
export default {
  data() {
    return {
      piePlot: "",
      data: [
        { type: "<5s", value: 0 },
        { type: "5s~60s", value: 0 },
        { type: "1min~5min", value: 0 },
        { type: "5min~15min", value: 0 },
        { type: ">15min", value: 0 },
      ],
    };
  },
  computed: {},
  methods: {
    init() {
      this.getStaytimeCharts();
      this.paint();
    },
    getStaytimeCharts() {
      fetch("http://127.0.0.1:8000/getStaytimeCharts/")
        .then((res) => res.json())
        .then((json) => {
          this.data = json.data;
        })
        .catch((err) => console.log("getStaytimeCharts Failed", err));
    },
    paint() {
      this.piePlot = new Pie("center", {
        appendPadding: 10,
        data: this.data,
        angleField: "value",
        colorField: "type",
        radius: 0.9,
        label: {
          type: "inner",
          offset: "-30%",
          content: ({ percent }) => `${(percent * 100).toFixed(0)}%`,
          style: {
            fontSize: 14,
            textAlign: "center",
          },
        },
        interactions: [{ type: "element-active" }],
      });
      this.piePlot.render();
    },
  },
  mounted() {
    this.init();
  },
};
</script>
<style scoped>
#center {
  width: 95%;
  height: 80%;
  left: 2%;
  position: relative;
}
</style>