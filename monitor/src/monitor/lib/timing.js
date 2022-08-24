import getLastEvent from "../utils/getLastEvent";
import getSelector from "../utils/getSelector";
import onload from "../utils/onload";
import tracker from "../utils/tracker";
export function timing() {
    let FMP, LCP;
    //增加一个性能条目的观察者
    new PerformanceObserver((entryList, observer) => {
        let perEntries = entryList.getEntries();
        FMP = perEntries[0];
        observer.disconnect();   //停止观察
    }).observe({ entryTypes: ['element'] });  //观察页面中有意义元素

    new PerformanceObserver((entryList, observer) => {
        let perEntries = entryList.getEntries();
        LCP = perEntries[0];
        observer.disconnect();   //停止观察
    }).observe({ entryTypes: ['largest-contentful-paint'] });  //观察页面中最大元素

    new PerformanceObserver((entryList, observer) => {
        let lastEvent = getLastEvent();
        let firstInput = entryList.getEntries()[0];
        console.log('FID', firstInput);
        if (firstInput) {
            //processingStart开始处理时间 startTime开始点击时间 差值为处理延时
            let inputDelay = firstInput.processingStart - firstInput.startTime;
            let duration = firstInput.duration;
            if (inputDelay > 0 || duration > 0) {
                tracker.send({
                    kind: 'experience', //用户体验指标
                    type: 'firstInputDelay',    //首次输入延时
                    inputDelay, //延时时间
                    duration,   //处理时间
                    startTime: firstInput.startTime, //首次输入开始时间
                    Selector: lastEvent ? getSelector(lastEvent.path || lastEvent.target) : '',

                });
            }
        }
        observer.disconnect();   //停止观察
    }).observe({ type: 'first-input', buffered: true });  //观察页面用户第一次交互

    onload(function () {
        setTimeout(() => {
            const {
                fetchStart,
                connectStart,
                connectEnd,
                responseStart,
                responseEnd,
                domInteractive,
                domContentLoadedEventStart,
                domContentLoadedEventEnd,
                loadEventStart,
                domComplete,
                domainLookupEnd,
                domainLookupStart,
            } = performance.getEntriesByType("navigation")[0];
            tracker.send({
                kind: 'experience', //用户体验指标
                type: 'timing',    //统计每个阶段的时间
                connectTime: connectEnd - connectStart,    //TCP连接时间
                ttfbTime: responseEnd - responseStart,  //首字节到达时间
                responseTime: responseEnd - responseStart,  //响应的读取时间
                parseDOMTime: domComplete - domInteractive,  //DOM解析时间
                domContentLoadedTime: domContentLoadedEventEnd - domContentLoadedEventStart,    //DOMContentLoaded 事件耗时
                timeToInteractive: domInteractive - fetchStart, //首次可交互时间
                loadTime: loadEventStart - fetchStart,   //完整加载时间
                dnsTime: domainLookupEnd - domainLookupStart, // DNS 解析耗时
                domReady: domContentLoadedEventEnd - fetchStart,    //DOM阶段渲染耗时
            });
            let FP = performance.getEntriesByName('first-paint')[0];
            let FCP = performance.getEntriesByName('first-contentful-paint')[0];
            //发送性能指标
            console.log('FMP', FMP);
            console.log('FP', FP);
            console.log('FCP', FCP);
            console.log('LCP', LCP);
            tracker.send({
                kind: 'experience', //用户体验指标
                type: 'paint',    //首次输入延时
                //!格式化时间，是否存在
                firstPaint: FP ? FP.startTime : '',//首次绘制时间
                firstContentfulPaint: FCP ? FCP.startTime : '',//首次内容绘制时间
                firstMeaningfulPaint: FMP ? FMP.startTime : '',//首次有意义绘制时间
                largestContentfulPaint: LCP ? LCP.startTime : '',//最大内容渲染时间
            });
        }, 3000);
        console.log(performance.getEntriesByType("navigation"));
    });
}