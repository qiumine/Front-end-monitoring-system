<template>
  <div class="container">
    <div class="left">
      <div class="circle">
        <LeftCircle></LeftCircle>
      </div>
      <h3>成功率</h3>
    </div>
    <div class="right">
      <div class="small">
        <div id="url">
          <ul>
            <template v-for="(url, index) in ques">
              <li @click="greet">{{ index }}-发起{{ url.type }}的{{ url.method }}请求，路径为:{{ url.url }}</li>
            </template>
          </ul>
        </div>
      </div>
      <div class="small">
        <h3>返回信息：</h3>
        <br>
        <div class="info">
          <span v-for="(value, key) in body">
            {{ key }} : {{ value }}
            <br>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LeftCircle from "./leftCircle.vue";
import Vue from "vue"
export default {
  name: "Request",
  components: {
    LeftCircle
  },
  data() {
    return {
      ques: [
        { "type": "fetch", "method": "GET", "url": "/success", "body": { "kind": "stability", "type": "fetch", "startTime": "1661266057726", "url": "/success", "method": "GET", "endTime": "1661266057731", "duration": "5", "status": "0", "success": "False", "title": "\u524d\u7aef\u76d1\u63a7SDK", "timestamp": "1661266057731" } },
        { "type": "xhr", "method": "load", "url": "/error", "body": { "kind": "stability", "type": "xhr", "eventType": "load", "pathname": "/error", "status": "500-Internal Server Error", "duration": "5", "response": "", "params": "name=luo", "timestamp": "1661265503363" } },
      ],
      body: {},
    };
  },
  methods: {
    getData() {
      this.getApiInfo();
    },
    getApiInfo() {
      fetch("http://127.0.0.1:8000/getApiInfo/")
        .then((res) => res.json())
        .then((json) => {
          this.ques = json.data;
          this.body = this.ques[0].body;
        })
        .catch((err) => console.log("getApiInfo", err));
    },
    getUrlLi() {
      var url = new Vue({
        el: '#url',
        data: {},
      });

    },
    greet(e) {
      let index = (e.target.innerHTML).replace(/[^0-9]/ig, "");
      this.body = this.ques[index].body;
    },

  },
  created() {
    this.getData();
    // console.log('this.data', this.data);

  },

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
      // border: 2px solid #000;
      width: 100%;
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
      margin: 10px 0;
      overflow: auto;
      text-align: left;
      padding: 15px;
      h3{
        margin-left: 50px;
        margin-bottom: 0;
      }
      .info {
        margin-left: 50px;
      }
      #url {
        width: 100%;

        ul {
          width: 100%;
          text-align: left;
          li{
            list-style: none;
            margin: 5px;
            padding: 5px;
            border-radius: 5px;
          }

          li:hover{
            background-color: #eee;
            opacity: 0.7;
          }
        }
      }
    }
  }
}
</style>
