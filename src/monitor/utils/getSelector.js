
function getSelector(path) {
    //反转过滤选择器
    return path.reverse().filter(element => {
        return element !== document && element !== window;
    }).map(element => {
        let selector = '';
        if (element.id) {
            return `${element.nodeName.toLowerCase()}#${element.id}`;
        } else if (element.className) {
            return `${element.nodeName.toLowerCase()}.${element.className}`;
        } else {
            selector = element.nodeName.toLowerCase();
        }
        return selector;
    }).join(' ');
}

export default function (pathsOrTarget) {
    if (Array.isArray(pathsOrTarget)) {
        return getSelector(pathsOrTarget);
    } else {
        let path = [];
        while (pathsOrTarget) {
            path.push(pathsOrTarget);
            pathsOrTarget = pathsOrTarget.parentNode;
        }
        return getSelector(path);
    }
}