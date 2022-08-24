<template>
  <div class="container">
    <div class="header">
      <div class="small" title="First Paint">
        <h2>FP:</h2>
        <h1>{{this.FP}}ms</h1>
      </div>
      <div class="small" title="First ContentFul Paint">
        <h2>FCP:</h2>
        <h1>{{this.FCP}}ms</h1>
      </div>
      <div class="small" title="DOM Content Loaded Time">
        <h2>DOM Ready:</h2>
        <h1>{{this.DOM}}s</h1>
      </div>
    </div>
    <div class="header">
      <div class="small" title="发起请求到第一个字节到达的时间">
        <h2>ttfbtime:</h2>
        <h1>{{this.ttfb}}s</h1>
      </div>
      <div class="small" title="接口响应时间">
        <h2>responsetime:</h2>
        <h1>{{this.responsetime}}s</h1>
      </div>
      <div class="small" title="页面加载完成的总时间">
        <h2>load time:</h2>
        <h1>{{this.LoadTime}}ms</h1>
      </div>
    </div>
    <div class="header">
      <div class="small" title="inputDelay">
        <h2>inputDelay:</h2>
        <h1>{{this.inputDelay}}ms</h1>
      </div>
      <div class="small" title="（largest contentful Paint），最大内容渲染时间。">
        <h2>LCP:</h2>
        <h1>{{this.LCP}}ms</h1>
      </div>
      <div class="small" title="（First Meaningful Paint），首次渲染有意义的内容的时间">
        <h2>FMP:</h2>
        <h1>{{this.FMP}}ms</h1>
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
          this.FP = json.data.firstPaint;
        })
        .catch((err) => console.log("getFP Failed", err));
    },
    getFCP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.FCP = json.data.firstContentFulPaint;
        })
        .catch((err) => console.log("getFCP Failed", err));
    },
    getDOM(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.DOM = json.data.domContentLoadedTime;
        })
        .catch((err) => console.log("getDOM Failed", err));
    },
    getttfb(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.ttfb = json.data.ttfbTime;
        })
        .catch((err) => console.log("getttfb Failed", err));
    },
    getresponse(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.responsetime = json.data.responseTime;
        })
        .catch((err) => console.log("getresponsetime Failed", err));
    },
    getLoadTime(){
        fetch("http://127.0.0.1:8000/getTiming/")
        .then((res) => res.json())
        .then((json) => {
          this.LoadTime = json.data.loadTime;
        })
        .catch((err) => console.log("getLoadTime Failed", err));
    },
    getinputDelay(){
        fetch("http://127.0.0.1:8000/getFirstInputDelay/")
        .then((res) => res.json())
        .then((json) => {
          this.inputDelay = json.data.inputDelay;
        })
        .catch((err) => console.log("getinputDelay Failed", err));
    },
    getLCP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.LCP = json.data.largestContentfulPaint;
        })
        .catch((err) => console.log("getLCP Failed", err));
    },
    getFMP() {
      fetch("http://127.0.0.1:8000/getPaint/")
        .then((res) => res.json())
        .then((json) => {
          this.FMP = json.data.firstMeaningfulPaint;
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
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: calc(100vh - 50px);
  margin: 0;
  padding: 5px;
  background-color: #e9eef3;
  overflow: hidden;
  .header {
    height: 33%;
    width: 100%;
    margin: 10px;
    border: 1px solid #000;
    border-radius: 20px;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    .small {
      margin: 0 20px;
      flex: 1;
      height: 80%;
      border: 1px solid #000;
      border-radius: 15px;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
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
