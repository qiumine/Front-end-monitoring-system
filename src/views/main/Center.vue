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
        "https://gw.alipayobjects.com/os/bmw-prod/1d565782-dde4-4bb6-8946-ea6a38ccf184.json"
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