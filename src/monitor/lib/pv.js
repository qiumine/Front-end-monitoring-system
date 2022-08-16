import tracker from "../utils/tracker";
import getPageURL from "../utils/getPageURL";
import getUUID from "../utils/getUUID";

export function pv() {
    //pv 页面浏览量上报
    tracker.send({
        kind: "business",
        type: "pv",
        startTime: performance.now(),
        pageURL: getPageURL(),
        referrer: document.referrer,
        uuid: getUUID(), //业务相关
    });
    let startTime = Date.now();
    window.addEventListener("beforeunload", () => {
        let stayTime = Date.now() - startTime;
        //页面停留时间上报
        tracker.send({
            kind: "business",
            type: "stayTime",
            stayTime,   //页面停留时间
            pageURL: getPageURL(),
            uuid: getUUID(),     //业务相关
        });
    },
        false
    );
}