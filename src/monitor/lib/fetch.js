import tracker from "../utils/tracker";

const originalFetch = window.fetch;
export function injectFetch() {

    window.fetch = function newFetch(url, config) {
        const startTime = Date.now()
        const reportData = {
            kind: 'stability',//监控指标的大类
            type: 'fetch',//小类型
            startTime,
            url,//请求路径
            method: (config?.method || 'GET').toUpperCase(),

        }

        return originalFetch(url, config)
            .then(res => {
                // console.log('res:' + res);
                reportData.endTime = Date.now();
                reportData.duration = reportData.endTime - reportData.startTime;

                const data = res.clone();
                reportData.status = data.status; //状态码
                reportData.success = data.ok; //true flase

                tracker.send(reportData);

                return res;
            })
            .catch(err => {
                console.log('err:' + err);
                reportData.endTime = Date.now();
                reportData.duration = reportData.endTime - reportData.startTime;
                reportData.status = 0;
                reportData.success = false;

                tracker.send(reportData);

                throw err;
            })
    }
}