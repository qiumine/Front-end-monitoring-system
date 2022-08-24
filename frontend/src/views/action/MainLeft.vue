<template>
  <div id="mainLeft"></div>
</template>

<script>
import { Line } from "@antv/g2plot";
export default {
  data() {
    return {
      line: "",
      data:[
                {
                    "Date": "2010-01",
                    "scales": 1998
                },
                {
                    "Date": "2010-02",
                    "scales": 1850
                },
                {
                    "Date": "2010-03",
                    "scales": 1720
                },
                {
                    "Date": "2010-04",
                    "scales": 1818
                },
            ]
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
          this.line = new Line("mainLeft", {
            data:this.data,
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
#mainLeft {
  width: 95%;
  height: 80%;
  left:2%;
  position: relative;
}
</style>