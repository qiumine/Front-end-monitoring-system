let host = 'cn-guangzhou.log.aliyuncs.com';
let project = 'my-monitor';
let logStore = 'my-monitor-store';
let userAgent = require('user-agent');

function getExtraData() {
    return {
        title: document.title,
        url: location.href,
        timestamp: Date.now(),
        userAgent: userAgent.parse(navigator.userAgent).name,
    }
}
class SendTracket {
    constructor() {
        //this.url = `http://${project}.${host}/logstores/${logStore}/track`; //上报的路径
        this.url = 'http://127.0.0.1:8000/senddata/'
        // this.xhr = new XMLHttpRequest;
    }

    send(data = {}) {
        let extraData = getExtraData();
        let log = { ...extraData, ...data };
        //对象的值不能是数字
        for (let key in log) {
            if (typeof log[key] === 'number') {
                log[key] = `${log[key]}`;
            }
        }
        console.log('log:', log);
        navigator.sendBeacon(this.url, JSON.stringify(log));
    }
}

export default new SendTracket();