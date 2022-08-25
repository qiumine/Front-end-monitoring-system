<template>
  <div class="container">
    <div class="header">
      <div class="small" title="First Paint">
        <h2>FP:</h2>
        <span>{{this.FP}}ms</span>
      </div>
      <div class="small" title="First ContentFul Paint">
        <h2>FCP:</h2>
        <span>{{this.FCP}}ms</span>
      </div>
      <div class="small" title="DOM Content Loaded Time">
        <h2>DOM Ready:</h2>
        <span>{{this.DOM}}ms</span>
      </div>
    </div>
    <div class="header">
      <div class="small" title="发起请求到第一个字节到达的时间">
        <h2>ttfbtime:</h2>
        <span>{{this.ttfb}}ms</span>
      </div>
      <div class="small" title="接口响应时间">
        <h2>responsetime:</h2>
        <span>{{this.responsetime}}ms</span>
      </div>
      <div class="small" title="页面加载完成的总时间">
        <h2>load time:</h2>
        <span>{{this.LoadTime}}ms</span>
      </div>
    </div>
    <div class="header">
      <div class="small" title="inputDelay">
        <h2>inputDelay:</h2>
        <span>{{this.inputDelay}}ms</span>
      </div>
      <div class="small" title="（largest contentful Paint），最大内容渲染时间。">
        <h2>LCP:</h2>
        <span>{{this.LCP}}ms</span>
      </div>
      <div class="small" title="（First Meaningful Paint），首次渲染有意义的内容的时间">
        <h2>FMP:</h2>
        <span>{{this.FMP}}ms</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Performance",
  data() {
    return {
      FP: 0,
      FCP: 0,
      DOM: 0,
      ttfb: 0,
      responsetime: 0,
      LoadTime: 0,
      inputDelay: 0,
      LCP: 0,
      FMP: 0,
    };
  },
  methods: {
    getData() {
      this.getFP();
      this.getFCP();
      this.getDOM();
      this.getttfb();
      this.getresponse();
      this.getLoadTime();
      this.getinputDelay();
      this.getLCP();
      this.getFMP();
    },
    getFP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.FP = parseFloat(json.data.firstPaint).toFixed(2);
        })
        .catch((err) => console.log("getFP Failed", err));
    },
    getFCP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.FCP = parseFloat(json.data.firstContentFulPaint).toFixed(2);
        })
        .catch((err) => console.log("getFCP Failed", err));
    },
    getDOM(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.DOM = parseFloat(json.data.domContentLoadedTime).toFixed(2);
        })
        .catch((err) => console.log("getDOM Failed", err));
    },
    getttfb(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.ttfb = parseFloat(json.data.ttfbTime).toFixed(2);
        })
        .catch((err) => console.log("getttfb Failed", err));
    },
    getresponse(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.responsetime = parseFloat(json.data.responseTime).toFixed(2);
        })
        .catch((err) => console.log("getresponsetime Failed", err));
    },
    getLoadTime(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.LoadTime = parseFloat(json.data.loadTime).toFixed(2);
        })
        .catch((err) => console.log("getLoadTime Failed", err));
    },
    getinputDelay(){
        fetch("http://127.0.0.1:8000/getFirstInputDelay/")
        .then((res) => res.json())
        .then((json) => {
          this.inputDelay = parseFloat(json.data.inputDelay).toFixed(2);
        })
        .catch((err) => console.log("getinputDelay Failed", err));
    },
    getLCP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.LCP = parseFloat(json.data.largestContentfulPaint).toFixed(2);
        })
        .catch((err) => console.log("getLCP Failed", err));
    },
    getFMP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.FMP = parseFloat(json.data.firstMeaningfulPaint).toFixed(2);
        })
        .catch((err) => console.log("getFMP Failed", err));
    }
  },
  created() {
    this.getData();
  },
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  border-style:none;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: calc(100vh - 50px);
  margin: 0;
  padding: 20px;
  background-color: #e9eef3;
  overflow: hidden;
  .header {
    height: 30%;
    width: 95%;
    margin: 10px;
    border: 0px solid #000;
    border-radius: 20px;
    background-color: #e9eef3;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .small {
      margin: 0 20px;
      flex: 1;
      height: 90%;
      border: 0px solid #000;
      border-radius: 30px;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      background-color: #fff;
    }
  .small:hover {
      transform: scale(1.15);
  }
  .small span{
    font-size: larger;
  }
  .main {
    flex: 1;
    width: 100%;
    border: 1px solid #000;
    background: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
