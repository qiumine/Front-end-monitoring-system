<template>
  <div id="mainLeft"></div>
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
    getPVbyDay() {
      fetch("http://127.0.0.1:8000/getPVbyDay/")
        .then((res) => res.json())
        .then((json) => {
          this.data = json.data;
        })
        .catch((err) => console.log("getPVbyDay Failed", err))
        .finally(() => this.paint());
    },
    paint() {
      this.line = new Line("mainLeft", {
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
    this.getPVbyDay();
  },
};
</script>
<style scoped>
#mainLeft {
  width: 95%;
  height: 80%;
  left: 2.5%;
  top: 10%;
  position: relative;
}
</style>