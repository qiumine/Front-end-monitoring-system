<template>
  <div class="container">
    <div class="left">
      <div class="circle"></div>
      <h3>成功率</h3>
    </div>
    <div class="right">
      <div class="small">请求链路</div>
      <div class="small">返回信息</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Request",
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  margin: 0;
  padding: 20px;
  height: calc(100vh - 50px);
  background-color: #e9eef3;
  overflow: hidden;
  text-align: center;
  .left,
  .right {
    width: 50%;
    height: 100%;
    margin: 0 10px;
  }
  .left {
    background-color: #fff;
    border-radius: 15%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    .circle {
      border: 2px solid #000;
      width: 75%;
      aspect-ratio: 1/1;
      border-radius: 50%;
      margin: 20px 0;
    }
  }
  .right {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    .small {
      width: 100%;
      aspect-ratio: 2/1;
      background-color: #fff;
      border-radius: 25px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 10px 0;
    }
  }
}
</style>
