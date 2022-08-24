<template>
  <div class="container">
    <div class="header">
      <div class="sum">
        <div id="Errors"></div>
      </div>
      <div class="right">
        <a class="circle">
          <p>
            JS异常: {{ JsError.total }}
            <br>
          </p>
        </a>
        <a class="circle">
          <p>
            白屏异常: {{ blank }}
            <br>
          </p>
        </a>
        <a class="circle">
          <p>
            接口异常: {{ apiError }}
            <br>
          </p>
        </a>
        <a class="circle">
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
  </div>
</template>

<script>
import { Line } from '@antv/g2plot'
import { Pie } from '@antv/g2plot'
export default {
  data() {
    return {
      JsError: {},
      apiError: {},
      blank: 0,
      resourceError: 0
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
    },
    getBlank() {
      fetch('http://127.0.0.1:8000/getBlank/')
        .then((res) => res.json())
        .then((json) => {
          this.blank = json.data
        })
        .catch((err) => console.log('getBlank Failed', err))
    },
    getApiError() {
      fetch('http://127.0.0.1:8000/getApiError/')
        .then((res) => res.json())
        .then((json) => {
          this.apiError = json.data.xhr.error + json.data.fetch.error
        })
        .catch((err) => console.log('getApiError Failed', err))
    },
    getResourceError() {
      fetch('http://127.0.0.1:8000/getResourceError/')
        .then((res) => res.json())
        .then((json) => {
          this.resourceError = json.data
        })
        .catch((err) => console.log('getResourceError Failed', err))
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
        border: 2px solid red;
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
}
</style>
