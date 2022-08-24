 <template>
  <div>
    <div class="header">
      <div class="left">
        <div class="small">
          <div class="first">
            <div>
              <h3>{{ this.PV }}</h3>
              <span>浏览量(PV)</span>
            </div>
          </div>
        </div>
        <div class="small">
          <div class="first">
            <div>
              <h2>{{ this.newVisitor }}</h2>
              <span>新访客</span>
            </div>
          </div>
        </div>
      </div>
      <div class="center">
        <div class="center-container">
          <div class="title">
            <span>页面停留时间分段数量占比</span>
          </div>
          <div class="vue-container"><Center></Center></div>
        </div>
      </div>
      <div class="right">
        <div class="small">
          <div class="first">
            <div>
              <h3>{{ this.UV }}</h3>
              <span>访客数(UV)</span>
            </div>
          </div>
        </div>
        <div class="small">
          <div class="first">
            <div>
              <h3>{{ this.TP.average }}</h3>
              <span>TP页面停留时间(平均值)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="main">
      <div class="left">
        <div class="title">
          <span>PV趋势图</span>
        </div>
        <MainLeft></MainLeft>
      </div>
      <div class="right">
        <div class="title">
          <span>UV趋势图</span>
        </div>
        <div class="vue-container">
          <div id="mainRight"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Line } from "@antv/g2plot";

import Center from "./Center";
import MainLeft from "./MainLeft";

export default {
  name: "action",
  components: {
    Center,
    MainLeft,
  },
  data() {
    return {
      PV: 0,
      UV: 0,
      TP: {
        min: 0, //最小值
        max: 0, //最大值
        average: 0, //平均值
        all: [0], //全部值
      },
      line: "",
      data: [
        { date: "2022-08-22", value: 0 },
        { date: "2022-08-23", value: 0 },
      ],
    };
  },
  computed: {
    newVisitor() {
      return this.data.at(-1)?.value - this.data.at(-2)?.value || 0;
    },
  },
  methods: {
    getData() {
      this.getPV();
      this.getUV();
      this.getStaytime();
      this.getUVbyDay();
    },
    getPV() {
      fetch("http://127.0.0.1:8000/getPV/")
        .then((res) => res.json())
        .then((json) => {
          this.PV = json.data;
        })
        .catch((err) => console.log("getPV Failed", err));
    },
    getUV() {
      fetch("http://127.0.0.1:8000/getUV/")
        .then((res) => res.json())
        .then((json) => {
          this.UV = json.data;
        })
        .catch((err) => console.log("getUV Failed", err));
    },
    getStaytime() {
      fetch("http://127.0.0.1:8000/getStaytime/")
        .then((res) => res.json())
        .then((json) => {
          this.TP = json.data;
        })
        .catch((err) => console.log("getStaytime Failed", err));
    },
    getUVbyDay() {
      fetch("http://127.0.0.1:8000/getUVbyDay/")
        .then((res) => res.json())
        .then((json) => {
          this.data = json.data;
          this.paint();
        })
        .catch((err) => console.log("getUVbyDay Failed", err))
        .finally(() => this.paint());
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
    this.getData();
  },
};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  height: calc(50vh - 25px);
  background-color: #e9eef3;
  .left,
  .right {
    width: 25%;
    height: 100%;
  }
  .center {
    height: 100%;
    flex: 1;
    padding: 5px;
    margin: 0;
    display: flex;
    flex-direction: column;
    .center-container {
      height: 100%;
      width: 100%;
      border-radius: 5px;
      margin: 5px 0;
      background-color: #fff;
      .title {
        display: flex;
        margin: 5px;
      }
    }
  }
  .small {
    flex: 1;
    height: 46%;
    background: #fff;
    margin: 10px 7px;
    border-radius: 3px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .first {
    display: flex;
    justify-content: space-between;
    align-items: center;
    div {
      margin: 0 40px;
      text-align: center;
    }
  }
}
.main {
  display: flex;
  background-color: #e9eef3;
  height: calc(50vh - 25px);
  margin: 0;
  .left,
  .right {
    width: 50%;
    height: 100%;
    padding: 5px;
    margin: 0 0.5%;
    border-radius: 5px;
    background-color: #fff;
    .title span {
      margin: 10px;
    }
  }
}
.vue-container {
  width: 100%;
  height: 100%;
  margin: 10px;
}
#mainRight {
  width: 95%;
  height: 80%;
  left: 2.5%;
  top: 10%;
  position: relative;
}
</style>