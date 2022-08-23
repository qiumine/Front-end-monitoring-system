<template>
  <div class="container">
    <div class="header">
      <div class="small">FP</div>
      <div class="small">FCP</div>
      <div class="small">DOM Ready</div>
    </div>
    <div class="main">DNS</div>
  </div>
</template>

<script>
export default {
  name: "Performance",
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
    height: 30%;
    width: 100%;
    margin: 10px;
    border: 1px solid #000;
    border-radius: 20px;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    .small {
      margin: 0 5px;
      flex: 1;
      height: 80%;
      border: 1px solid #000;
      border-radius: 15px;
      display: flex;
      justify-content: center;
      align-items: center;
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
