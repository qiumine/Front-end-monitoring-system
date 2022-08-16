let url = window.location.href;
let loc = url.substring(url.lastIndexOf('/') + 1, url.length);

export default function () {
    return loc;
}