 <template>
  <div>
    <div class="header">
      <div class="left">
        <div class="small">
          <div class="first">
            <div>
              <h3>8</h3>
              <span>JS错误数</span>
            </div>
            <div>
              <h3>1.52%</h3>
              <span>JS错误率</span>
            </div>
          </div>
        </div>
        <div class="small">
          <div class="first">
            <div>
              <h3>0</h3>
              <span>API错误数</span>
            </div>
            <div>
              <h3>100%</h3>
              <span>API请求成功率</span>
            </div>
          </div>
        </div>
      </div>
      <div class="center">
        <div class="center-container">
          <div class="title">
            <span>待改</span>
          </div>
          <Center></Center>
        </div>
      </div>
      <div class="right">
        <div class="small">
          <div class="first">
            <div>
              <h3>938ms</h3>
              <span>首次渲染耗时</span>
            </div>
          </div>
        </div>
        <div class="small">
          <div class="first">
            <div>
              <h3>732</h3>
              <span>资源错误</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="main">
      <div class="left">
        <div class="title">
          <span>待改</span>
        </div>
        <MainLeft></MainLeft>
      </div>
      <div class="right">
        <div class="title">
          <span>待改</span>
        </div>
        <MainRight></MainRight>
      </div>
    </div>
  </div>
</template>

<script>
import Center from "./Center";
import MainLeft from "./MainLeft";
import MainRight from "./MainRight";
export default {
  name: "action",
  components: {
    Center,
    MainLeft,
    MainRight,
  },
  methods: {},
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
  }
}
</style>