/**
 * 获取浏览器唯一标识
 */
export default function () {
    return sessionStorage.getItem('cip') + '&&' + sessionStorage.getItem('cfp') + '&&' + Date.now();
};

