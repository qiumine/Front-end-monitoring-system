<template>
  <div class="container">
    <div class="header">
      <div class="sum">
        <div id="Errors" />
      </div>
      <div class="right">
        <a class="circle" href="#jsReason">
          <p>
            JS异常: {{ JsError.total }}
            <br>
          </p>
        </a>
        <a class="circle" href="#blankReason">
          <p>
            白屏异常: {{ blank }}
            <br>
          </p>
        </a>
        <a class="circle" href="#apiReason">
          <p>
            接口异常: {{ apiError }}
            <br>
          </p>
        </a>
        <a class="circle" href="#resourceReason">
          <p>
            资源异常: {{ resourceError }}
            <br>
          </p>
        </a>
      </div>
    </div>
    <div class="main">
      <div id="jsTrend" class="small">JS异常趋势图</div>
      <div id="blankTrend" class="small">白屏异常趋势图</div>
      <div id="apiTrend" class="small">接口异常趋势图</div>
      <div id="resourceTrend" class="small">资源异常趋势图</div>

    </div>
    <div class="reason">
      <div id="jsReason" class="small">
        <h2>JS异常</h2>
        <ul>
          <li v-for="item in JsErrorInfo">
            <span class="time">{{ item.time }}</span>
            &nbsp;
            <span class="type">{{ item.type }}</span>
            :&nbsp;
            <span class="message">{{ item.message }}</span>
            <a>{{ item.stack }}</a>
          </li>
        </ul>
      </div>
      <div id="blankReason" class="small">
        <h2>白屏异常</h2>
        <ul>
          <li v-for="item in blankInfo">
            <span class="time">{{ item.time }}</span>
            &nbsp;
            <span class="type">{{ item.type }}</span>
            :&nbsp;
            <span class="message">{{ item.message }}</span>
          </li>
        </ul>
      </div>
      <div id="apiReason" class="small">
        <h2>接口异常</h2>
        <ul>
          <li v-for="item in apiErrorInfo">
            <span class="time">{{ item.time }}</span>
            &nbsp;
            <span class="type">{{ item.type }} &nbsp; ({{ item.method }})</span>
            :&nbsp;
            <span class="message">{{ item.status }}</span>
            <a>{{ item.url }}</a>
          </li>
        </ul>
      </div>
      <div id="resourceReason" class="small">
        <h2>资源异常</h2>
        <ul>
          <li v-for="item in resourceErrorInfo">
            <span class="time">{{ item.time }}</span>
            &nbsp;
            <span class="type">{{ item.type }}</span>
            :&nbsp;
            <span class="message">{{ item.message }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { Line } from '@antv/g2plot'
import { Pie } from '@antv/g2plot'
export default {
  data() {
    return {
      JsError: {},
      JsErrorInfo: [],
      apiError: {},
      apiErrorInfo: [],
      blank: 0,
      blankInfo: [],
      resourceError: 0,
      resourceErrorInfo: [],
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      this.getErrors()
      this.getJsError()
      this.getBlank()
      this.getApiError()
      this.getResourceError()
      this.getTrend()
    },
    getTrend() {
      fetch(
        'http://127.0.0.1:8000/getJsErrorbyDay/'
      )
        .then((res) => res.json())
        .then((data) => {
          this.line = new Line('jsTrend', {
            data: data.data,
            padding: 'auto',
            xField: 'date',
            yField: 'value',
            seriesField: 'kind',
            xAxis: {
              tickCount: 5
            }
          })
          this.line.render()
        })
      fetch(
        'http://127.0.0.1:8000/getBlankbyDay/'
      )
        .then((res) => res.json())
        .then((data) => {
          this.line = new Line('blankTrend', {
            data: data.data,
            padding: 'auto',
            xField: 'date',
            yField: 'value',
            xAxis: {
              tickCount: 5
            }
          })
          this.line.render()
        })
      fetch(
        'http://127.0.0.1:8000/getResourceErrorbyDay/'
      )
        .then((res) => res.json())
        .then((data) => {
          this.line = new Line('resourceTrend', {
            data: data.data,
            padding: 'auto',
            xField: 'date',
            yField: 'value',
            xAxis: {
              tickCount: 5
            }
          })
          this.line.render()
        })
      fetch(
        'http://127.0.0.1:8000/getApiErrorbyDay/'
      )
        .then((res) => res.json())
        .then((data) => {
          this.line = new Line('apiTrend', {
            data: data.data,
            padding: 'auto',
            xField: 'date',
            yField: 'value',
            seriesField: 'kind',
            xAxis: {
              tickCount: 5
            }
          })
          this.line.render()
        })
    },
    getErrors() {
      fetch('http://127.0.0.1:8000/getErrors/')
        .then((res) => res.json())
        .then((data) => {
          this.piePlot = new Pie('Errors', {
            appendPadding: 20,
            data: data.data,
            angleField: 'value',
            colorField: 'type',
            radius: 0.7,
            innerRadius: 0.6,
            label: {
              type: 'inner',
              offset: '-50%',
              content: '{value}',
              style: {
                textAlign: 'center',
                fontSize: 10
              }
            },
            interactions: [{ type: 'element-selected' }, { type: 'element-active' }],
            statistic: {
              title: false,
              content: {
                style: {
                  whiteSpace: 'pre-wrap',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis'
                },
                content: '总览'
              }
            }
          })
          this.piePlot.render()
        })
        .catch((err) => console.log('getErrors Failed', err))
    },
    getJsError() {
      fetch('http://127.0.0.1:8000/getJsError/')
        .then((res) => res.json())
        .then((json) => {
          this.JsError = json.data
        })
        .catch((err) => console.log('getJsError Failed', err))
      fetch('http://127.0.0.1:8000/getJsErrorInfo/')
        .then((res) => res.json())
        .then((json) => {
          this.JsErrorInfo = json.data
        })
        .catch((err) => console.log('getJsErrorInfo Failed', err))
    },
    getBlank() {
      fetch('http://127.0.0.1:8000/getBlank/')
        .then((res) => res.json())
        .then((json) => {
          this.blank = json.data
        })
        .catch((err) => console.log('getBlank Failed', err))
      fetch('http://127.0.0.1:8000/getBlankErrorInfo/')
        .then((res) => res.json())
        .then((json) => {
          this.blankInfo = json.data
        })
        .catch((err) => console.log('getBlankErrorInfo Failed', err))
    },
    getApiError() {
      fetch('http://127.0.0.1:8000/getApiError/')
        .then((res) => res.json())
        .then((json) => {
          this.apiError = json.data.xhr.error + json.data.fetch.error
        })
        .catch((err) => console.log('getApiError Failed', err))
      fetch('http://127.0.0.1:8000/getApiErrorInfo/')
        .then((res) => res.json())
        .then((json) => {
          this.apiErrorInfo = json.data
        })
        .catch((err) => console.log('getApiErrorInfo Failed', err))
    },
    getResourceError() {
      fetch('http://127.0.0.1:8000/getResourceError/')
        .then((res) => res.json())
        .then((json) => {
          this.resourceError = json.data
        })
        .catch((err) => console.log('getResourceError Failed', err))
      fetch('http://127.0.0.1:8000/getResourceErrorInfo/')
        .then((res) => res.json())
        .then((json) => {
          this.resouceErrorInfo = json.data
        })
        .catch((err) => console.log('getResourceErrorInfo Failed', err))
    }
  }
}
</script>

<style lang="scss" scoped>
* {
  box-sizing: border-box;
}
.container {
  display: flex;
  overflow: scroll;
  flex-direction: column;
  height: calc(100vh - 50px);
  background-color: #e9eef3;
  .header {
    width: calc(100% - 20px);
    height: 25vh;
    background: #fff;
    margin: 20px 10px;
    border-radius: 20px;
    display: flex;
    .sum {
      width: 25%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .right {

      flex: 1;
      display: flex;
      justify-content: space-evenly;
      align-items: center;
      .circle {
        border: 10px solid rgb(255, 94, 0);
        font-weight: bold;
        border-radius: 50%;
        aspect-ratio: 1/1;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }
      .circle:hover{
        background-color: rgb(255, 115, 0);
        color: #fff;
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
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 2vh 1vw;
      padding: 20px;
    }
  }
  .reason{
    .small{
      width: 98%;
      height: 400px;
      overflow: auto;
      background-color: #fff;
      border-radius: 25px;
      margin: 2vh 1vw;
      padding: 10px;
      h2{
        margin: 20px;
      }
      .message{
        color: red;
      }
      .time{
        color: rgb(0, 119, 255);
      }
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
      a{
        float: right;
        clear: both;
        color:rgb(0, 0, 238);
        text-decoration: underline;
      }
    }
  }
}
</style>
