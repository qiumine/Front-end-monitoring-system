import tracker from "../utils/tracker";
import getPageURL from "../utils/getPageURL";
import getUID from "../utils/getUID";

export function pv() {
    //pv 页面浏览量上报
    tracker.send({
        kind: "business",
        type: "pv",
        startTime: performance.now(),
        pageURL: getPageURL(),  //页面url
        referrer: document.referrer,
        uuid: getUID(),    //浏览器唯一标识
    });
    let startTime = Date.now();
    window.addEventListener("beforeunload", () => {
        let stayTime = Date.now() - startTime;
        //页面停留时间上报
        tracker.send({
            kind: "business",
            type: "stayTime",
            stayTime,   //页面停留时间
            pageURL: getPageURL(), //页面url
            uuid: getUID(),  //浏览器唯一标识
        });
    },
        false
    );
}