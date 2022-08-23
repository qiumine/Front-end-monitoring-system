<template>
  <div class="container">
    <div class="header">
      <div class="sum">
        <div class="circle">综合性能</div>
      </div>
      <div class="right">
        <div class="circle">JS异常</div>
        <div class="circle">白屏异常</div>
        <div class="circle">接口异常</div>
        <div class="circle">性能异常</div>
      </div>
    </div>
    <div class="main">
      <div class="small">JS异常趋势图</div>
      <div class="small">白屏异常趋势图</div>
      <div class="small">接口异常趋势图</div>
      <div class="small">性能异常趋势图</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Abnormal",
};
</script>

<style lang="scss" scoped>
* {
  box-sizing: border-box;
}
.container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 50px);
  background-color: #e9eef3;
  .header {
    width: calc(100% - 20px);
    height: 25vh;
    background: #fff;
    margin: 20px 10px;
    border-radius: 20px;
    border: 1px solid #000;
    display: flex;
    .sum {
      width: 25%;
      height: 100%;
      border-right: 1px solid #000;
      display: flex;
      justify-content: center;
      align-items: center;
      .circle {
        border: 2px solid #000;
        border-radius: 50%;
        height: 75%;
        aspect-ratio: 1/1;
        display: flex;
        justify-content: center;
        align-items: center;
      }
    }
    .right {
      flex: 1;
      display: flex;
      justify-content: space-evenly;
      align-items: center;
      .circle {
        border: 2px solid red;
        border-radius: 50%;
        aspect-ratio: 1/1;
        height: 60%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
      }
    }
  }
  .main {
    height: 75vh;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    .small {
      width: 26.5vw;
      height: 30vh;
      background-color: #fff;
      border-radius: 25px;
      border: 1px solid #000;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 2vh 1vw;
      padding: 0;
    }
  }
}
</style>
