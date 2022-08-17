import tracker from "../utils/tracker";

const originalFetch = window.fetch;
export function injectFetch() {

    window.fetch = function newFetch(url, config) {
        const startTime = Date.now()
        const reportData = {
            kind: 'stability',
            type: 'fetch',
            startTime,
            url,
            method: (config?.method || 'GET').toUpperCase(),

        }

        return originalFetch(url, config)
            .then(res => {
                console.log('res:' + res);
                reportData.endTime = Date.now();
                reportData.duration = reportData.endTime - reportData.startTime;

                const data = res.clone();
                reportData.status = data.status;
                reportData.success = data.ok;

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