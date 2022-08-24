<template>
  <div id="mainRight"></div>
</template>

<script>
import { Line } from "@antv/g2plot";
export default {
  data() {
    return {
      line: "",
      data: [
        { date: "2022-08-22", value: 0 },
        { date: "2022-08-23", value: 0 },
      ],
    };
  },
  computed: {},
  methods: {
    async init() {
      await this.getUVbyDay();
      this.paint();
    },
    getUVbyDay() {
      fetch("http://127.0.0.1:8000/getUVbyDay/")
        .then((res) => res.json())
        .then((json) => {
          this.data = json.data;
          this.paint();
        })
        .catch((err) => console.log("getUVbyDay Failed", err));
    },
    paint() {
      this.line = new Line("mainRight", {
        data: this.data,
        padding: "auto",
        xField: "date",
        yField: "value",
        xAxis: {
          // type: 'timeCat',
          tickCount: 5,
        },
      });
      this.line.render();
    },
  },
  created() {
    this.init();
  },
};
</script>
<style scoped>
#mainRight {
  width: 95%;
  height: 80%;
  left: 2.5%;
  top: 10%;
  position: relative;
}
</style>