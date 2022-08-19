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
  </div>
</template>

<script>
import Center from "./Center";
export default {
  name: "jsError",
  components: {
    Center,
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  height: 50vh;
  background-color: #e9eef3;
  .left {
    width: 25%;
    height: 100%;
  }
  .center {
    height: 100%;
    flex: 1;
    padding: 10px;
    display: flex;
    flex-direction: column;
    .center-container {
      height: 100%;
      background-color: #fff;
      .title {
        display: flex;
        margin: 5px;
      }
    }
  }
  .right {
    width: 25%;
    height: 100%;
  }
  .small {
    flex: 1;
    height: 46%;
    background: #fff;
    margin: 2.5% 2%;
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
</style>