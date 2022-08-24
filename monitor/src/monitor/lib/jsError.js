import getLastEvent from "../utils/getLastEvent";
import getSelector from "../utils/getSelector";
import tracker from "../utils/tracker";

export function injectJsError() {
    //监听全局未捕获的错误
    window.addEventListener('error', function (event) {//错误事件对象
        console.log('error', event);
        let lastEvent = getLastEvent(); //最后一个交互事件
        if (event.target && (event.target.src || event.target.href)) {
            //脚本加载错误
            tracker.send({
                kind: 'stability', //监控指标的大类
                type: 'error', //小类型
                errorType: 'resourceError', //js或css资源加载错误
                filename: event.target.src || event.target.href,
                tagName: event.target.tagName,// script
                selector: getSelector(event.target),//最后一个操作元素
            });
        } else {
            tracker.send({
                kind: 'stability', //监控指标的大类
                type: 'error', //小类型
                errorType: 'jsError', //js执行错误
                //url: '', //访问哪个路径报错
                message: event.message,//报错信息
                filename: event.filename,
                position: `${event.lineno}:${event.colno}`,
                stack: getLines(event.error.stack),
                selector: lastEvent ? getSelector(lastEvent.path) : ''//最后一个操作元素
            });
        }
    }, true);

    window.addEventListener('unhandledrejection', (event) => {
        console.log(event);
        let lastEvent = getLastEvent(); //最后一个交互事件
        let reason = event.reason;
        let message;
        let filename = '';
        let line = 0;
        let column = 0;
        let stack = '';

        if (typeof reason === 'string') {//reason是一个字符串  reject('error');
            message = reason;
        } else if (typeof reason === 'object') {//reason是一个错误对象  window.someVar.error = 'error';
            if (reason.stack) {
                //at http://localhost:8080/:23:38
                let matchResult = reason.stack.match(/at\s+(.+):(\d+):(\d+)/);
                filename = matchResult[1];
                line = matchResult[2];
                column = matchResult[3];
            }
            stack = getLines(reason.stack);
            message = reason.message;
        }
        tracker.send({
            kind: 'stability', //监控指标的大类
            type: 'error', //小类型
            errorType: 'promiseError', //promise错误
            message,//报错信息
            filename,
            position: `${line}:${column}`,
            stack,
            selector: lastEvent ? getSelector(lastEvent.path) : ''//最后一个操作元素
        });
    }, true);

    function getLines(stack) {
        return stack.split('\n').slice(1).map(item => item.replace(/^\s+at\s+/g, "")).join('^');
    }
}