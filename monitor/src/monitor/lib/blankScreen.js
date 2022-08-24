import onload from "../utils/onload";
import tracker from "../utils/tracker";


export function blankScreen() {

    let warpperElement = ['html', 'body', '#container', '.content.main'];
    let emptyPoints = 0;

    function getSelector(element){
        if(element.id){
            return '#' + element.id;
        }else if (element.className){ // a b c => .a.b.c
            return '.' + element.className.split(' ').filter(item => !!item).join('.');
        }else{
            return element.nodeName.toLowerCase();
        }
    }
    function isWrapper(element){
        let selector = getSelector(element);
        if(warpperElement.indexOf(selector)!=-1){
            emptyPoints++;
        }
    }

    onload(function(){
        for(let i = 0; i <=9; i++){
            let xElements = document.elementsFromPoint(
                window.innerWidth*i/10, window.innerHeight/2);
            let yElements = document.elementsFromPoint(
                window.innerWidth/2, window.innerHeight*i/10);
                isWrapper(xElements[0]);
                isWrapper(yElements[0]);
        }
    
        if(emptyPoints > 0){
            let centerElements = document.elementsFromPoint(
                window.innerWidth/2, window.innerHeight/2
            );
    
            tracker.send({
                kind : 'stability',
                type : 'blank',
                emptyPoints,
                screen : window.screen.width + '*' + window.screen.height,
                viewPoint : window.innerWidth + '*' + window.innerHeight,
                selector : getSelector(centerElements[0]) 
            });
        }
    }); 
}