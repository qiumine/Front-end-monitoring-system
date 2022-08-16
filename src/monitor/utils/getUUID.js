/**
 * 获取一个UUID
 * 格式：8-4-4-4-12
 * @returns UUID
 */
export default function () {
    return "xxxxxxxx-xxxx-xxxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, c => {
        const r = (Math.random() * 16) | 0;
        const v = c === "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
};

