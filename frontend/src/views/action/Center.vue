<template>
  <div id="center"></div>
</template>

<script>
import { Line } from "@antv/g2plot";
// import { mapState } from "vuex";
export default {
  data() {
    return {
      line: "",
    };
  },
  computed: {},
  methods: {
    init() {
      //待改
      fetch(
        "http://127.0.0.1:8000/getJsError/"
      )
        .then((res) => res.json())
        .then((data) => {
          this.line = new Line("center", {
            data,
            padding: "auto",
            xField: "Date",
            yField: "scales",
            xAxis: {
              // type: 'timeCat',
              tickCount: 5,
            },
          });
          this.line.render();
        });
    },
  },
  created() {
    this.init();
  },
  mounted() {},
};
</script>
<style scoped>
#center {
  width: 95%;
  height: 80%;
  left:2%;
  position: relative;
}
</style>